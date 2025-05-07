import os
import soundfile as sf

# Function to convert a single FLAC file to WAV
def convert_flac_to_wav(flac_path, wav_path=None):
    audio, sample_rate = sf.read(flac_path)
    if wav_path is None:
        wav_path = flac_path.replace(".flac", ".wav")
    sf.write(wav_path, audio, sample_rate)
    return wav_path

# Directory containing FLAC files
directory = "C:/Users/rvmut/Downloads/archive (18)/UserLibri/audio_data/test-clean/speaker-908-book-574"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".flac"):
        flac_file = os.path.join(directory, filename)
        wav_file = convert_flac_to_wav(flac_file)  # Converts to .wav
        print(f"Converted {flac_file} to {wav_file}")
    else:
        continue
