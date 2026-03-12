class ClassicalCiphers:
    @staticmethod
    def caesar_encrypt(text, shift=3):
        """Caesar cipher encryption"""
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result
    
    @staticmethod
    def caesar_decrypt(text, shift=3):
        """Caesar cipher decryption"""
        return ClassicalCiphers.caesar_encrypt(text, -shift)
    
    @staticmethod
    def vigenere_encrypt(text, key):
        """Vigenère cipher encryption"""
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                key_char = key[key_index % len(key)]
                shift = ord(key_char) - 65
                
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
                key_index += 1
            else:
                result += char
        return result
    
    @staticmethod
    def vigenere_decrypt(text, key):
        """Vigenère cipher decryption"""
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                key_char = key[key_index % len(key)]
                shift = ord(key_char) - 65
                
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
                key_index += 1
            else:
                result += char
        return result
    
    @staticmethod
    def rail_fence_encrypt(text, rails=3):
        """Rail Fence cipher encryption"""
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        
        for char in text:
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction = -direction
        
        return ''.join([''.join(rail) for rail in fence])
    
    @staticmethod
    def rail_fence_decrypt(text, rails=3):
        """Rail Fence cipher decryption"""
        fence = [[''] * len(text) for _ in range(rails)]
        
        # Build fence pattern
        rail = 0
        direction = 1
        for i in range(len(text)):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction = -direction
        
        # Fill fence with ciphertext
        index = 0
        for r in range(rails):
            for c in range(len(text)):
                if fence[r][c] == '*' and index < len(text):
                    fence[r][c] = text[index]
                    index += 1
        
        # Read plaintext
        result = []
        rail = 0
        direction = 1
        for i in range(len(text)):
            result.append(fence[rail][i])
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction = -direction
        
        return ''.join(result)
    
    @staticmethod
    def get_ciphers():
        """Return available ciphers"""
        return {
            "Caesar": ClassicalCiphers.caesar_encrypt,
            "Vigenère": ClassicalCiphers.vigenere_encrypt,
            "Rail Fence": ClassicalCiphers.rail_fence_encrypt
        }