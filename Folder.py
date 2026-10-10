import os
import shutil

# Enable ANSI colors on Windows terminals
os.system("")

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

path = input("Enter the folder path to organize: ").strip().strip('"')

if not os.path.isdir(path):
    raise SystemExit(f"{RED}Folder not found: {path}{RESET}")

# Files that should stay where they are
SKIP_FILES = {"desktop.ini"}

created_folders = []
moved = 0
renamed = 0
skipped = []
errors = []

print(f"\n{BOLD}{CYAN}Organizing: {path}{RESET}\n")

for file in os.listdir(path):
    source = os.path.join(path, file)

    # Skip folders (including ones this script creates) and system files
    if not os.path.isfile(source) or file.lower() in SKIP_FILES:
        skipped.append(file)
        print(f"{YELLOW}[SKIPPED] {file}{RESET}")
        continue

    filename, extension = os.path.splitext(file)
    extension = extension[1:].lower()

    # Files with no extension go into "no_extension"
    folder_name = extension if extension else "no_extension"
    target_folder = os.path.join(path, folder_name)

    if not os.path.exists(target_folder):
        try:
            os.makedirs(target_folder)
            created_folders.append(folder_name)
            print(f"{CYAN}[NEW FOLDER] {folder_name}/{RESET}")
        except OSError as e:
            errors.append((file, str(e)))
            print(f"{RED}[ERROR] Could not create folder '{folder_name}': {e}{RESET}")
            continue

    destination = os.path.join(target_folder, file)

    # Avoid overwriting if a file with the same name already exists
    was_renamed = False
    counter = 1
    while os.path.exists(destination):
        suffix = f".{extension}" if extension else ""
        destination = os.path.join(target_folder, f"{filename}_{counter}{suffix}")
        counter += 1
        was_renamed = True

    try:
        shutil.move(source, destination)
        moved += 1
        if was_renamed:
            renamed += 1
            print(f"{GREEN}[MOVED]{RESET} {file} -> {folder_name}/ {YELLOW}(renamed, duplicate){RESET}")
        else:
            print(f"{GREEN}[MOVED]{RESET} {file} -> {folder_name}/")
    except (PermissionError, shutil.Error, OSError) as e:
        errors.append((file, str(e)))
        print(f"{RED}[ERROR] {file}: {e}{RESET}")

# Summary
print(f"\n{BOLD}{CYAN}{'=' * 40}")
print("              SUMMARY")
print(f"{'=' * 40}{RESET}")
print(f"{CYAN}Folders created : {len(created_folders)}{RESET}", end="")
print(f"  ({', '.join(created_folders)})" if created_folders else "")
print(f"{GREEN}Files moved     : {moved}{RESET}")
print(f"{YELLOW}Renamed (dupes) : {renamed}{RESET}")
print(f"{YELLOW}Skipped         : {len(skipped)}{RESET}")
print(f"{RED}Errors          : {len(errors)}{RESET}")

if errors:
    print(f"\n{RED}{BOLD}Error details:{RESET}")
    for name, msg in errors:
        print(f"{RED}  - {name}: {msg}{RESET}")

print()
