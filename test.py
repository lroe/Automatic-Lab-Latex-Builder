import os

def find_replace_in_files(directory, old_substring, new_substring):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            updated_content = content.replace(old_substring, new_substring)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))  # Set the directory to the same as the Python program
    old_substring = " "
    new_substring = " "

    find_replace_in_files(directory, old_substring, new_substring)
    print(f"Substring '{old_substring}' replaced with '{new_substring}' successfully in all files.")
