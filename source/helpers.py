import os

K_SWIFT_EXTENSION = '.swift'
READ_FILE_MODE = 'r'

initial_directory = "."

def get_all_files_in_directory_with(extension = '.swift'):
    all_files = []
    for root, dirs, files in os.walk(initial_directory):
        for name in files:
            if name.endswith(extension):
                path = f'{root}/{name}'
                with open(path, READ_FILE_MODE) as file:
                    all_files.append(file.read())
    return all_files

def execute_for_all_files_in_directory(execute, extension = K_SWIFT_EXTENSION):
    for root, dirs, files in os.walk(initial_directory):
        for name in files:
            if name.endswith(extension):
                path = f'{root}/{name}'
                print(path)
                with open(path, READ_FILE_MODE) as file:
                    execute(file.read())
