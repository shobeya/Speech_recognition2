import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import soundfile as sf
from transformers import pipeline

# Load the transcription model
asr_pipeline = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

def check_audio_file(audio_file):
    try:
        audio, sample_rate = sf.read(audio_file)
        print(f"Audio File: {audio_file}")
        print(f"Audio Shape: {audio.shape}, Sample Rate: {sample_rate}")
        if len(audio) == 0:
            print("Warning: The audio file is empty!")
        elif len(audio) < 1000:
            print("Warning: The audio file is too short!")
        else:
            print("Audio loaded successfully!")
        return audio_file  # Returning path for model
    except Exception as e:
        print(f"Error loading audio: {e}")
        return None

def transcribe_audio(filepath):
    try:
        result = asr_pipeline(filepath)
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return "Error during transcription"

def browse_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("WAV files", "*.wav"), ("FLAC files", "*.flac")]
    )
    if filepath:
        audio_path_var.set(filepath)

def perform_transcription():
    filepath = audio_path_var.get()
    if not os.path.exists(filepath):
        messagebox.showerror("Error", "Audio file not found!")
        return

    checked_file = check_audio_file(filepath)
    if checked_file:
        transcription = transcribe_audio(filepath)
        transcription_text.delete("1.0", tk.END)
        transcription_text.insert(tk.END, transcription)
    else:
        transcription_text.delete("1.0", tk.END)
        transcription_text.insert(tk.END, "Failed to load audio.")

# UI setup
root = tk.Tk()
root.title("Speech-to-Text Transcription UI")
root.geometry("700x400")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Audio file selection
audio_path_var = tk.StringVar()
file_entry = ttk.Entry(main_frame, textvariable=audio_path_var, width=60)
file_entry.grid(row=0, column=0, padx=5, pady=10, sticky="w")
browse_button = ttk.Button(main_frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=5, pady=10)

# Transcribe button
transcribe_button = ttk.Button(main_frame, text="Transcribe", command=perform_transcription)
transcribe_button.grid(row=1, column=0, columnspan=2, pady=10)

# Output text box
transcription_text = tk.Text(main_frame, height=15, wrap=tk.WORD)
transcription_text.grid(row=2, column=0, columnspan=2, sticky="nsew")

main_frame.rowconfigure(2, weight=1)
main_frame.columnconfigure(0, weight=1)

root.mainloop()
