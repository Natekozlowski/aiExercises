from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.iterdir()
print(list(file_paths))