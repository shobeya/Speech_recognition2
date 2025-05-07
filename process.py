import os

folder_path = r'C:\Users\rvmut\Downloads\archive (18)\UserLibri\audio_data\test-clean'

# Check if the path exists
if os.path.exists(folder_path):
    # List all the files and folders in the folder
    files = os.listdir(folder_path)
    
    # Loop through each folder in the test-clean directory
    for speaker_folder in files:
        speaker_folder_path = os.path.join(folder_path, speaker_folder)
        
        # Check if it's a folder (not a file)
        if os.path.isdir(speaker_folder_path):
            print(f"Processing files in {speaker_folder_path}")
            
            # List all the audio files in this speaker folder
            audio_files = os.listdir(speaker_folder_path)
            
            # Example: Loop through the audio files
            for audio_file in audio_files:
                audio_file_path = os.path.join(speaker_folder_path, audio_file)
                print(f"Found audio file: {audio_file_path}")
                # You can now perform operations on these audio files (e.g., load them, extract features, etc.)
        else:
            print(f"{speaker_folder_path} is not a valid folder.")
else:
    print(f"The folder path {folder_path} does not exist.")
