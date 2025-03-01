from pathlib import Path
import os


def find_path(name: Path) -> Path:
    name = Path(name)
    path = Path(os.getcwd())
    while True:
        # Check if the file exists in the current directory
        if (path / name).exists():
            return path / name
        else:
            # If the file is not found by the time the root directory is reached, raise an exception
            if path.parent == path:
                raise FileNotFoundError(f"File {name} not found in directory tree")
            else:
                # Move up to the parent directory
                path = path.parent
