from plyer import notification
import rotatescreen
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import time
from threading import Thread
import sys

class ModernScreenRotator:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Rotation Utility")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f2f5")
        
        # Variables
        self.rotation_count = tk.IntVar(value=1)
        self.is_running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Style configuration
        style = ttk.Style()
        style.configure('Title.TLabel', 
                       font=('Helvetica', 16, 'bold'), 
                       padding=10)
        style.configure('Info.TLabel', 
                       font=('Helvetica', 10), 
                       padding=5)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Screen Rotation Utility",
            style='Title.TLabel'
        )
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = ttk.LabelFrame(
            main_frame,
            text="Configuration",
            padding="10"
        )
        input_frame.pack(fill=tk.X, pady=10)
        
        # Rotation count input
        ttk.Label(
            input_frame,
            text="Number of rotations:",
            style='Info.TLabel'
        ).pack(anchor=tk.W)
        
        rotation_entry = ttk.Entry(
            input_frame,
            textvariable=self.rotation_count,
            width=10
        )
        rotation_entry.pack(pady=5)
        
        # Warning label
        warning_label = ttk.Label(
            main_frame,
            text="⚠️ Please use this utility responsibly",
            foreground="orange",
            style='Info.TLabel'
        )
        warning_label.pack(pady=10)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = ttk.Button(
            button_frame,
            text="Start Rotation",
            command=self.start_rotation,
            style='Accent.TButton',
            width=20
        )
        self.start_button.pack(pady=5)
        
        # Stop button
        self.stop_button = ttk.Button(
            button_frame,
            text="Stop",
            command=self.stop_rotation,
            style='Danger.TButton',
            width=20,
            state=tk.DISABLED
        )
        self.stop_button.pack(pady=5)
        
        # Exit button
        exit_button = ttk.Button(
            button_frame,
            text="Exit Application",
            command=self.root.destroy,
            width=20
        )
        exit_button.pack(pady=5)
        
    def show_notification(self):
        notification.notify(
            title="Screen Rotation Utility",
            message="Screen rotation sequence has started. Press Stop to cancel.",
            app_name="Screen Rotator",
            timeout=5
        )
        
    def rotate_screen_sequence(self):
        screen = rotatescreen.get_primary_display()
        count = self.rotation_count.get()
        
        try:
            for i in range(count):
                if not self.is_running:
                    break
                screen.rotate_to(i * 90 % 360)
                time.sleep(1)
        finally:
            screen.rotate_to(0)  # Reset to normal orientation
            self.is_running = False
            self.root.after(0, self.update_button_states)
    
    def start_rotation(self):
        if self.rotation_count.get() <= 0:
            tk.messagebox.showerror(
                "Invalid Input",
                "Please enter a positive number of rotations."
            )
            return
        
        self.is_running = True
        self.update_button_states()
        self.show_notification()
        
        # Start rotation in a separate thread
        Thread(target=self.rotate_screen_sequence, daemon=True).start()
    
    def stop_rotation(self):
        self.is_running = False
        
    def update_button_states(self):
        if self.is_running:
            self.start_button.configure(state=tk.DISABLED)
            self.stop_button.configure(state=tk.NORMAL)
        else:
            self.start_button.configure(state=tk.NORMAL)
            self.stop_button.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernScreenRotator(root)
    root.mainloop()