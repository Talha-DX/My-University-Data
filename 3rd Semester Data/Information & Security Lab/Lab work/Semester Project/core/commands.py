from core.logging import log_event
from core.encryption import ClassicalCiphers
import json
from datetime import datetime

class CommandSystem:
    # Available mission commands
    MISSION_COMMANDS = [
        "ACTIVATE_THRUSTER",
        "DEPLOY_SOLAR_PANELS",
        "ROTATE_SATELLITE",
        "COLLECT_TELEMETRY",
        "ADJUST_ORBIT",
        "SEND_DATA_STREAM",
        "ENTER_SAFE_MODE",
        "PERFORM_DIAGNOSTICS"
    ]
    
    def __init__(self):
        self.command_history = []
    
    def get_commands_by_role(self, role):
        """Return available commands based on role"""
        if role == "Admin":
            return self.MISSION_COMMANDS + ["ADD_USER", "VIEW_LOGS", "SYSTEM_STATUS"]
        elif role == "Engineer":
            return self.MISSION_COMMANDS
        elif role == "Observer":
            return ["VIEW_TELEMETRY", "REQUEST_DATA"]
        return []
    
    def execute_command(self, user, role, command, cipher_type=None, key=""):
        """Execute a command with optional encryption"""
        # Check authorization
        available_commands = self.get_commands_by_role(role)
        if command not in available_commands:
            log_event("UNAUTHORIZED", f"User {user} tried unauthorized command: {command}")
            return False, "Unauthorized command for your role"
        
        # Encrypt if requested
        original_command = command
        if cipher_type and key:
            if cipher_type == "Caesar":
                command = ClassicalCiphers.caesar_encrypt(command, int(key))
            elif cipher_type == "Vigenère":
                command = ClassicalCiphers.vigenere_encrypt(command, key)
            elif cipher_type == "Rail Fence":
                command = ClassicalCiphers.rail_fence_encrypt(command, int(key))
        
        # Simulate command execution
        response = self.simulate_command_response(original_command)
        
        # Log and store
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "role": role,
            "command": original_command,
            "encrypted": command if cipher_type else None,
            "cipher": cipher_type,
            "response": response
        }
        
        self.command_history.append(log_entry)
        log_event("COMMAND", f"{user} executed: {original_command}")
        
        return True, f"✓ Command executed: {response}"
    
    def simulate_command_response(self, command):
        """Simulate realistic satellite responses"""
        responses = {
            "ACTIVATE_THRUSTER": "Thruster activated. Delta-V: 5.2 m/s",
            "DEPLOY_SOLAR_PANELS": "Solar panels deployed. Power: +150W",
            "ROTATE_SATELLITE": "Satellite rotated 45°. New orientation confirmed",
            "COLLECT_TELEMETRY": "Telemetry collected. Temp: 22°C, Power: 87%",
            "ADJUST_ORBIT": "Orbit adjusted. Apogee: 650km, Perigee: 620km",
            "SEND_DATA_STREAM": "Data stream initiated. Rate: 2.5 Mbps",
            "ENTER_SAFE_MODE": "Safe mode engaged. All systems nominal",
            "PERFORM_DIAGNOSTICS": "Diagnostics complete. All systems OK",
            "ADD_USER": "User management panel opened",
            "VIEW_LOGS": "Security logs displayed",
            "SYSTEM_STATUS": "All systems operational. Satellites: 3 online",
            "VIEW_TELEMETRY": "Telemetry dashboard displayed",
            "REQUEST_DATA": "Data request queued for transmission"
        }
        return responses.get(command, "Command acknowledged")
    
    def get_command_history(self, user=None):
        """Get command history, optionally filtered by user"""
        if user:
            return [cmd for cmd in self.command_history if cmd['user'] == user]
        return self.command_history