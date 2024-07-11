from cryptography.fernet import Fernet
from art import text2art

# Stwórz napis "CRYPTOR 1.0" za pomocą modułu art
text = text2art("CRYPTOR 1.0")

# ASCII art dla kłódki
lock = """
   .----.
  /      \\
 |--------|
 |        |
 |        |
 |   __   |
 |  [  ]  |
 |  ____  |
 '.__.__.-'
"""

# Wyświetl kłódkę obok napisu
print(lock)
print(text)

# Do szyfrowania
message = input("Hi! Type text to crypt: ")

# Klucz
key = Fernet.generate_key()
#print("Generated key:", key.decode())

fernet = Fernet(key)

# Szyfrowanie
encoded_message = fernet.encrypt(message.encode())

# Wyświetl Zakodowany Tekst
print("\nYour crypted message is: \n" + encoded_message.decode())


# Opinia
rate = int(input("\nType stars (max 5)) : "))

