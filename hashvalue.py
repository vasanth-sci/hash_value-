import hashlib

# Define the password
password = "kumar115"

# Create a SHA-256 hash of the password
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# Create an MD5 hash of the password
md5_hash = hashlib.md5(password.encode()).hexdigest()

print(sha256_hash, md5_hash)
