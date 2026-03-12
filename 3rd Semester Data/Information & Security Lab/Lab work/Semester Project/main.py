import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from datetime import datetime
from core.auth import AuthenticationSystem
from core.commands import CommandSystem
from core.logging import SecurityLogger
from core.encryption import ClassicalCiphers


class SpaceComDefenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 SpaceCom Defender - Mission Control")
        self.root.geometry("1200x700")
        self.root.configure(bg='#0a0a2a')
        # Initialize systems
        self.auth_system = AuthenticationSystem()
        self.command_system = CommandSystem()
        self.logger = SecurityLogger()
        # GUI Variables
        self.login_frame = None
        self.main_frame = None
        self.current_user = None
        self.current_role = None
        # Styles
        self.setup_styles()
        # Start with login
        self.show_login_screen()

    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        # Configure colors
        bg_color = '#0a0a2a'
        fg_color = '#ffffff'
        accent_color = '#00ffff'
        button_color = '#1a1a3a'
        style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Segoe UI', 10))
        style.configure('TButton', background=button_color, foreground=fg_color,
                        font=('Segoe UI', 10, 'bold'), borderwidth=0)
        style.configure('Title.TLabel', font=('Segoe UI', 20, 'bold'), foreground=accent_color)
        style.configure('Role.TLabel', font=('Segoe UI', 12), foreground='#ffaa00')

    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        """Display login screen"""
        self.clear_window()
        # Main container
        container = tk.Frame(self.root, bg='#0a0a2a')
        container.pack(expand=True, fill='both', padx=50, pady=50)
        # Title
        title = ttk.Label(container, text="🚀 SPACECOM DEFENDER", style='Title.TLabel')
        title.pack(pady=(0, 30))
        subtitle = ttk.Label(container, text="Secure Mission Control System",
                             font=('Segoe UI', 12), foreground='#8888ff')
        subtitle.pack(pady=(0, 50))
        # Login Frame
        login_frame = tk.Frame(container, bg='#1a1a3a', relief='ridge', borderwidth=2)
        login_frame.pack(padx=100, pady=20, fill='x')
        # Username
        tk.Label(login_frame, text="Username:", bg='#1a1a3a', fg='white',
                 font=('Segoe UI', 11)).pack(pady=(20, 5), padx=20, anchor='w')
        self.username_entry = ttk.Entry(login_frame, font=('Segoe UI', 11), width=30)
        self.username_entry.pack(pady=(0, 15), padx=20, fill='x')
        self.username_entry.insert(0, "admin")  # Default for testing
        # Password
        tk.Label(login_frame, text="Password:", bg='#1a1a3a', fg='white',
                 font=('Segoe UI', 11)).pack(pady=(0, 5), padx=20, anchor='w')
        self.password_entry = ttk.Entry(login_frame, show="*", font=('Segoe UI', 11), width=30)
        self.password_entry.pack(pady=(0, 20), padx=20, fill='x')
        self.password_entry.insert(0, "123")  # Default for testing
        # Login Button
        login_btn = ttk.Button(login_frame, text="🔐 SECURE LOGIN",
                               command=self.attempt_login, style='TButton')
        login_btn.pack(pady=(0, 20), padx=20, fill='x')
        # Demo credentials
        cred_frame = tk.Frame(container, bg='#0a0a2a')
        cred_frame.pack(pady=(20, 0))
        tk.Label(cred_frame, text="Demo Credentials:", bg='#0a0a2a', fg='#8888ff',
                 font=('Segoe UI', 9)).pack()
        cred_text = "admin/123 (Admin) | engineer/123 (Engineer) | observer/123 (Observer)"
        tk.Label(cred_frame, text=cred_text, bg='#0a0a2a', fg='#aaaaaa',
                 font=('Courier', 8)).pack(pady=(5, 0))

    def attempt_login(self):
        """Attempt user login"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return
        # Show loading
        loading = tk.Label(self.root, text="🔐 Authenticating...",
                           bg='#0a0a2a', fg='#00ff00', font=('Segoe UI', 10))
        loading.place(relx=0.5, rely=0.8, anchor='center')
        self.root.update()
        # Simulate authentication delay
        self.root.after(500, lambda: self.process_login(username, password, loading))

    def process_login(self, username, password, loading):
        """Process login authentication"""
        success, message = self.auth_system.login(username, password)
        loading.destroy()
        if success:
            self.current_user = username
            self.current_role = self.auth_system.get_user_role()
            messagebox.showinfo("Access Granted", message)
            self.show_main_dashboard()
        else:
            messagebox.showerror("Access Denied", message)

    def show_main_dashboard(self):
        """Display main dashboard after login"""
        self.clear_window()
        # Configure root grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        # Header
        header = tk.Frame(self.root, bg='#1a1a3a', height=60)
        header.grid(row=0, column=0, sticky='ew')
        header.grid_columnconfigure(1, weight=1)
        # Logo/Title
        tk.Label(header, text="🚀 SPACECOM DEFENDER", bg='#1a1a3a',
                 fg='#00ffff', font=('Segoe UI', 16, 'bold')).grid(row=0, column=0, padx=20, pady=10)
        # User info
        user_info = tk.Frame(header, bg='#1a1a3a')
        user_info.grid(row=0, column=1, sticky='e', padx=20)
        tk.Label(user_info, text=f"User: {self.current_user}", bg='#1a1a3a',
                 fg='white', font=('Segoe UI', 10)).pack(side='left', padx=(0, 10))
        role_color = {'Admin': '#ff5555', 'Engineer': '#55ff55', 'Observer': '#5555ff'}
        tk.Label(user_info, text=f"Role: {self.current_role}", bg='#1a1a3a',
                 fg=role_color.get(self.current_role, 'white'),
                 font=('Segoe UI', 10, 'bold')).pack(side='left', padx=(0, 20))
        # Logout button
        ttk.Button(user_info, text="🚪 Logout", command=self.logout,
                   style='TButton').pack(side='left')
        # Main content area (Notebook for tabs)
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        # Create tabs based on role
        self.create_command_tab(notebook)
        self.create_encryption_tab(notebook)
        self.create_logs_tab(notebook)
        if self.current_role == "Admin":
            self.create_admin_tab(notebook)
        # Status bar
        status_bar = tk.Frame(self.root, bg='#2a2a4a', height=30)
        status_bar.grid(row=2, column=0, sticky='ew')
        status_text = f"🛰️ Mission Control Online | Secure Connection Established | Last Login: {datetime.now().strftime('%H:%M:%S')}"
        tk.Label(status_bar, text=status_text, bg='#2a2a4a', fg='#88ff88',
                 font=('Segoe UI', 9)).pack(side='left', padx=10)

    def create_command_tab(self, notebook):
        """Create command execution tab"""
        tab = ttk.Frame(notebook)
        notebook.add(tab, text='📡 Mission Commands')
        # Left panel - Available commands
        left_panel = tk.Frame(tab, bg='#1a1a2a')
        left_panel.pack(side='left', fill='y', padx=(0, 5))
        tk.Label(left_panel, text="Available Commands", bg='#1a1a2a',
                 fg='#00ffff', font=('Segoe UI', 12, 'bold')).pack(pady=(10, 5))
        # Command listbox
        commands_frame = tk.Frame(left_panel, bg='#1a1a2a')
        commands_frame.pack(fill='both', expand=True, padx=10, pady=5)
        self.command_listbox = tk.Listbox(commands_frame, bg='#0a0a1a', fg='white',
                                          selectbackground='#2a4a6a', font=('Courier', 10),
                                          height=15)
        self.command_listbox.pack(fill='both', expand=True)
        # Populate commands based on role
        available_commands = self.command_system.get_commands_by_role(self.current_role)
        for cmd in available_commands:
            self.command_listbox.insert(tk.END, f"▶ {cmd}")
        # Right panel - Command execution
        right_panel = tk.Frame(tab, bg='#1a1a2a')
        right_panel.pack(side='right', fill='both', expand=True, padx=(5, 0))
        tk.Label(right_panel, text="Command Execution", bg='#1a1a2a',
                 fg='#00ffff', font=('Segoe UI', 12, 'bold')).pack(pady=(10, 5))
        # Command details
        details_frame = tk.Frame(right_panel, bg='#2a2a3a', relief='sunken', borderwidth=1)
        details_frame.pack(fill='x', padx=10, pady=5)
        self.selected_command = tk.StringVar(value="Select a command from the list")
        tk.Label(details_frame, textvariable=self.selected_command, bg='#2a2a3a',
                 fg='#ffff88', font=('Courier', 11)).pack(pady=10, padx=10)
        # Encryption options
        encrypt_frame = tk.LabelFrame(right_panel, text="🔒 Encryption Options",
                                     bg='#1a1a2a', fg='white', font=('Segoe UI', 10))
        encrypt_frame.pack(fill='x', padx=10, pady=10)
        # Cipher selection
        tk.Label(encrypt_frame, text="Cipher:", bg='#1a1a2a', fg='white').grid(row=0, column=0, padx=5, pady=5)
        self.cipher_var = tk.StringVar(value="None")
        cipher_combo = ttk.Combobox(encrypt_frame, textvariable=self.cipher_var,
                                    values=["None", "Caesar", "Vigenère", "Rail Fence"],
                                    state='readonly', width=15)
        cipher_combo.grid(row=0, column=1, padx=5, pady=5)
        # Key entry
        self.key_label = tk.Label(encrypt_frame, text="Key:", bg='#1a1a2a', fg='white')
        self.key_label.grid(row=0, column=2, padx=5, pady=5)
        self.key_entry = ttk.Entry(encrypt_frame, width=15)
        self.key_entry.grid(row=0, column=3, padx=5, pady=5)
        self.key_label.grid_remove()
        self.key_entry.grid_remove()
        # Bind cipher change
        cipher_combo.bind('<<ComboboxSelected>>', self.on_cipher_change)
        # Execute button
        execute_btn = ttk.Button(right_panel, text="🚀 EXECUTE COMMAND",
                                 command=self.execute_selected_command,
                                 style='TButton')
        execute_btn.pack(pady=20)
        # Response area
        response_frame = tk.LabelFrame(right_panel, text="Satellite Response",
                                       bg='#1a1a2a', fg='white', font=('Segoe UI', 10))
        response_frame.pack(fill='both', expand=True, padx=10, pady=5)
        self.response_text = scrolledtext.ScrolledText(response_frame, bg='#0a0a1a',
                                                       fg='#88ff88', font=('Courier', 10),
                                                       height=8)
        self.response_text.pack(fill='both', expand=True, padx=5, pady=5)
        # Bind listbox selection
        self.command_listbox.bind('<<ListboxSelect>>', self.on_command_select)

    def on_cipher_change(self, event):
        """Show/hide key entry based on cipher selection"""
        cipher = self.cipher_var.get()
        if cipher == "None":
            self.key_label.grid_remove()
            self.key_entry.grid_remove()
        else:
            self.key_label.grid()
            self.key_entry.grid()
            # Set placeholder based on cipher
            if cipher == "Caesar":
                self.key_entry.delete(0, tk.END)
                self.key_entry.insert(0, "3")
            elif cipher == "Rail Fence":
                self.key_entry.delete(0, tk.END)
                self.key_entry.insert(0, "3")

    def on_command_select(self, event):
        """Handle command selection from listbox"""
        selection = self.command_listbox.curselection()
        if selection:
            cmd = self.command_listbox.get(selection[0])
            cmd = cmd.replace("▶ ", "")
            self.selected_command.set(f"Selected: {cmd}")

    def execute_selected_command(self):
        """Execute the selected command"""
        selection = self.command_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a command first")
            return
        cmd = self.command_listbox.get(selection[0])
        cmd = cmd.replace("▶ ", "")
        # Get encryption options
        cipher = self.cipher_var.get()
        key = self.key_entry.get() if cipher != "None" else ""
        # Validate key for selected cipher
        if cipher == "Caesar":
            if not key.isdigit():
                messagebox.showerror("Invalid Key", "Caesar cipher requires numeric key")
                return
        elif cipher == "Rail Fence":
            if not key.isdigit() or int(key) < 2:
                messagebox.showerror("Invalid Key", "Rail Fence requires integer key ≥ 2")
                return
        # Execute command
        success, response = self.command_system.execute_command(
            self.current_user, self.current_role, cmd, cipher, key
        )
        if success:
            self.response_text.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}] {response}")
            self.response_text.see(tk.END)
            # Show encrypted command if applicable
            if cipher != "None":
                encrypted_msg = f"Encrypted command sent: {self.get_encrypted_preview(cmd, cipher, key)}"
                self.response_text.insert(tk.END, f"\n{encrypted_msg}")
                self.response_text.see(tk.END)
        else:
            messagebox.showerror("Command Failed", response)

    def get_encrypted_preview(self, command, cipher, key):
        """Get preview of encrypted command"""
        if cipher == "Caesar":
            return ClassicalCiphers.caesar_encrypt(command, int(key))
        elif cipher == "Vigenère":
            return ClassicalCiphers.vigenere_encrypt(command, key)
        elif cipher == "Rail Fence":
            return ClassicalCiphers.rail_fence_encrypt(command, int(key))
        return command

    def create_encryption_tab(self, notebook):
        """Create encryption/decryption testing tab"""
        tab = ttk.Frame(notebook)
        notebook.add(tab, text='🔐 Encryption Lab')
        # Top panel - Input
        top_panel = tk.Frame(tab, bg='#1a1a2a')
        top_panel.pack(fill='x', padx=10, pady=10)
        tk.Label(top_panel, text="Plaintext:", bg='#1a1a2a', fg='white').grid(row=0, column=0, padx=5, pady=5)
        self.plaintext_entry = tk.Text(top_panel, height=4, width=50, bg='#0a0a1a', fg='white')
        self.plaintext_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        self.plaintext_entry.insert('1.0', "ACTIVATE_THRUSTER")
        # Cipher selection
        tk.Label(top_panel, text="Cipher:", bg='#1a1a2a', fg='white').grid(row=1, column=0, padx=5, pady=5)
        self.test_cipher_var = tk.StringVar(value="Caesar")
        cipher_combo = ttk.Combobox(top_panel, textvariable=self.test_cipher_var,
                                    values=["Caesar", "Vigenère", "Rail Fence"],
                                    state='readonly', width=15)
        cipher_combo.grid(row=1, column=1, padx=5, pady=5)
        # Key entry
        tk.Label(top_panel, text="Key:", bg='#1a1a2a', fg='white').grid(row=1, column=2, padx=5, pady=5)
        self.test_key_entry = ttk.Entry(top_panel, width=15)
        self.test_key_entry.grid(row=1, column=3, padx=5, pady=5)
        self.test_key_entry.insert(0, "3")
        # Buttons
        button_frame = tk.Frame(top_panel, bg='#1a1a2a')
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        ttk.Button(button_frame, text="Encrypt", command=self.test_encrypt).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Decrypt", command=self.test_decrypt).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_encryption_test).pack(side='left', padx=5)
        # Results panel
        results_frame = tk.LabelFrame(tab, text="Results", bg='#1a1a2a', fg='white')
        results_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.results_text = scrolledtext.ScrolledText(results_frame, bg='#0a0a1a',
                                                      fg='#88ff88', font=('Courier', 10))
        self.results_text.pack(fill='both', expand=True, padx=5, pady=5)

    def test_encrypt(self):
        """Test encryption function"""
        plaintext = self.plaintext_entry.get('1.0', tk.END).strip()
        cipher = self.test_cipher_var.get()
        key = self.test_key_entry.get()
        if not plaintext:
            messagebox.showwarning("No Input", "Enter text to encrypt")
            return
        try:
            if cipher == "Caesar":
                result = ClassicalCiphers.caesar_encrypt(plaintext, int(key))
            elif cipher == "Vigenère":
                result = ClassicalCiphers.vigenere_encrypt(plaintext, key)
            elif cipher == "Rail Fence":
                result = ClassicalCiphers.rail_fence_encrypt(plaintext, int(key))
            self.results_text.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}]")
            self.results_text.insert(tk.END, f"\nCipher: {cipher}")
            self.results_text.insert(tk.END, f"\nKey: {key}")
            self.results_text.insert(tk.END, f"\nPlaintext: {plaintext}")
            self.results_text.insert(tk.END, f"\nCiphertext: {result}")
            self.results_text.insert(tk.END, "\n" + "="*50 + "\n")
            self.results_text.see(tk.END)
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))

    def test_decrypt(self):
        """Test decryption function"""
        ciphertext = self.plaintext_entry.get('1.0', tk.END).strip()
        cipher = self.test_cipher_var.get()
        key = self.test_key_entry.get()
        if not ciphertext:
            messagebox.showwarning("No Input", "Enter text to decrypt")
            return
        try:
            if cipher == "Caesar":
                result = ClassicalCiphers.caesar_decrypt(ciphertext, int(key))
            elif cipher == "Vigenère":
                result = ClassicalCiphers.vigenere_decrypt(ciphertext, key)
            elif cipher == "Rail Fence":
                result = ClassicalCiphers.rail_fence_decrypt(ciphertext, int(key))
            self.results_text.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}]")
            self.results_text.insert(tk.END, f"\nCipher: {cipher}")
            self.results_text.insert(tk.END, f"\nKey: {key}")
            self.results_text.insert(tk.END, f"\nCiphertext: {ciphertext}")
            self.results_text.insert(tk.END, f"\nPlaintext: {result}")
            self.results_text.insert(tk.END, "\n" + "="*50 + "\n")
            self.results_text.see(tk.END)
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

    def clear_encryption_test(self):
        """Clear encryption test results"""
        self.results_text.delete('1.0', tk.END)

    def create_logs_tab(self, notebook):
        """Create security logs tab"""
        tab = ttk.Frame(notebook)
        notebook.add(tab, text='📊 Security Logs')
        # Toolbar
        toolbar = tk.Frame(tab, bg='#1a1a2a')
        toolbar.pack(fill='x', padx=10, pady=5)
        ttk.Button(toolbar, text="🔄 Refresh", command=self.refresh_logs).pack(side='left', padx=5)
        ttk.Button(toolbar, text="📋 Copy", command=self.copy_logs).pack(side='left', padx=5)
        ttk.Button(toolbar, text="🗑️ Clear", command=self.clear_logs).pack(side='left', padx=5)
        # Logs display
        logs_frame = tk.Frame(tab, bg='#1a1a2a')
        logs_frame.pack(fill='both', expand=True, padx=10, pady=5)
        # Create Treeview for logs
        columns = ('Time', 'Event', 'User', 'Details')
        self.logs_tree = ttk.Treeview(logs_frame, columns=columns, show='headings', height=15)
        # Define headings
        for col in columns:
            self.logs_tree.heading(col, text=col)
            self.logs_tree.column(col, width=150 if col != 'Details' else 300)
        # Add scrollbar
        scrollbar = ttk.Scrollbar(logs_frame, orient=tk.VERTICAL, command=self.logs_tree.yview)
        self.logs_tree.configure(yscrollcommand=scrollbar.set)
        self.logs_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        # Style treeview
        style = ttk.Style()
        style.configure("Treeview", background="#0a0a1a", foreground="white", fieldbackground="#0a0a1a")
        style.map('Treeview', background=[('selected', '#2a4a6a')])
        # Load initial logs
        self.refresh_logs()

    def refresh_logs(self):
        """Refresh logs display"""
        # Clear existing items
        for item in self.logs_tree.get_children():
            self.logs_tree.delete(item)
        # Get logs from database
        logs = self.logger.get_recent_logs(limit=100)
        # Add logs to treeview with color coding
        for log in logs:
            event_type = log['event_type']
            # Color coding based on event type
            tags = ()
            if "AUTH_FAIL" in event_type:
                tags = ('fail',)
            elif "INTRUSION" in event_type:
                tags = ('intrusion',)
            elif "SUCCESS" in event_type:
                tags = ('success',)
            self.logs_tree.insert('', tk.END, values=(
                log['timestamp'][11:19],  # Just time
                log['event_type'],
                log['user'] or 'N/A',
                log['details'][:50] + "..." if len(log['details']) > 50 else log['details']
            ), tags=tags)
        # Configure tag colors
        self.logs_tree.tag_configure('fail', foreground='#ff6666')
        self.logs_tree.tag_configure('intrusion', foreground='#ff0000', font=('Segoe UI', 9, 'bold'))
        self.logs_tree.tag_configure('success', foreground='#66ff66')

    def copy_logs(self):
        """Copy selected log to clipboard"""
        selection = self.logs_tree.selection()
        if selection:
            item = self.logs_tree.item(selection[0])
            self.root.clipboard_clear()
            self.root.clipboard_append(str(item['values']))
            messagebox.showinfo("Copied", "Log entry copied to clipboard")

    def clear_logs(self):
        """Clear logs (demo only - in real system this would require admin)"""
        if messagebox.askyesno("Confirm", "Clear all logs? (Demo only)"):
            for item in self.logs_tree.get_children():
                self.logs_tree.delete(item)

    def create_admin_tab(self, notebook):
        """Create admin-only tab"""
        if self.current_role != "Admin":
            return
        tab = ttk.Frame(notebook)
        notebook.add(tab, text='⚙️ Admin Panel')
        # Admin controls
        tk.Label(tab, text="Administrator Controls", font=('Segoe UI', 14, 'bold'),
                 bg='#1a1a2a', fg='#ff5555').pack(pady=10)
        # User management frame
        user_frame = tk.LabelFrame(tab, text="User Management", bg='#1a1a2a', fg='white')
        user_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(user_frame, text="Username:", bg='#1a1a2a', fg='white').grid(row=0, column=0, padx=5, pady=5)
        new_user_entry = ttk.Entry(user_frame, width=20)
        new_user_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(user_frame, text="Role:", bg='#1a1a2a', fg='white').grid(row=0, column=2, padx=5, pady=5)
        role_combo = ttk.Combobox(user_frame, values=["Admin", "Engineer", "Observer"], width=15)
        role_combo.grid(row=0, column=3, padx=5, pady=5)
        role_combo.set("Engineer")
        ttk.Button(user_frame, text="Add User",
                   command=lambda: self.simulate_add_user(new_user_entry.get(), role_combo.get())).grid(row=0, column=4, padx=10, pady=5)
        # System status
        status_frame = tk.LabelFrame(tab, text="System Status", bg='#1a1a2a', fg='white')
        status_frame.pack(fill='x', padx=20, pady=10)
        status_text = """🟢 Authentication System: ONLINE
