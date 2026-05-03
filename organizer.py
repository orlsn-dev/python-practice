from pathlib import Path

downloads = Path.home() / "Downloads"

for item in downloads.iterdir():
    print(item.name)

    from pathlib import Path

downloads = Path.home() / "Downloads"

for item in downloads.iterdir():
    if item.is_file():
        print(f"{item.name} → extension: {item.suffix}")

        from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".pages"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".numbers"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}

def get_category(extension):
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"

downloads = Path.home() / "Downloads"

for item in downloads.iterdir():
    if item.is_file():
        category = get_category(item.suffix)
        print(f"{item.name} → {category}")

        from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".pages"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".numbers"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
}

def get_category(extension):
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Other"

def organize(folder, dry_run=True):
    folder = Path(folder)
    moves = 0
    
    for item in folder.iterdir():
        if not item.is_file():
            continue
        
        category = get_category(item.suffix)
        destination_folder = folder / category
        destination = destination_folder / item.name
        
        if dry_run:
            print(f"[DRY RUN] Would move: {item.name} → {category}/")
        else:
            destination_folder.mkdir(exist_ok=True)
            item.rename(destination)
            print(f"Moved: {item.name} → {category}/")
        
        moves += 1
    
    print(f"\nTotal: {moves} files {'would be' if dry_run else 'were'} organized.")

downloads = Path.home() / "Downloads"
organize(downloads, dry_run=Falsee)
