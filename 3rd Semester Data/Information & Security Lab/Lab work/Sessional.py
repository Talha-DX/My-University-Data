# 65 - 91 (A-Z)
# 97 - 122 (a-z)

#                             Vigonere Cipher

# def vigenere_encrypt(text, key):
#     cipher = ""
#     key = key.upper()
    
#     for i, ch in enumerate(text.upper()):
#         if ch.isalpha():
#             shift = ord(key[i % len(key)]) - 65
#             text += chr((ord(ch) - 65 + shift)%26 + 65)
#         else:
#             text += ch
#     return text

# def vigenere_dencrypt(text, key):
#     cipher = ""
#     key = key.upper()
    
#     for i, ch in enumerate(text.upper()):
#         if ch.isalpha():
#             shift = ord(key[i % len(key)]) - 65
#             text += chr((ord(ch) - 65 - shift)%26 + 65)
#         else:
#             text += ch
#     return text

# plain_txt = "ATTACKATDAWN"
# keyword   = "LEMON"
# cipher    = vigenere_encrypt(plain_txt,keyword)
# print("Encrypted: ",cipher)
# decryption = vigenere_dencrypt(cipher, keyword)
# print("Decrypted: ",decryption)

#                              MonoAlphabatic Cipher

# import string, random
# alphabet = list(string.ascii_uppercase)
# print(alphabet)
# key = alphabet.copy()
# random.shuffle(key)
# print(key)
# encrypt_map = {}
# dencrypt_map = {}
# for i in range(len(alphabet)):
#     encrypt_map[alphabet[i]] = key[i]
#     dencrypt_map[key[i]] = alphabet[i]
# message = "DEAF"
# cipher = ""
# for letter in message:
#     if letter.isalpha():
#         cipher += encrypt_map[letter]
#     else:
#         cipher += letter
# plain = ""
# for letter in cipher:
#     if letter.isalpha():
#         plain  += dencrypt_map[letter]
#     else:
#         plain += letter
# print("PlainText: ",message)
# print("Encrypted Text: ",cipher)
# print("Decrypted Text: ",plain)


#                                Rail Fence

# def encryptRailFence(text, key):
#     rail = [['\n' for i in range(len(text))]
#                 for j in range(key)]
#     # to find the direction
#     dir_down = False
#     row, col = 0, 0
#     for i in range(len(text)):
#         # check the direction of flow
#         # reverse the direction if we've just
#         # filled the top or bottom rail
#         if (row == 0) or (row == key - 1):
#             dir_down = not dir_down
        
#         # fill the corresponding alphabet
#         rail[row][col] = text[i]
#         col += 1
        
#         # find the next row using
#         # direction flag
#         if dir_down:
#             row += 1
#         else:
#             row -= 1
#     # now we can construct the cipher
#     # using the rail matrix
#     result = []
#     for i in range(key):
#         for j in range(len(text)):
#             if rail[i][j] != '\n':
#                 result.append(rail[i][j])
#     return("" . join(result))
    

# def decryptRailFence(cipher, key):

    
#     rail = [['\n' for i in range(len(cipher))]
#                 for j in range(key)]
    
#     # to find the direction
#     dir_down = None
#     row, col = 0, 0
    
#     # mark the places with '*'
#     for i in range(len(cipher)):
#         if row == 0:
#             dir_down = True
#         if row == key - 1:
#             dir_down = False
        
#         # place the marker
#         rail[row][col] = '*'
#         col += 1
        
#         # find the next row
#         # using direction flag
#         if dir_down:
#             row += 1
#         else:
#             row -= 1
            
#     # now we can construct the
#     # fill the rail matrix
#     index = 0
#     for i in range(key):
#         for j in range(len(cipher)):
#             if ((rail[i][j] == '*') and (index < len(cipher))):
#                 rail[i][j] = cipher[index]
#                 index += 1
        
