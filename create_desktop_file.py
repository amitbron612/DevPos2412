import os

# Define the path to the temp directory
temp_dir = "C:\\Temp"

# Define the content of the text file
content = "My name is Amit"

# Define the path to the text file in the temp directory
file_path = os.path.join(temp_dir, "Amit.txt")

# Write the content to the text file
with open(file_path, "w") as file:
    file.write(content)

print("Text file created successfully in the C:\\Temp directory.")
