import filecmp
import os
import time


def compare_files(file1, file2):
    """Compare two files using filecmp."""
    if filecmp.cmp(file1, file2, shallow=False):
        print(f"The files '{file1}' and '{file2}' are identical.")


def compare_all_files_in_folder(folder_path):
    """Compare all files within a folder to each other, printing only when files are identical."""
    start_time = time.time()  # Start the timer
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f))]
    n = len(files)
    for i in range(n):
        for j in range(i + 1, n):
            compare_files(files[i], files[j])
    end_time = time.time()  # Stop the timer
    print(f"Time taken to compare all files: {end_time - start_time:.2f} seconds")


# Example usage:
folder_path = 'C:/Users/busek/OneDrive/Masaüstü/Test/'
compare_all_files_in_folder(folder_path)
