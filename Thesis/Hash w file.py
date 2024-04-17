import hashlib
import os
import time


def hash_file(filename):
    """Generate SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def compare_files(file1, file2):
    """Compare two files by their SHA-256 hashes."""
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        print(f"The files '{file1}' and '{file2}' are identical. Hash: {hash1}")


def compare_all_files_in_folder(folder_path):
    """Compare all files within a folder to each other, printing only when files are identical."""
    start_time = time.time()  # Start timing
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f))]
    n = len(files)
    for i in range(n):
        for j in range(i + 1, n):
            compare_files(files[i], files[j])
    end_time = time.time()  # End timing
    print(f"Time taken to compare all files: {end_time - start_time:.2f} seconds")


# Example usage:
folder_path = 'C:/Users/busek/OneDrive/Masaüstü/Test/'
compare_all_files_in_folder(folder_path)
