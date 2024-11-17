# CryptoObfuscator-Advanced-AES-Encryption-Obfuscation-Techniques-for-Secure-Systems
making hard  reverse engineering 

# CryptoObfuscator

## Description
CryptoObfuscator is a powerful and complex password obfuscation tool that utilizes AES encryption, dynamic character mapping (Tamil and Sinhala), and a unique typing speed-based Collatz sequence. This project combines advanced techniques in cryptography and obfuscation to make reverse engineering extremely challenging.

The tool applies AES encryption with a secret key, random character mapping (between Tamil and Sinhala), and dynamic checks based on typing speed to obscure passwords. This multi-layer approach makes it highly secure and hard to reverse engineer.

## Features
- **AES Encryption**: Encrypts passwords with AES-CBC, ensuring strong encryption.
- **Randomized Character Mapping**: Randomly chooses between Tamil and Sinhala character sets for added complexity.
- **Collatz Conjecture**: Applies Collatz calculations based on typing speed to further obfuscate the password input process.
- **Password Length & Complexity Check**: Ensures password checks while considering length and complexity for secure password validation.

## Installation

1. **Clone this repository to your local machine**:
    ```bash
    git clone https://github.com/yourusername/CryptoObfuscator.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd CryptoObfuscator
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Program**: To test the password encoding and obfuscation functionality, run the `main.py` script:
    ```bash
    python main.py
    ```

2. **Enter the Secret Key**: When prompted, input the secret key to generate the randomized encoding.

3. **Enter the Password**: The program will obfuscate the password using the randomized character mappings and apply AES encryption.

4. **Password Check**: The program will check the entered password and display the Collatz sequence results based on your typing speed.

## Security Considerations

- **AES Key Management**: The secret key used for AES encryption should be kept secure. Always use strong, unique keys for each encryption.
- **Password Length & Complexity**: While this project applies heavy obfuscation, ensuring that the password itself is complex and long adds another layer of security.
- **Reverse Engineering**: The combination of AES encryption, random character mappings, and real-time typing-speed analysis makes it very difficult to reverse engineer the obfuscation process.

## Contribution

Feel free to fork this project and submit pull requests with improvements or new features. Please ensure all contributions adhere to the project’s coding standards and are thoroughly tested.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **pyCryptodome**: Used for AES encryption and decryption.
- **Base64**: Used for encoding and decoding data.
- **Randomization and Obfuscation**: Custom implementations to increase password security and add complexity.

---

## Code Overview

```python
import random
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

# AES Encryption and Decryption Helper Functions
def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt(data, key):
    raw = base64.b64decode(data)
    iv, ct = raw[:16], raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

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

# Function to generate a randomized character set
def generate_randomized_mapping(key):
    random.seed(key)  # Use the key to ensure the mapping is reproducible
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

# Function to check password with complexity and obfuscation
def சோதனை_கடவுச்சொல்(correct_password):
    secret_key = input("Enter the secret key to generate the encoding: ")
    encrypted_mapping = encrypt(str(generate_randomized_mapping(secret_key)), secret_key)
    
    encoded_password, mapping = encode_password(correct_password, secret_key)
    print(f"Obfuscated password (internal): {encoded_password}")
    
    decrypted_mapping = eval(decrypt(encrypted_mapping, secret_key))
    
    user_input = input("Enter the password: ")
    
    if len(user_input) != len(correct_password):
        print("Incorrect password length!")
        return
    
    previous_time = time.time()
    collatz_results = 0
    
    for i in range(len(user_input)):
        current_time = time.time()
        
        if user_input[i] == correct_password[i]:
            print(f"Character '{user_input[i]}' is correct!")
        else:
            print(f"Character '{user_input[i]}' is incorrect!")
        
        random_number = தட்டச்சு_வகை_அடிப்படையிலான_சீருடா(previous_time, current_time)
        collatz_results = காலச்சுழற்சி(random_number)
        
        print(f"Collatz sequence result based on typing speed: {collatz_results}")
        
        previous_time = current_time
    
    print("Password check complete!")

correct_password = "secure123"
சோதனை_கடவுச்சொல்(correct_password)

