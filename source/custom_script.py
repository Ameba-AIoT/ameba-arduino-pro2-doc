import os
import shutil

board_list = []
common_list = []
temp_only_list = [1000, 1000]

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    except OSError as error:
        print(f"Creation of the directory '{folder_name}' failed: {error}")

def get_folder_paths(folder_path, mode):
    folder_paths = []
    if mode == 0:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                folder_paths.append(item_path)
    elif mode == 1:
        for item in os.listdir(folder_path):
            if os.path.isdir(os.path.join(folder_path, item)) and not item.startswith("_"):
                folder_paths.append(item)
    return folder_paths

def copy_folder_bak(src_folder, target_folder):
    """
    Copy a folder and its contents to a target location.

    Args:
        src_folder (str): Path to the source folder.
        target_folder (str): Path to the target folder.

    Returns:
        None
    """
    # Check if source folder exists
    if not os.path.exists(src_folder):
        raise FileNotFoundError(f"Source folder '{src_folder}' not found.")

    # Check if target folder exists, create it if not
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Copy folder and its contents
    target_path = os.path.join(target_folder, os.path.basename(src_folder))
    shutil.copytree(src_folder, target_path)
    print(f"Copied folder: {src_folder} -> {target_path}")

def copy_folder(src_folder, target_folder):
    """
    Copy the contents of a folder into an existing target folder.

    Args:
        src_folder (str): Path to the source folder.
        target_folder (str): Path to the target folder.

    Returns:
        None
    """
    # Check if source folder exists
    if not os.path.exists(src_folder):
        raise FileNotFoundError(f"Source folder '{src_folder}' not found.")

    # Check if target folder exists, create it if not
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Iterate over all items in the source folder
    for item in os.listdir(src_folder):
        src_item = os.path.join(src_folder, item)
        target_item = os.path.join(target_folder, item)

        # If it's a directory, copy it recursively
        if os.path.isdir(src_item):
            if os.path.exists(target_item):
                # If the target subdirectory already exists, merge contents
                shutil.copytree(src_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copytree(src_item, target_item)
        # If it's a file, copy it directly
        else:
            shutil.copy2(src_item, target_item)

def search_files(file_path, search_term):
    """
    Searches for a specific term at the beginning of each line in a file.

    Args:
        file_path (str): The path to the file to search.
        search_term (str): The term to search for at the beginning of each line.

    Returns:
        int: The line number where the search term is found, or None if not found.
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for num, line in enumerate(file, 1):
                if line.lstrip().startswith(search_term):
                    return num
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except UnicodeDecodeError:
        print(f"Error reading file: {file_path}")
        return 0

    return 0

def remove_lines(file_path, search_string):
    """
    Removes lines containing the specified search string from a file.

    Args:
        file_path (str): Path to the file to modify.
        search_string (str): String to search for in each line.

    Returns:
        None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if search_string not in line:
                file.write(line)

def remove_lines_by_number(file_path, start_line, end_line):
    """
    Removes all lines between the specified start and end line numbers, inclusive.

    Args:
        file_path (str): Path to the file to modify.
        start_line (int): Starting line number (1-indexed).
        end_line (int): Ending line number (1-indexed).

    Returns:
        None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for i, line in enumerate(lines, start=1):
            if i < start_line or i > end_line:
                file.write(line)

def remove_consecutive_empty_lines(file_path):
    """
    Removes consecutive empty lines from a file, replacing them with a single empty line.

    Args:
        file_path (str): Path to the file to modify.

    Returns:
        None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        empty_lines = 0
        for line in lines:
            if line.strip() == '':
                empty_lines += 1
                if empty_lines >= 2:
                    continue
            else:
                empty_lines = 0
            file.write(line)

if __name__ == "__main__":
    # Change the current working directory
    new_directory = './source'
    os.chdir(new_directory)
    # Print the new current working directory
    ###print(os.getcwd())

    ###for item in board_list:
    ###    create_folder(item)

    board_list = get_folder_paths('./', 1)
    common_list = get_folder_paths('./_common', 0)

    ###for i, item in enumerate(common_list):
    ###    current_path = os.getcwd()
    ###    new_path = os.path.join(current_path, item)
    ###    common_list[i] = new_path

#    for board in board_list:
#        for item in common_list:
#            print(item)
#            print(board)
#            copy_folder(item, board)

    for board in board_list:
        copy_folder('./_common', board)

    for board in board_list:
        for root, dirs, files in os.walk(board):
            for file in files:
                if file.endswith('.rst'):
                    file_path = os.path.join(root, file)
                    remove_lines(file_path, '.. only:: ' + board)
                    remove_lines(file_path, '.. only:: end ' + board)
                    while temp_only_list[0] != 0:
                        temp_only_list[0] = search_files(file_path, '.. only:: ')
                        temp_only_list[1] = search_files(file_path, '.. only:: end')
                        if temp_only_list[0] != 0:
                            print(temp_only_list)
                            remove_lines_by_number(file_path, temp_only_list[0], temp_only_list[1])
                    temp_only_list[0] = 1000
                    temp_only_list[1] = 1000
                    remove_consecutive_empty_lines(file_path)

    # Remove the folder '/path/to/folder' and all its contents
    ###for item in common_list:
    ###    shutil.rmtree(item)
    shutil.rmtree('_common')

    new_directory = './../'
    os.chdir(new_directory)
    # Print the new current working directory
    ###print(os.getcwd())
