import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from modules.locker import encryptor, decryptor
from modules.meta_process import extract_metadata
import os
import webbrowser

VERSION = "1.1.0"

class SafeBoxGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" S4D0X - SafeBox File Security.")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Variables
        self.encrypt_file_path = tk.StringVar()
        self.encrypt_output_path = tk.StringVar()
        self.encrypt_password = tk.StringVar()
        self.decrypt_file_path = tk.StringVar()
        self.decrypt_output_path = tk.StringVar()
        self.decrypt_output_dir = tk.StringVar()
        self.decrypt_password = tk.StringVar()
        self.use_original_name = tk.BooleanVar(value=True)
        
        # Main frame
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)
        
        # Title
        tk.Label(self.main_frame, text="SafeBox", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Encryption tab
        self.encrypt_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encrypt_tab, text="Encrypt")
        self.setup_encrypt_tab()
        
        # Decryption tab
        self.decrypt_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.decrypt_tab, text="Decrypt")
        self.setup_decrypt_tab()
        
        # About tab
        self.about_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.about_tab, text="About")
        self.setup_about_tab()
        
        # Status label
        self.status = tk.Label(self.main_frame, text="Ready", wraplength=500, fg="blue")
        self.status.pack(pady=10)
    
    def setup_encrypt_tab(self):
        # File selection
        file_frame = tk.Frame(self.encrypt_tab)
        file_frame.pack(fill="x", pady=5)
        tk.Label(file_frame, text="Input File:", width=15, anchor="w").pack(side="left")
        tk.Entry(file_frame, textvariable=self.encrypt_file_path, width=40, state="readonly").pack(side="left", padx=5)
        tk.Button(file_frame, text="Browse", command=self.browse_encrypt_file).pack(side="left")
        
        # Password
        pass_frame = tk.Frame(self.encrypt_tab)
        pass_frame.pack(fill="x", pady=5)
        tk.Label(pass_frame, text="Password:", width=15, anchor="w").pack(side="left")
        tk.Entry(pass_frame, textvariable=self.encrypt_password, width=40, show="*").pack(side="left", padx=5)
        
        # Output file
        out_frame = tk.Frame(self.encrypt_tab)
        out_frame.pack(fill="x", pady=5)
        tk.Label(out_frame, text="Output File:", width=15, anchor="w").pack(side="left")
        tk.Entry(out_frame, textvariable=self.encrypt_output_path, width=40, state="readonly").pack(side="left", padx=5)
        tk.Button(out_frame, text="Browse", command=self.browse_encrypt_output).pack(side="left")
        
        # Action button
        tk.Button(self.encrypt_tab, text="Encrypt", command=self.execute_encrypt, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
    
    def setup_decrypt_tab(self):
        # File selection
        file_frame = tk.Frame(self.decrypt_tab)
        file_frame.pack(fill="x", pady=5)
        tk.Label(file_frame, text="Input File:", width=15, anchor="w").pack(side="left")
        tk.Entry(file_frame, textvariable=self.decrypt_file_path, width=40, state="readonly").pack(side="left", padx=5)
        tk.Button(file_frame, text="Browse", command=self.browse_decrypt_file).pack(side="left")
        
        # Password
        pass_frame = tk.Frame(self.decrypt_tab)
        pass_frame.pack(fill="x", pady=5)
        tk.Label(pass_frame, text="Password:", width=15, anchor="w").pack(side="left")
        tk.Entry(pass_frame, textvariable=self.decrypt_password, width=40, show="*").pack(side="left", padx=5)
        
        # Use original filename checkbox
        check_frame = tk.Frame(self.decrypt_tab)
        check_frame.pack(fill="x", pady=5)
        tk.Checkbutton(check_frame, text="Use original filename from metadata", variable=self.use_original_name, command=self.toggle_output_selection).pack(anchor="w")
        
        # Output directory/file frame
        self.decrypt_out_frame = tk.Frame(self.decrypt_tab)
        self.decrypt_out_frame.pack(fill="x", pady=5)
        self.decrypt_out_label = tk.Label(self.decrypt_out_frame, text="Output Directory:", width=15, anchor="w")
        self.decrypt_out_label.pack(side="left")
        self.decrypt_output_entry = tk.Entry(self.decrypt_out_frame, textvariable=self.decrypt_output_dir, width=40, state="readonly")
        self.decrypt_output_entry.pack(side="left", padx=5)
        self.decrypt_output_button = tk.Button(self.decrypt_out_frame, text="Browse", command=self.browse_decrypt_output_dir)
        self.decrypt_output_button.pack(side="left")
        
        # Action button
        tk.Button(self.decrypt_tab, text="Decrypt", command=self.execute_decrypt, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
    
    def setup_about_tab(self):
        # About frame
        about_frame = tk.Frame(self.about_tab)
        about_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # About text
        tk.Label(about_frame, text=f"SafeBox v{VERSION}", font=("Helvetica", 14, "bold")).pack(anchor="w")
        tk.Label(about_frame, text="A powerful file encryption/decryption tool, that allows you to encrypt your files\nwith your own password in highly valuable(AES) Encryption with\nsome customization/Optimzations.\nIt's free and open-source, so enjoy it.").pack(anchor="w", pady=5)
        tk.Label(about_frame, text="Author: S4D0X").pack(anchor="w", pady=5)
        
        # GitHub link
        github_frame = tk.Frame(about_frame)
        github_frame.pack(fill="x", pady=2)
        tk.Label(github_frame, text="GitHub:", width=10, anchor="w").pack(side="left")
        github_link = tk.Label(github_frame, text="github.com/S4D0X", fg="blue", cursor="hand2")
        github_link.pack(side="left")
        github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/s4d0x-dev/safebox"))
        
        # Facebook link
        fb_frame = tk.Frame(about_frame)
        fb_frame.pack(fill="x", pady=2)
        tk.Label(fb_frame, text="Facebook:", width=10, anchor="w").pack(side="left")
        fb_link = tk.Label(fb_frame, text="facebook.com/S4D0X", fg="blue", cursor="hand2")
        fb_link.pack(side="left")
        fb_link.bind("<Button-1>", lambda e: webbrowser.open("https://facebook.com/fared.baktashabdaly.1"))
        
        # Email
        email_frame = tk.Frame(about_frame)
        email_frame.pack(fill="x", pady=2)
        tk.Label(email_frame, text="Email:", width=10, anchor="w").pack(side="left")
        email_entry = tk.Entry(email_frame, width=40, state="readonly")
        email_entry.insert(0, "faredba@outlook.com")
        email_entry.config(state="readonly")
        email_entry.pack(side="left")
    
    def browse_encrypt_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.encrypt_file_path.set(file)
            self.encrypt_output_path.set(file + ".ssb")
    
    def browse_encrypt_output(self):
        file = filedialog.asksaveasfilename(defaultextension=".ssb", filetypes=[("SafeBox files", "*.ssb"), ("All files", "*.*")])
        if file:
            self.encrypt_output_path.set(file)
    
    def browse_decrypt_file(self):
        file = filedialog.askopenfilename(filetypes=[("SafeBox files", "*.ssb"), ("All files", "*.*")])
        if file:
            self.decrypt_file_path.set(file)
            if self.use_original_name.get():
                try:
                    with open(file, "rb") as f_in:
                        full_data = f_in.read()
                    _, original_name = extract_metadata(full_data)
                    input_dir = os.path.dirname(file) or "."
                    self.decrypt_output_dir.set(input_dir)
                    self.decrypt_output_path.set(os.path.join(input_dir, original_name))
                except Exception as e:
                    self.decrypt_output_dir.set("")
                    self.decrypt_output_path.set("")
                    messagebox.showerror("Error", f"Could not extract original filename: {str(e)}")
            else:
                base, _ = os.path.splitext(file)
                self.decrypt_output_path.set(base)
                self.decrypt_output_dir.set("")
    
    def browse_decrypt_output_dir(self):
        if self.use_original_name.get():
            directory = filedialog.askdirectory()
            if directory:
                self.decrypt_output_dir.set(directory)
                if self.decrypt_file_path.get():
                    try:
                        with open(self.decrypt_file_path.get(), "rb") as f_in:
                            full_data = f_in.read()
                        _, original_name = extract_metadata(full_data)
                        self.decrypt_output_path.set(os.path.join(directory, original_name))
                    except Exception as e:
                        self.decrypt_output_path.set("")
                        messagebox.showerror("Error", f"Could not extract original filename: {str(e)}")
        else:
            file = filedialog.asksaveasfilename(filetypes=[("All files", "*.*")])
            if file:
                self.decrypt_output_path.set(file)
                self.decrypt_output_dir.set("")
    
    def toggle_output_selection(self):
        if self.use_original_name.get():
            self.decrypt_out_label.config(text="Output Directory:")
            self.decrypt_output_entry.config(textvariable=self.decrypt_output_dir, state="readonly")
            self.decrypt_output_button.config(command=self.browse_decrypt_output_dir)
            if self.decrypt_file_path.get():
                try:
                    with open(self.decrypt_file_path.get(), "rb") as f_in:
                        full_data = f_in.read()
                    _, original_name = extract_metadata(full_data)
                    input_dir = os.path.dirname(self.decrypt_file_path.get()) or "."
                    self.decrypt_output_dir.set(input_dir)
                    self.decrypt_output_path.set(os.path.join(input_dir, original_name))
                except Exception as e:
                    self.decrypt_output_dir.set("")
                    self.decrypt_output_path.set("")
                    messagebox.showerror("Error", f"Could not extract original filename: {str(e)}")
        else:
            self.decrypt_out_label.config(text="Output File:")
            self.decrypt_output_entry.config(textvariable=self.decrypt_output_path, state="readonly")
            self.decrypt_output_button.config(command=self.browse_decrypt_output_dir)
            if self.decrypt_file_path.get():
                base, _ = os.path.splitext(self.decrypt_file_path.get())
                self.decrypt_output_path.set(base)
                self.decrypt_output_dir.set("")
    
    def validate_encrypt_inputs(self):
        if not self.encrypt_file_path.get():
            messagebox.showerror("Error", "Please select an input file.")
            return False
        if not self.encrypt_password.get():
            messagebox.showerror("Error", "Please enter a password.")
            return False
        if not self.encrypt_output_path.get():
            messagebox.showerror("Error", "Please specify an output file.")
            return False
        if not os.path.exists(self.encrypt_file_path.get()):
            messagebox.showerror("Error", "Input file does not exist.")
            return False
        return True
    
    def validate_decrypt_inputs(self):
        if not self.decrypt_file_path.get():
            messagebox.showerror("Error", "Please select an input file.")
            return False
        if not self.decrypt_password.get():
            messagebox.showerror("Error", "Please enter a password.")
            return False
        if not self.use_original_name.get() and not self.decrypt_output_path.get():
            messagebox.showerror("Error", "Please specify an output file or select 'Use original filename'.")
            return False
        if not os.path.exists(self.decrypt_file_path.get()):
            messagebox.showerror("Error", "Input file does not exist.")
            return False
        return True
    
    def execute_encrypt(self):
        if not self.validate_encrypt_inputs():
            return
        
        self.status.config(text="Encrypting...", fg="blue")
        self.root.update()
        
        try:
            result = encryptor(self.encrypt_file_path.get(), self.encrypt_password.get(), self.encrypt_output_path.get())
            if isinstance(result, tuple):
                message, *err = result
                color = "red" if "[-]" in message else "green" if "[+]" in message else "blue"
                self.status.config(text=message, fg=color)
                if err and "[-]" in message:
                    messagebox.showerror("Error", str(err[0]))
            else:
                color = "red" if "[-]" in result else "green" if "[+]" in result else "blue"
                self.status.config(text=result, fg=color)
        except Exception as e:
            self.status.config(text="Error occurred", fg="red")
            messagebox.showerror("Error", str(e))
    
    def execute_decrypt(self):
        if not self.validate_decrypt_inputs():
            return
        
        self.status.config(text="Decrypting...", fg="blue")
        self.root.update()
        
        output_path = self.decrypt_output_path.get() if not self.use_original_name.get() else self.decrypt_output_path.get()
        
        try:
            result = decryptor(self.decrypt_file_path.get(), self.decrypt_password.get(), output_path)
            if isinstance(result, tuple):
                message, *err = result
                color = "red" if "[-]" in message else "green" if "[+]" in message else "blue"
                self.status.config(text=message, fg=color)
                if err and "[-]" in message:
                    messagebox.showerror("Error", str(err[0]))
            else:
                color = "red" if "[-]" in result else "green" if "[+]" in result else "blue"
                self.status.config(text=result, fg=color)
        except Exception as e:
            self.status.config(text="Error occurred", fg="red")
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SafeBoxGUI(root)
    root.mainloop()