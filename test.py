from pathlib import Path
import shutil



base_dir = Path.cwd() / "C:/Users/Owner/Desktop/test_files"


FILE_CATEGORIES = {
    ".pdf": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".zip": "Archives",
}


def organize_files():

    for file_path in base_dir.iterdir():
        if file_path.is_file():

            ext = file_path.suffix.lower()


            if ext in FILE_CATEGORIES:
                folder_name = FILE_CATEGORIES[ext]
            else:
                folder_name = "other"

            target_dir = base_dir / folder_name


            target_dir.mkdir(exist_ok=True)


            print(f"Moving {file_path.name} to {folder_name}/")
            shutil.move(str(file_path), str(target_dir / file_path.name))


if __name__ == "__main__":
    organize_files()

















































































































































