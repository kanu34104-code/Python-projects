9. #Password Generator
import random
import string

def generate_password(Length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    generate_password = ''.join(random.choice(all_characters) for _ in range(Length))
    return generate_password

print("Generated Password:", generate_password(16))
