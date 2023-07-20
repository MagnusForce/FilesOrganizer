# File Management Script

The File Management Script is a Python script that helps you organize your Desktop and Downloads folder by moving files to appropriate folders and managing the trash folder. It also provides notifications for files that have been in the trash folder for an extended period, giving you notifications and the option to delete them permanently.

# Installation

This program can be used as is by simply running the Python script.

Most modules used in this project are pre-installed with Python. The only module you need to install is `plyer` and datetime. To install these modules, run these commands in CMD:

`pip install plyer`

# Features

Clean Desktop: Moves files from the Desktop to the Downloads folder, organizing them in subfolders based on their file extensions. Directories on the Desktop are deleted.

Downloads Files Separation: Moves files from the Downloads folder to subfolders based on their file extensions.

Trash Separation: Moves old files from the Downloads folder to the Trash folder after a specified number of days.

Trash Notification: Sends a Desktop notification if there are files in the Trash folder that haven't been checked in for a prolonged period.

Delete Trash: Deletes files from the Trash folder that have been there for a specified number of days.

# Usage

Clone or download this repository to your local machine.

Script is intended to run on each computer startup (it still can be used manually). To achieve this you can follow these steps:
1. Create a shortcut to your Python script.
2. Open the Startup folder (Press Win + R to open the "Run" dialog box.Type "shell:startup" and click "OK.") 
3. Move the shortcut to the Startup folder.
4. Test your script by restarting your computer.

Note: The notifications are supported on Windows, macOS, and Linux. If your operating system is not supported, the script will inform you that the notification function is not available for your OS, but the rest of the script will still work as expected.

# Configuration

You can customize the behavior of the script by modifying the following variables at the beginning of the file_management_script.py file:

`days_to_move_to_trash`: The number of days after which files in the Downloads folder are moved to the Trash folder.

`days_to_notify_trash`: The number of days after which a notification is triggered for files in the Trash folder that haven't been checked in.

`days_to_remove_trash`: The number of days after which files in the Trash folder are permanently deleted.

`wait_interval_seconds`: The interval (in seconds) between script executions.

`notification_length`: The length of time (in seconds) that the notification will be displayed.