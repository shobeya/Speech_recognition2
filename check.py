# Specify the file path
file_path = 'C:/Users/rvmut/Downloads/archive (18)/UserLibri/lm_data/test_data.txt'

# Read the text file into a list
with open(file_path, 'r') as file:
    lines = file.readlines()

# Convert the list to a DataFrame (each line becomes a row)
test_data_df = pd.DataFrame(lines, columns=["text"])

# Display the first few rows of the DataFrame
print(test_data_df.head())
