def caesar_encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(message, key):
    return caesar_encrypt(message, -key)

if __name__ == "__main__":
    print("Caesar Cipher Program")
    choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter choice (1/2): ")

    message = input("Enter your message: ")
    try:
        key = int(input("Enter the key (number): "))
    except ValueError:
        print("Invalid key. Please enter a number.")
        exit(1)

    if choice == '1':
        encrypted = caesar_encrypt(message, key)
        print("Encrypted message:", encrypted)
    elif choice == '2':
        decrypted = caesar_decrypt(message, key)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice.")