import os
from collections import Counter
import re

def clean_text(text):
    """Clean and normalize text."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def process_file(file_path):
    """Read and analyze a single lm_train.txt file."""
    print(f"Processing file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = [clean_text(line.strip()) for line in lines if line.strip()]
    words = [word for line in cleaned_lines for word in line.split()]
    
    total_lines = len(cleaned_lines)
    total_words = len(words)
    unique_words = len(set(words))

    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print("-" * 40)

    return total_lines, total_words, unique_words, Counter(words)

def process_all_files(data_dir):
    """Process all *_lm_train.txt files in the specified directory."""
    global_counter = Counter()
    for file_name in os.listdir(data_dir):
        if file_name.endswith("_lm_train.txt"):
            file_path = os.path.join(data_dir, file_name)
            _, _, _, word_counter = process_file(file_path)
            global_counter.update(word_counter)

    print("Top 10 most common words across all files:")
    for word, freq in global_counter.most_common(10):
        print(f"{word}: {freq}")

# Set your path to the dataset
data_directory = r"C:\Users\rvmut\Downloads\archive (18)\UserLibri\lm_data"
process_all_files(data_directory)