#     # now read the matrix in
#     # zig-zag manner to construct
#     # the resultant text
#     result = []
#     row, col = 0, 0
#     for i in range(len(cipher)):
        
#         # check the direction of flow
#         if row == 0:
#             dir_down = True
#         if row == key-1:
#             dir_down = False
            
#         # place the marker
#         if (rail[row][col] != '*'):
#             result.append(rail[row][col])
#             col += 1
            
#         # find the next row using
#         # direction flag
#         if dir_down:
#             row += 1
#         else:
#             row -= 1
#     return("".join(result))

# # Driver code
# if __name__ == "__main__":
#     print(encryptRailFence("attack", 2))

#     # Now decryption of the
#     # same cipher-text
#     print(decryptRailFence("atctak", 2))


#                             PlayFair Cipher

# def playfair_prepare_key(keyword):
#     """
#     Prepares 5x5 Playfair matrix from a keyword.
#     Merges I/J into a single letter.
#     """
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J merged
#     key = ""
#     # Add unique letters from keyword
#     for ch in keyword.upper():
#         if ch not in key and ch in alphabet:
#             key += ch
#     # Add remaining letters
#     for ch in alphabet:
#         if ch not in key:
#             key += ch

#     # Create 5x5 matrix
#     matrix = []
#     for i in range(0, 25, 5):
#       row = key[i:i+5]  # Take 5 letters slice for this row
#       matrix.append(row)
#     return matrix

# def find_position(matrix, letter):
#     """Finds row and column of a letter in the matrix"""
#     for i, row in enumerate(matrix):
#         if letter in row:
#             return i, row.index(letter)
#     return None

# def preprocess_text(text):
#     """
#     Prepares text for Playfair cipher:
#     - Uppercase, replace J with I
#     - Split into digraphs
#     - Insert X between repeated letters
#     - Append X if length is odd
#     """
#     text = text.upper().replace("J", "I")
#     digraphs = []
#     i = 0
#     while i < len(text):
#         a = text[i]
#         b = ''
#         if i+1 < len(text):
#             b = text[i+1]
#         if a == b or b == '':
#             b = 'X'
#             i += 1
#         else:
#             i += 2
#         digraphs.append(a+b)

#     return digraphs

# def playfair_encrypt(plaintext, matrix):
#     ciphertext = ""
#     digraphs = preprocess_text(plaintext)
#     for pair in digraphs:
#         r1, c1 = find_position(matrix, pair[0])
#         r2, c2 = find_position(matrix, pair[1])
#         # Rule 1: Same row
#         if r1 == r2:
#             ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
#         # Rule 2: Same column
#         elif c1 == c2:
#             ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
#         # Rule 3: Rectangle
#         else:
#             ciphertext += matrix[r1][c2] + matrix[r2][c1]
#     return ciphertext

# def playfair_decrypt(ciphertext, matrix):
#     plaintext = ""
#     digraphs = []
#     for i in range(0, len(ciphertext), 2):
#       pair = ciphertext[i:i+2]
#       digraphs.append(pair)
      
#     for pair in digraphs:
#         r1, c1 = find_position(matrix, pair[0])
#         r2, c2 = find_position(matrix, pair[1])
#         # Rule 1: Same row
#         if r1 == r2:
#             plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
#         # Rule 2: Same column
#         elif c1 == c2:
#             plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
#         # Rule 3: Rectangle
#         else:
#             plaintext += matrix[r1][c2] + matrix[r2][c1]
#     return plaintext

# # ------------------- Example Usage -------------------

# keyword = "MONARCHY"
# matrix = playfair_prepare_key(keyword)
# print("Playfair Matrix:")
# for row in matrix:
#     print(row)

# plaintext = "INSTRUMENT"
# ciphertext = playfair_encrypt(plaintext, matrix)
# decrypted = playfair_decrypt(ciphertext, matrix)

# print("\nPlaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted:", decrypted)