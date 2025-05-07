import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Assuming you have the transcribe_audio function and the evaluation functions already defined
# import your transcription function
# from transcription_module import transcribe_audio

def transcribe_audio(file_path):
    """
    A dummy transcription function. Replace this with your actual transcription logic.
    For example, it can be a function that uses a pre-trained model to transcribe the audio file.
    """
    # For demonstration purposes, let's just simulate transcription and WER/CER metrics
    # In practice, replace this with the actual transcription logic
    transcription = "Hello world"
    wer = 0.25
    cer = 0.10
    return transcription, wer, cer


def browse_file():
    """
    Opens a file dialog to choose an audio file and displays the path in the UI.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
    if file_path:
        print("Selected file:", file_path)  # Debugging print statement
        file_path_label.config(text="Selected file: " + file_path)
        transcribe_button.config(state="normal", command=lambda: transcribe_file(file_path))
    else:
        print("No file selected.")


def transcribe_file(file_path):
    """
    Transcribes the audio file and displays the transcription and WER/CER in the UI.
    """
    try:
        # Call your transcription function (this is a dummy function for now)
        transcription, wer, cer = transcribe_audio(file_path)
        
        # Display transcription and error metrics
        transcription_text.delete(1.0, tk.END)
        transcription_text.insert(tk.END, transcription)
        
        # Display WER and CER
        wer_label.config(text=f"Word Error Rate (WER): {wer:.4f}")
        cer_label.config(text=f"Character Error Rate (CER): {cer:.4f}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# UI Setup using Tkinter
root = tk.Tk()
root.title("Speech-to-Text Transcription")

# Create a frame for the file selection
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Label to show the file path
file_path_label = tk.Label(frame, text="No file selected", width=50, anchor="w")
file_path_label.grid(row=0, column=0, padx=5, pady=5)

# Button to browse and select a file
browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=5, pady=5)

# Button to start transcription (initially disabled)
transcribe_button = tk.Button(root, text="Transcribe", state="disabled", width=20)
transcribe_button.pack(pady=10)

# Textbox to display the transcription result
transcription_text = tk.Text(root, height=6, width=50)
transcription_text.pack(padx=10, pady=10)

# Labels to display WER and CER
wer_label = tk.Label(root, text="Word Error Rate (WER): -", width=50, anchor="w")
wer_label.pack(padx=10, pady=5)

cer_label = tk.Label(root, text="Character Error Rate (CER): -", width=50, anchor="w")
cer_label.pack(padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
