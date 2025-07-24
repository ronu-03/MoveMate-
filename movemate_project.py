import tkinter as tk
from tkinter import messagebox
import threading
import time
from playsound import playsound
import os

# Function to play sound in a separate thread
def play_alert_sound():
    sound_path = r"C:\Users\RONAK DR\Documents\MINI PROJECT 1\vehicle_beep.wav.wav"
    try:
        playsound(sound_path)
    except Exception as e:
        messagebox.showerror("Error", f"Sound failed: {e}")

# Function to simulate vehicle detection
def detect_vehicle():
    if not alert_state["active"]:
        alert_state["active"] = True
        status_label.config(text="🚗 Vehicle Detected!", fg="red")
        stop_button.config(state="normal")
        threading.Thread(target=play_alert_sound).start()
    else:
        messagebox.showinfo("Info", "Vehicle already detected!")

# Function to simulate turning off alert (IR remote)
def stop_alert():
    alert_state["active"] = False
    status_label.config(text="✅ No Vehicle Detected", fg="green")
    stop_button.config(state="disabled")

# GUI Setup
window = tk.Tk()
window.title("MoveMate – Smart Parking Sticker")
window.geometry("400x300")
window.config(bg="#f0f4f7")

alert_state = {"active": False}

title = tk.Label(window, text="🚘 MoveMate – Vehicle Detection", font=("Arial", 16, "bold"), bg="#f0f4f7")
title.pack(pady=10)

status_label = tk.Label(window, text="✅ No Vehicle Detected", font=("Arial", 14), fg="green", bg="#f0f4f7")
status_label.pack(pady=10)

detect_button = tk.Button(window, text="Simulate Vehicle Detection", font=("Arial", 12), bg="#007bff", fg="white", command=detect_vehicle)
detect_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Alert (IR Remote)", font=("Arial", 12), bg="#28a745", fg="white", command=stop_alert, state="disabled")
stop_button.pack(pady=10)

window.mainloop()
