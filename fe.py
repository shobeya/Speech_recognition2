import os
import librosa
import numpy as np

folder_path = r'C:\Users\rvmut\Downloads\archive (18)\UserLibri\audio_data\test-clean'

# Function to extract MFCC from an audio file
def extract_mfcc(audio_path):
    try:
        # Load the audio file
        y, sr = librosa.load(audio_path, sr=None)
        
        # Extract MFCC features
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)  # 13 MFCC features
        
        # Transpose the MFCC to get one feature vector per frame
        mfcc = np.mean(mfcc, axis=1)  # Averaging over time (frames)
        
        return mfcc
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        return None

# Loop through the subfolders and extract MFCC features from each audio file
if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    
    for speaker_folder in files:
        speaker_folder_path = os.path.join(folder_path, speaker_folder)
        
        if os.path.isdir(speaker_folder_path):
            print(f"Processing folder: {speaker_folder_path}")
            
            audio_files = os.listdir(speaker_folder_path)
            
            for audio_file in audio_files:
                audio_file_path = os.path.join(speaker_folder_path, audio_file)
                
                # Check if the file is an audio file (based on file extension)
                if audio_file.endswith('.flac'):  # Adjust file extension as needed
                    mfcc = extract_mfcc(audio_file_path)
                    
                    if mfcc is not None:
                        print(f"MFCC extracted for {audio_file}: {mfcc}")
                    else:
                        print(f"Failed to extract MFCC for {audio_file}")
