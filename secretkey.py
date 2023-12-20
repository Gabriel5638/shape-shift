import secrets
import string

def generate_secret_key(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(chars) for _ in range(length))
    return secret_key

# Generate a new secret key with 16 characters
new_secret_key = generate_secret_key(16)
print(new_secret_key)