import os

def list_files_in_folders(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, 'please enter valid folder'
    except PermissionError:
        return None, 'permission denied'

def main():
    folder_paths = input('Pls enter folder name separated by commas : ').split(',')
    for folder_path in folder_paths:
        files, error_msg = list_files_in_folders(folder_path)
        if(files):
            print("-> files in folders:")
            for file in files:
                print(file)
        else:
            print('Error for {folder_path}: {error_mesg}')

if __name__ == "__main__":
    main()