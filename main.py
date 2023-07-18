from pathlib import Path
import shutil

desktop_path = Path.home() / "Desktop"
downloads = Path.home() / "Downloads"


def clean_desktop():
    for item in desktop_path.iterdir():
        if item.is_dir():
            # Move files from subfolder to Downloads directory
            for file_path in item.iterdir():
                if file_path.is_file():
                    destination = downloads / file_path.name
                    shutil.move(file_path, destination)

            # Delete the subfolder and its contents recursively
            shutil.rmtree(item)

        elif item.is_file():
            # Move files directly from the desktop to Downloads directory
            if not item.name.endswith('.lnk'):
                destination = downloads / item.name
                shutil.move(item, destination)


    # for file_path in downloads.rglob('*'):
    #     shutil.move(file_path, downloads)


def create_folders_for_files():
    for file_path in downloads.iterdir():
        if file_path.is_file():
            if not file_path.name.endswith('.lnk'):
                # Get the file extension (excluding the dot)
                extension = file_path.suffix[1:]

                # Create a folder with the extension name if it doesn't exist
                folder = downloads / extension
                folder.mkdir(exist_ok=True)

                # Move the file to the corresponding folder
                destination = folder / file_path.name
                shutil.move(file_path, destination)



def main():
    clean_desktop()
    create_folders_for_files()

if __name__== "__main__":
    main()