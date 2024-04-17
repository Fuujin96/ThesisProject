import hashlib


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
        print(f"The files are identical. Hash: {hash1}")
    else:
        print(f"The files are different. Hashes: {hash1}, {hash2}")


# Example usage:
compare_files('path/to/file1.txt', 'path/to/file2.txt')
