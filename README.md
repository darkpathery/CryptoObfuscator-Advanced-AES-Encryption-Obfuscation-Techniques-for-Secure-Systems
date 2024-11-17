# Linguistic Mathematical Obfuscation Engine

## Project Overview
This project aims to make reverse engineering significantly harder by blending complex, unsolved mathematical equations with linguistic encoding in a programmatic environment. By combining AES encryption, real-time Collatz conjecture sequences, and dynamic linguistic transformations, this software offers high levels of obfuscation and security.

### Features
- **Mathematical Obfuscation:** Integrates complex mathematical logic such as the Collatz conjecture to complicate reverse engineering.
- **AES Encryption:** Secure data using AES encryption with a secret key.
- **Linguistic Encoding:** Maps characters to random Tamil/Sinhala characters based on the secret key, adding complexity.
- **Typing Speed-Based Randomization:** Uses user typing speed to influence random number generation.


## code

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



  
## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/Linguistic-Mathematical-Obfuscation.git
cd Linguistic-Mathematical-Obfuscation


## Security Considerations

- **AES Key Management:** The secret key used for AES encryption should be kept safe. Use strong, unique keys for better security.
- **Password Complexity:** While this project adds significant obfuscation, it’s still important to choose a long, complex password.
- **Reverse Engineering Resistance:** The combined use of mathematical obfuscation, AES encryption, and linguistic encoding makes it much harder to reverse engineer.

## Contribution

Feel free to fork this repository and submit pull requests for improvements or new features. Please make sure to test new features thoroughly and follow coding best practices.


## future Development
This project is intended to be a continuous effort in exploring new methods for increasing code obfuscation, encryption, and reverse engineering resistance. Below are some areas for future development:

Advanced Mathematical Equations Integration:

Future versions may integrate more complex and unsolved mathematical problems to enhance the difficulty of reverse engineering. The aim is to make the software harder to understand and reverse while maintaining its core functionality.
Expanded Linguistic Assignments:

Further research into using different languages and linguistics for encoding passwords or data, blending them with mathematical randomness, could be incorporated.
Real-Time Typing and Behavior Analysis:

Improvements in real-time typing analysis and behavior tracking may add further layers of obfuscation and security. This could include adapting the obfuscation scheme dynamically based on typing speed, pressure, or other unique human factors.
Optimizing the Code for Performance:

Over time, optimizations may be made to enhance the speed and efficiency of the software without compromising security. This could involve better memory management and faster algorithms for encryption.
Additional Encryption Schemes:

Although AES is used for encryption, future versions of the software could implement alternative or hybrid encryption schemes to further diversify security strategies.
Cross-Platform Compatibility:

Making the tool compatible with more platforms (e.g., Windows, macOS, and Linux) and extending its usability with a user-friendly interface (GUI) for less technical users.
Community Contributions:

Contributions from the open-source community are encouraged. Ideas for new features, optimizations, or research into advanced encryption and obfuscation methods are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- **pyCryptodome:** For AES encryption and decryption functionality.
- **Mathematical Obfuscation:** Custom logic, including Collatz conjecture-based randomization.
- **Linguistic Encoding:** Random character mappings with Tamil and Sinhala characters for additional encoding complexity.

