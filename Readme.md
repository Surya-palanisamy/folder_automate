# File Organizer

A simple Python script that sorts the files in any folder into subfolders based on their file extension. For example, `.pdf` files go into a `pdf` folder, `.jpg` files into a `jpg` folder, and so on.

## Features

- Asks you for the folder path when you run it
- Creates a subfolder for each file extension (lowercase, so `.JPG` and `.jpg` go together)
- Files with no extension go into a `no_extension` folder
- Handles duplicate names by adding a number (e.g. `report_1.pdf`) instead of overwriting
- Skips existing folders and system files like `desktop.ini`
- Skips files that can't be moved (locked or in use) without stopping
- Colored output and a summary at the end

## Requirements

- Python 3.6 or newer
- No extra packages needed (uses only `os` and `shutil`)

## Usage

1. Save the script as `organize_desktop.py`.
2. Open a terminal (Windows Terminal or PowerShell is recommended for colors).
3. Run:

   ```
   python organize_desktop.py
   ```

4. When prompted, enter the folder path, for example:

   ```
   Enter the folder path to organize: C:\Users\surya\OneDrive\Desktop
   ```

   Quotes around the path are fine, so you can paste a path copied from File Explorer.

## Output Colors

| Color  | Meaning                                         |
|--------|-------------------------------------------------|
| Green  | File moved                                      |
| Cyan   | New folder created                              |
| Yellow | Skipped, or renamed because of a duplicate name |
| Red    | Error                                           |

## Example Output

```
Organizing: C:\Users\surya\OneDrive\Desktop

[NEW FOLDER] pdf/
[MOVED] resume.pdf -> pdf/
[NEW FOLDER] jpg/
[MOVED] photo.jpg -> jpg/
[SKIPPED] Projects
[MOVED] notes.txt -> txt/

========================================
              SUMMARY
========================================
Folders created : 3  (pdf, jpg, txt)
Files moved     : 3
Renamed (dupes) : 0
Skipped         : 1
Errors          : 0
```

## Notes

- The script moves your files, so try it on a copy of a folder first if you want to be safe.
- It only organizes files directly inside the folder you choose, not files inside existing subfolders.
- To undo, move the files back out of the extension folders manually.
