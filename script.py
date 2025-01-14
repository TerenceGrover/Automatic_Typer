import tkinter as tk
from tkinter import ttk
import time
import keyboard
import random

def simulate_typing(text, speed, pause_duration, rewrite_probability):
    """
    Simulate typing the given text with human-like errors and random rewrites.
    """
    time.sleep(5)  # Small timeout before typing begins
    
    for i, char in enumerate(text):
        keyboard.write(char)  # Type the current character using the native layout
        time.sleep(random.uniform(0.8 / speed, 1.2 / speed))  # Add slight randomness to typing speed

        # Randomly decide to "rewrite" (delete and retype a few characters)
        if random.random() < rewrite_probability:
            backspaces = random.randint(1, min(3, i + 1))  # Limit backspaces to available characters
            for _ in range(backspaces):
                keyboard.press_and_release('backspace')
                time.sleep(0.05)  # Slight delay for realism
            keyboard.write(text[i - backspaces + 1:i + 1])  # Retype what was deleted

    # Pause after typing
    time.sleep(pause_duration)

def start_typing():
    text = code_text.get("1.0", tk.END).rstrip('\n')  # Retrieve text, strip trailing newline
    speed_value = speed_scale.get()
    pause_value = pause_scale.get()
    rewrite_probability = rewrite_scale.get() / 100  # Convert percentage to a probability
    
    simulate_typing(text, speed_value, pause_value, rewrite_probability)

# Set up the UI
root = tk.Tk()
root.title("Automatic typer")

# Frame for text input
text_frame = ttk.Frame(root, padding="10 10 10 10")
text_frame.grid(row=0, column=0, sticky="nsew")

# Label and text box
ttk.Label(text_frame, text="Enter your code here:").grid(row=0, column=0, sticky="w")
code_text = tk.Text(text_frame, width=50, height=10)
code_text.grid(row=1, column=0, pady=5)

# Frame for controls
control_frame = ttk.Frame(root, padding="10 10 10 10")
control_frame.grid(row=1, column=0, sticky="ew")

# Speed slider
speed_label = ttk.Label(control_frame, text="Typing Speed:")
speed_label.grid(row=0, column=0, sticky="w")
speed_scale = tk.Scale(control_frame, from_=1, to=20, orient="horizontal")
speed_scale.set(10)
speed_scale.grid(row=0, column=1, padx=5)

# Pause slider
pause_label = ttk.Label(control_frame, text="Pause Duration (secs):")
pause_label.grid(row=1, column=0, sticky="w")
pause_scale = tk.Scale(control_frame, from_=0, to=5, resolution=0.5, orient="horizontal")
pause_scale.set(2)
pause_scale.grid(row=1, column=1, padx=5)

# Rewrite probability slider
rewrite_label = ttk.Label(control_frame, text="Rewrite Probability (%):")
rewrite_label.grid(row=2, column=0, sticky="w")
rewrite_scale = tk.Scale(control_frame, from_=0, to=100, orient="horizontal")
rewrite_scale.set(10)
rewrite_scale.grid(row=2, column=1, padx=5)

# Button to start typing
start_button = ttk.Button(control_frame, text="Start Typing", command=start_typing)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
