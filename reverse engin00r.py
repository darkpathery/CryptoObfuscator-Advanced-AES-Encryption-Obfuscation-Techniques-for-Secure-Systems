import random
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
import struct
import ctypes

# AES Encryption and Decryption Helper Functions
def encrypt(data, key):
    # Generate a random IV for each encryption
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(iv + ct_bytes).decode()

def decrypt(data, key):
    raw = base64.b64decode(data)
    iv, ct = raw[:AES.block_size], raw[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# Stronger Key Derivation Function using PBKDF2 (better than simple key)
def derive_key(secret, salt):
    return hashlib.pbkdf2_hmac('sha256', secret.encode(), salt, 100000, dklen=32)

# Anti-Debugging: Check for common debugger techniques
def anti_debugging():
    if ctypes.windll.kernel32.IsDebuggerPresent():
        print("Debugger detected!")
        exit(1)

# Custom Encryption Method (mixing logic)
def custom_encrypt(data, key):
    encrypted_data = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return encrypted_data

# Function for Collatz Conjecture calculation
def காலச்சுழற்சி(n):
    படிகள் = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        படிகள் += 1
    return படிகள்

# Function to simulate random number generation based on typing speed
def தட்டச்சு_வகை_அடிப்படையிலான_சீருடா(prev_time, current_time):
    typing_speed = current_time - prev_time
    random_number = random.randint(1, 100) + typing_speed
    return random_number

# Function to generate a randomized character set (obfuscation)
def generate_randomized_mapping(key):
    random.seed(key)
    tamil_mapping = ['அஹ', 'பீ', 'சீ', 'டே', 'எ', 'ஃப', 'கீ', 'ஹ', 'இ', 'ஜ', 'க', 'எல்', 'எம்', 'என்', 'ஒ', 'பி', 'க்யூ', 'ஆர்', 'எஸ்', 'டி', 'யு', 'வீ', 'டபிள்யூ', 'எக்ஸ்', 'வாய்', 'ஜெட்']
    sinhala_mapping = ['අ', 'බ', 'ච', 'ඩ', 'එ', 'ෆ', 'ග', 'හ', 'ඉ', 'ජ', 'ක', 'ල', 'ම', 'න', 'ඔ', 'ප', 'කූ', 'ර', 'ස', 'ට', 'උ', 'ව', 'ව්', 'ක්ස්', 'ය', 'ස්']
    all_characters = list("abcdefghijklmnopqrstuvwxyz")
    
    randomized_mapping = {}
    for char in all_characters:
        if random.choice([True, False]):
            randomized_mapping[char] = random.choice(tamil_mapping)
        else:
            randomized_mapping[char] = random.choice(sinhala_mapping)
    
    return randomized_mapping

# Function to encode the password using the randomized mappings
def encode_password(password, key):
    mapping = generate_randomized_mapping(key)
    encoded_password = ''.join([mapping.get(char.lower(), char) for char in password])
    return encoded_password, mapping

# Function to check password with added complexity and obfuscation
def சோதனை_கடவுச்சொல்(correct_password):
    secret_key = input("Enter the secret key to generate the encoding: ")
    salt = os.urandom(16)
    derived_key = derive_key(secret_key, salt)  # Deriving a strong key using PBKDF2
    
    # Encrypt mapping using AES
    encrypted_mapping = encrypt(str(generate_randomized_mapping(secret_key)), derived_key)
    
    # Obfuscate the password using the randomized Tamil/Sinhala mappings
    encoded_password, mapping = encode_password(correct_password, secret_key)
    print(f"Obfuscated password (internal): {encoded_password}")
    
    # Decrypt the mapping securely using the derived key
    decrypted_mapping = eval(decrypt(encrypted_mapping, derived_key))  # Convert back to dict (remains secure)
    
    user_input = input("Enter the password: ")
    
    if len(user_input) != len(correct_password):
        print("Incorrect password length!")
        return
    
    previous_time = time.time()
    collatz_results = 0
    
    # Iterate over user input and check each character
    for i in range(len(user_input)):
        current_time = time.time()
        
        if user_input[i] == correct_password[i]:
            print(f"Character '{user_input[i]}' is correct!")
        else:
            print(f"Character '{user_input[i]}' is incorrect!")
        
        # Apply random number generation based on typing speed and Collatz sequence
        random_number = தட்டச்சு_வகை_அடிப்படையிலான_சீருடா(previous_time, current_time)
        collatz_results = காலச்சுழற்சி(random_number)
        
        # Output Collatz result for further obfuscation
        print(f"Collatz sequence result based on typing speed: {collatz_results}")
        
        previous_time = current_time
    
    print("Password check complete!")

# Example password for demonstration
correct_password = "secure123"
சோதனை_கடவுச்சொல்(correct_password)

