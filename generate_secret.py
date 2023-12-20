import secrets

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join(secrets.choice(chars) for _ in range(50))
print(SECRET_KEY)