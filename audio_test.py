import soundfile as sf

# Function to check audio file
def check_audio_file(audio_file):
    try:
        # Read the audio file
        audio, sample_rate = sf.read(audio_file)
        
        # Print audio properties to check if it's being loaded correctly
        print(f"Audio File: {audio_file}")
        print(f"Audio Shape: {audio.shape}, Sample Rate: {sample_rate}")
        
        # If audio is too short or empty, notify user
        if len(audio) == 0:
            print("Warning: The audio file is empty!")
        elif len(audio) < 1000:
            print("Warning: The audio file is too short!")
        else:
            print("Audio loaded successfully!")

        return audio, sample_rate
    except Exception as e:
        print(f"Error loading audio: {e}")
        return None, None

# Path to the audio file you want to check
audio_file = "C:/Users/rvmut/Downloads/archive (18)/UserLibri/audio_data/test-clean/speaker-908-book-574/908-157963-0001.wav"

# Check the audio file
audio_data, sample_rate = check_audio_file(audio_file)