🟢 Command System: ONLINE
🟢 Encryption Module: ONLINE
🟢 Logging System: ONLINE
🟢 Intrusion Detection: ACTIVE
📊 Total Logs: 1,247 entries
🚨 Intrusion Attempts: 3 blocked today
👥 Active Users: 3 registered"""
        tk.Label(status_frame, text=status_text, bg='#1a1a2a', fg='#88ff88',
                 font=('Courier', 10), justify='left').pack(padx=10, pady=10)
        # Quick actions
        action_frame = tk.Frame(tab, bg='#1a1a2a')
        action_frame.pack(pady=20)
        ttk.Button(action_frame, text="Run Security Audit",
                   command=self.run_audit).pack(side='left', padx=5)
        ttk.Button(action_frame, text="Export Logs",
                   command=self.export_logs).pack(side='left', padx=5)
        ttk.Button(action_frame, text="Backup System",
                   command=self.backup_system).pack(side='left', padx=5)

    def simulate_add_user(self, username, role):
        """Simulate adding a user (demo only)"""
        if not username:
            messagebox.showerror("Error", "Enter username")
            return
        messagebox.showinfo("User Added",
                            f"User '{username}' added with role '{role}'\n\nNote: This is a simulation. In a real system, this would update the database.")

    def run_audit(self):
        """Run security audit simulation"""
        messagebox.showinfo("Security Audit",
                            "Security audit completed!\n\n✓ All systems secure\n✓ No vulnerabilities found\n✓ Encryption strength: Excellent")

    def export_logs(self):
        """Export logs simulation"""
        messagebox.showinfo("Export Logs",
                            "Logs exported to 'security_logs_export.csv'\n\nContains 1,247 security events")

    def backup_system(self):
        """Backup system simulation"""
        messagebox.showinfo("Backup",
                            "System backup created successfully!\n\nBackup file: spacecom_backup_2024.bak")

    def logout(self):
        """Logout user"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.auth_system.logout()
            self.show_login_screen()


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = SpaceComDefenderGUI(root)
    root.mainloop()


if __name__ == "__main__":

    import os
    os.makedirs('data', exist_ok=True)
    os.makedirs('core', exist_ok=True)
    main()