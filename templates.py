import os
from pathlib import Path

main_folder = "src"

paths = [
    f"{main_folder}/__init__.py",
    f"{main_folder}/helper.py",
    f"{main_folder}/llm_service.py",
    "requirements.txt",
    "setup.py",
    ".env",
    "main.py"
]

for path in paths:
    file_path = Path(path)
    folder = file_path.parent
    os.makedirs(folder,exist_ok=True)
    
    if not os.path.exists(file_path):
        file_path.touch(exist_ok=True)