import os


def read_all_excel_files(directory):
    all_paths = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xls') or file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                all_paths[file] = file_path
    return all_paths
