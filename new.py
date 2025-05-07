import os
import glob

# Folder where files are stored
folder_path = r'C:/Users/rvmut/Downloads/archive (18)/UserLibri/lm_data/'

# Pattern to match all *_lm_train.txt files
file_pattern = os.path.join(folder_path, '*_lm_train.txt')
train_files = glob.glob(file_pattern)

# Process each file
for file_path in train_files:
    print(f"Processing file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Basic stats
        total_lines = len(lines)
        total_words = sum(len(line.strip().split()) for line in lines)
        unique_words = set(word for line in lines for word in line.strip().split())

        print(f"Total lines: {total_lines}")
        print(f"Total words: {total_words}")
        print(f"Unique words: {len(unique_words)}")
        print("-" * 40)

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
