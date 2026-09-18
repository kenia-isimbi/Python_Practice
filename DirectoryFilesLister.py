from pathlib import Path

directory_path = Path('.')

files = [item.name for item in directory_path.iterdir() if item.is_file()]

print("Files in directory:")
for file in files:
    print(file)
