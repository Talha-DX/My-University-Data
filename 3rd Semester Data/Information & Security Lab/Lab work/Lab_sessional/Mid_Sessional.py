def VG_Encrypt(text, key):
    key = key.upper()
    vowel = "AEIOU"
    result = ""

    for i, ch in enumerate(text.upper()):
        a_shift = ord(key[i % len(key)]) - 65
        
        if key[i % len(key)] in vowel:
            shift = a_shift + 2
        else:
            shift = a_shift
        
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    
    return result


def VG_Decrypt(text, key):
    key = key.upper()
    vowel = "AEIOU"
    result = ""

    for i, ch in enumerate(text.upper()):
        b_shift = ord(key[i % len(key)]) - 65

        if key[i % len(key)] in vowel:
            shift = b_shift + 2
        else:
            shift = b_shift

        result += chr((ord(ch) - 65 - shift) % 26 + 65)

    return result


characters = "!@#$%^&*()_+=}|[]:;?><"
numbers = "1234567890"

while True:
    text = input("Enter the text: ")
    if any(ch in characters or ch in numbers for ch in text):
        print("Invalid Input. Please enter text without special characters or numbers.")
    else:
        break

key = input("Enter the key: ")

encrp = VG_Encrypt(text, key)
print("Encryption Text:", encrp)

decrp = VG_Decrypt(encrp, key)
print("Decryption Text:", decrp)



