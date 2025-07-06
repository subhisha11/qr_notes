from cryptography.fernet import Fernet
from datetime import datetime
import os

# File to save the key and notes
KEY_FILE = "secret.key"
NOTES_FILE = "notes.txt"

# Generate encryption key if not present
def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)

# Load the encryption key
def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

# Encrypt a note
def encrypt_note(note, key):
    f = Fernet(key)
    return f.encrypt(note.encode())

# Decrypt a note
def decrypt_note(encrypted_note, key):
    f = Fernet(key)
    return f.decrypt(encrypted_note).decode()

# Write a new note
def write_note():
    note = input("📝 Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_note = f"[{timestamp}] {note}"
    key = load_key()
    encrypted = encrypt_note(full_note, key)

    with open(NOTES_FILE, 'ab') as f:
        f.write(encrypted + b"\n")
    print("✅ Note saved and encrypted!")

# Read all notes
def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("🚫 No notes found.")
        return

    key = load_key()
    print("\n🔓 Decrypted Notes:")
    with open(NOTES_FILE, 'rb') as f:
        for line in f:
            try:
                decrypted = decrypt_note(line.strip(), key)
                print(f"📌 {decrypted}")
            except Exception as e:
                print("⚠️ Skipped a corrupted note")

# Main menu
def main():
    generate_key()
    while True:
        print("\n🔐 Encrypted Notes CLI App")
        print("1. Write a note")
        print("2. Read all notes")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            write_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
