from pathlib import Path
import shutil

desktop_path = Path.home() / "Desktop"
downloads = Path.home() / "Downloads"


def clean_desktop():
    for item in desktop_path.iterdir():
        if item.is_dir():
            for file_path in item.iterdir():
                if file_path.is_file():
                    destination = downloads / file_path.name
                    shutil.move(file_path, destination)

            shutil.rmtree(item)

        elif item.is_file():

            if not item.name.endswith('.lnk'):
                destination = downloads / item.name
                shutil.move(item, destination)

def create_folders_for_files():
    for file_path in downloads.iterdir():
        if file_path.is_file():
            if not file_path.name.endswith('.lnk'):
                extension = file_path.suffix[1:]

                folder = downloads / extension
                folder.mkdir(exist_ok=True)

                destination = folder / file_path.name
                shutil.move(file_path, destination)

def main():
    clean_desktop()
    create_folders_for_files()

if __name__== "__main__":
    main()