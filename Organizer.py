from pathlib import Path
import shutil
from datetime import datetime
from plyer import notification
import time
import platform
import os

desktop_path = Path.home() / "Desktop"
downloads = Path.home() / "Downloads"
trash_path = Path.home() / "Trash"
days_to_move_to_trash = 60
days_to_notify_trash = 80
days_to_remove_trash = 100
wait_interval_seconds = 7200
notification_length = 5

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

def downloads_files_separation():
    for file_path in downloads.iterdir():
        if file_path.is_file():
            if not file_path.name.endswith('.lnk'):
                extension = file_path.suffix[1:]

                folder = downloads / extension
                folder.mkdir(exist_ok=True)

                destination = folder / file_path.name
                shutil.move(file_path, destination)


def trash_separation():
    trash_path.mkdir(exist_ok=True)
    current_datetime = datetime.now()

    for file_path in downloads.rglob('*'):
        file_stats = file_path.stat()

        modification_time = file_stats.st_mtime
        modification_time_dt = datetime.fromtimestamp(modification_time)
        time_difference = current_datetime - modification_time_dt

        if time_difference.days > days_to_move_to_trash:
            shutil.move(file_path, trash_path)

def trash_notification():
    current_datetime = datetime.now()
    count = 0

    for file_path in trash_path.rglob('*'):
        file_stats = file_path.stat()

        modification_time = file_stats.st_mtime
        modification_time_dt = datetime.fromtimestamp(modification_time)
        time_difference = current_datetime - modification_time_dt

        if time_difference.days > days_to_notify_trash:
            count += 1

    if count != 0:

        notification.notify(
            title="Trash files",
            message="Trash files have not been checked in for far too long. Count of these files: " + str(count),
            timeout=notification_length,
        )

        open_trash_folder()

def delete_trash():
    current_datetime = datetime.now()

    for file_path in trash_path.rglob('*'):
        file_stats = file_path.stat()

        modification_time = file_stats.st_mtime
        modification_time_dt = datetime.fromtimestamp(modification_time)
        time_difference = current_datetime - modification_time_dt

        if time_difference.days > days_to_remove_trash:
            file_path.unlink()

def open_trash_folder():

    if platform.system() == "Windows":
        os.system(f'explorer "{trash_path}"')
    elif platform.system() == "Darwin":
        os.system(f'open "{trash_path}"')
    elif platform.system() == "Linux":
        os.system(f'xdg-open "{trash_path}"')
    else:
        print("Sorry, this function is not supported on your operating system.")

def wait():
    time.sleep(wait_interval_seconds)


def main():
    while True:
        clean_desktop()
        downloads_files_separation()
        trash_separation()
        trash_notification()
        delete_trash()
        wait()

if __name__== "__main__":
    main()