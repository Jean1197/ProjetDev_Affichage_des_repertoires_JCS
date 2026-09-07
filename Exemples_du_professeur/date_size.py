# affichage de date et taille

from pathlib import Path
from datetime import datetime

file = Path("show_file_directory.py")

file_info = file.stat()

print("Size:", file_info.st_size)

print("Modified:",datetime.fromtimestamp(file_info.st_mtime))
# print("Modified:",file_info.st_mtime) # temps brut