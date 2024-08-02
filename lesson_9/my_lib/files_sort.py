import re
import os


def files_sort_json(list_dir) -> str:
    """Function gets list with info about directories.
    Creates new dir and moves all .json files in
    Returns info about total number of files moved and their total size
    """
    expr = r"([a-z0-9_]+)\.(json)"
    list_json = list(filter(lambda item: re.fullmatch(expr, item), list_dir))
    count = 0
    for files in list_json:
        if os.path.exists(os.path.join("json_files")):
            os.replace(files, os.path.join("json_files", files))
        else:
            os.mkdir("json_files")
            os.replace(files, os.path.join("json_files", files))
        count += 1
    return files_count("json_files", count) if list_json else "json files not found"


def files_sort_txt(list_dir: list) -> str:
    """Function gets list with info about directories.
    Creates new dir and moves all .txt files in
    Returns info about total number of files moved and their total size
    """
    expr = r"([a-z0-9_]+)\.(txt)"
    list_txt = list(filter(lambda item: re.fullmatch(expr, item), list_dir))
    count = 0
    for files in list_txt:
        if os.path.exists(os.path.join(os.getcwd(), "txt_files")):
            os.replace(files, os.path.join("txt_files", files))
        else:
            os.mkdir("txt_files")
            os.replace(files, os.path.join("txt_files", files))
        count += 1
    return files_count("txt_files", count) if list_txt else "txt files not found"


def files_count(dir_name: str, count: int) -> str:
    """Function gets a dir, counts  the total number of files
    and total size is there
    """
    list_files = os.listdir(os.path.join(os.getcwd(), dir_name))
    files_size = 0
    for item in list_files:
        files_size += os.stat(os.path.join(os.getcwd(), dir_name, item))[6]
    return f"{count} files of {files_size} bytes in size were moved to {dir_name}"


def files_rename(old_name: str, new_name: str) -> str:
    """Finds the file old_name  renames it
    returns info about the changes"""
    file_found = False
    for dirpath, dirnames, filenames in os.walk("."):
        for item in dirnames:
            if os.path.exists(os.path.join(item, old_name)):
                file_found = True
                os.rename(
                    os.path.join(item, old_name),
                    os.path.join(item, new_name),
                )
    return (
        f"File {old_name} has been renamed {new_name}"
        if file_found
        else f"{old_name} file not found"
    )
