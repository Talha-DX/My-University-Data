import json
import sqlite3
from datetime import datetime
import threading

class SecurityLogger:
    def __init__(self, db_file='data/logs.db'):
        self.db_file = db_file
        self.lock = threading.Lock()
        self.init_database()
        self.failed_attempts = {}  # Track failed logins per IP/user
    
    def init_database(self):
        """Initialize SQLite database"""
        with self.lock:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Create logs table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS security_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    user TEXT,
                    details TEXT,
                    ip_address TEXT DEFAULT '127.0.0.1'
                )
            ''')
            
            # Create intrusion attempts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS intrusion_attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    source TEXT,
                    attack_type TEXT,
                    details TEXT,
                    blocked INTEGER DEFAULT 1
                )
            ''')
            
            conn.commit()
            conn.close()
    
    def log_event(self, event_type, details, user=None):
        """Log security event"""
        timestamp = datetime.now().isoformat()
        
        with self.lock:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO security_logs (timestamp, event_type, user, details)
                VALUES (?, ?, ?, ?)
            ''', (timestamp, event_type, user, details))
            
            # Check for intrusion patterns
            if event_type == "AUTH_FAIL":
                self._check_intrusion_patterns(user, details)
            
            conn.commit()
            conn.close()
        
        # Also print to console for debugging
        print(f"[{timestamp}] {event_type}: {details}")
    
    def _check_intrusion_patterns(self, user, details):
        """Detect potential intrusion attempts"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Check for multiple failed attempts in last 5 minutes
        cursor.execute('''
            SELECT COUNT(*) FROM security_logs 
            WHERE event_type = 'AUTH_FAIL' 
            AND timestamp > datetime('now', '-5 minutes')
        ''')
        
        recent_fails = cursor.fetchone()[0]
        
        if recent_fails >= 3:
            # Log intrusion attempt
            cursor.execute('''
                INSERT INTO intrusion_attempts (timestamp, source, attack_type, details)
                VALUES (datetime('now'), ?, ?, ?)
            ''', (user or 'Unknown', 'Brute Force', f'Multiple failed attempts: {recent_fails}'))
            
            # Alert could be sent here (email, SMS, etc.)
            print(f"⚠️ INTRUSION ALERT: {recent_fails} failed attempts detected!")
        
        conn.commit()
        conn.close()
    
    def get_recent_logs(self, limit=50):
        """Get recent security logs"""
        with self.lock:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT timestamp, event_type, user, details 
                FROM security_logs 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
            
            logs = cursor.fetchall()
            conn.close()
            
            return [{
                'timestamp': log[0],
                'event_type': log[1],
                'user': log[2],
                'details': log[3]
            } for log in logs]
    
    def get_intrusion_attempts(self):
        """Get all intrusion attempts"""
        with self.lock:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT timestamp, source, attack_type, details 
                FROM intrusion_attempts 
                ORDER BY timestamp DESC
            ''')
            
            attempts = cursor.fetchall()
            conn.close()
            
            return [{
                'timestamp': attempt[0],
                'source': attempt[1],
                'attack_type': attempt[2],
                'details': attempt[3]
            } for attempt in attempts]

# Global logger instance
logger = SecurityLogger()

def log_event(event_type, details, user=None):
    """Convenience function for logging"""
    logger.log_event(event_type, details, user)