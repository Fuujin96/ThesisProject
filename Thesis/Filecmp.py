import filecmp


def compare_files(file1, file2):
    """Compare two files using filecmp."""
    if filecmp.cmp(file1, file2, shallow=False):
        print("The files are identical.")
    else:
        print("The files are different.")


# Example usage:
compare_files('path/to/file1.txt', 'path/to/file2.txt')
