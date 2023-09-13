import os
import glob

# Define the directory to search
dir_path = r"C:\Users\Utente\AndroidStudioProjects\time_tracker - Copy\lib"

# Define the file extensions to include
extensions = ("*.py", "*.dart", "*.js", "*.html", "*.css")

# Initialize counters
total_lines = 0
file_count = 0

# Recursively search for files with specified extensions
for ext in extensions:
    for file_path in glob.glob(os.path.join(dir_path, "**", ext), recursive=True):
        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
                total_lines += len(lines)
                file_count += 1
               
        except (PermissionError, IOError):
            print('skipped')
            continue

# Print results
print(f"Total lines of code: {total_lines}")
print(f"Total number of files: {file_count}")