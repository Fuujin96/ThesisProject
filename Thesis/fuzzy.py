import ssdeep


def fuzzy_hash_file(filename):
    """Generate a fuzzy hash of a file using ssdeep."""
    with open(filename, 'rb') as f:
        data = f.read()
    return ssdeep.hash(data)


def compare_files(file1, file2):
    """Compare two files using fuzzy hashing."""
    hash1 = fuzzy_hash_file(file1)
    hash2 = fuzzy_hash_file(file2)
    similarity = ssdeep.compare(hash1, hash2)
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print(f"Similarity score: {similarity}%")


# Example usage:
compare_files('path/to/file1.txt', 'path/to/file2.txt')
