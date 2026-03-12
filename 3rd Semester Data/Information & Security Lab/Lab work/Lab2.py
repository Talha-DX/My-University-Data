# Id = [111,222,222,444,0,555]
# Uni = []
# count = 0
# for i in Id:
#     if i == 0:
#         break
#     elif i in Uni:
#         print(i,"Warning of this studnet")
#     else:
#         Uni.append(i)   
#     count = count + 1
    
# for j in Uni:
#     print(j)
# print("Total Number of Student ID's:",count)    

# ------------------------ Task 1 -------------------------
# Id = []
# for i in range(10):
#     j = input("Enter Student ID's: ")
#     Id.append(j)

# Uni = []
# count = 0
# for i in Id:
#     if i == "0":
#         break
#     if i in Uni:
#         print(i,"Warning of this studnet")
#     else:
#         Uni.append(i)   
#     count = count + 1
    
# for j in Uni:
#     print(j)
# print("Total Number of Student ID's:",count)    



# ------------------------ Task 2 -------------------------
# password = input("Enter Password: ")

# while len(password) <= 8:
#     print("Password must have 8 charachters.")
#     password = input("Enter Password: ")
    
# special_char = "!@#$%&*"

# has_char = any(ch.isupper() for ch in password)
# has_number = any(ch.isdigit() for ch in password)
# has_special = any(ch in special_char for ch in password)

# if has_char and has_number and has_special:
#     print("Password is Valid.")
# else:
#     if not has_char:
#         print("Password must have a character.")
#     if not has_number:
#         print("Password must have a number.")
#     if not has_special:
#         print("Password must have any special character.")


# ------------------------ Task 3 -------------------------
# def add_student(name, *marks):
#     print(name, marks)

# def calculate_average(*marks):
#     sum = 0
#     for i in marks:
#         sum = sum+ int(i)
#     avg = sum / len(marks)
#     print(avg)

# def assign_grade(average):
#     if average > 80:
#         grade = 'A'
#     elif average > 60 and average <80:
#         grade = 'B'
#     else:
#         grade = 'F'
#     return grade
    

# marks = {}
# for i in range(1,5):
#     student = input("Enter Student ",i,"marks: ")
#     for j in 
    
# add_student(name,marks)
# calculate_average(marks)
# assign_grade(marks)

# Simple Task 3 Solution

# Function to add student data

# ---------------------------- Task 3 ----------------------
# students = []

# def add_student(name, *marks):
#     student = {"name": name, "marks": marks}
#     students.append(student)

# def calculate_average(*marks):
#     return sum(marks) / len(marks)

# def assign_grade(avg):
#     if avg >= 90:
#         return "A"
#     elif avg >= 80:
#         return "B"
#     elif avg >= 70:
#         return "C"
#     elif avg >= 60:
#         return "D"
#     else:
#         return "F"

# for i in range(5):
#     print(f"\nStudent {i + 1}")
#     name = input("Enter name: ")
#     marks = []
#     for j in range(3):
#         mark = float(input(f"Enter mark {j + 1}: "))
#         marks.append(mark)
#     add_student(name, *marks)

# print("\nStudent Report")
# print(f"{'Name':<15}{'Average':<10}{'Grade'}")
# print("-" * 30)

# for s in students:
#     avg = calculate_average(*s["marks"])
#     grade = assign_grade(avg)
#     print(f"{s['name']:<15}{avg:<10.2f}{grade}")

# ----------------- 4 ---------------------
# def get_max_min(temps):
#     max_temp = temps[0]
#     min_temp = temps[0]
#     for t in temps:
#         if t > max_temp:
#             max_temp = t
#         if t < min_temp:
#             min_temp = t
#     return max_temp, min_temp

# def above_average(temps):
#     total = 0
#     for t in temps:
#         total += t
#     avg = total / len(temps)
#     print(f"\nAverage temperature: {avg:.2f}")
#     print("Days with above-average temperature:")
#     for i in range(len(temps)):
#         if temps[i] > avg:
#             print(f"Day {i + 1}: {temps[i]}")

# temps = []
# print("Enter temperatures for 7 days:")
# for i in range(7):
#     t = int(input(f"Day {i + 1}: "))
#     temps.append(t)

# max_t, min_t = get_max_min(temps)
# print(f"\nHighest temperature: {max_t}")
# print(f"Lowest temperature: {min_t}")

# above_average(temps)
# ----------------------- 5 --------------------
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

#     def borrow_book(self):
#         if self.is_borrowed == False:
#             self.is_borrowed = True
#             print("You borrowed", self.title)
#         else:
#             print("Already borrowed")

#     def return_book(self):
#         if self.is_borrowed == True:
#             self.is_borrowed = False
#             print("You returned", self.title)
#         else:
#             print("It was not borrowed")

#     def display_info(self):
#         if self.is_borrowed == True:
#             status = "Borrowed"
#         else:
#             status = "Available"
#         print(self.title, "-", self.author, "-", status)


# books = [
#     Book("English", "Ali"),
#     Book("Islamiyat", "Atif"),
#     Book("Science", "Rafay"),
#     Book("Physics", "James Bond"),
#     Book("Mathematics", "Shilaa ki jawani")
# ]
# while True:
#     print("\n1. Show books")
#     print("2. Borrow")
#     print("3. Return")
#     print("4. Exit")
#     ch = input("Enter choice: ")
#     if ch == "1":
#         for i in range(len(books)):
#             print(i+1, end=". ")
#             books[i].display_info()
#     elif ch == "2":
#         n = int(input("Enter book number: ")) - 1
#         books[n].borrow_book()
#     elif ch == "3":
#         n = int(input("Enter book number: ")) - 1
#         books[n].return_book()
#     elif ch == "4":
#         break
#     else:
#         print("Wrong choice")
# -----------------6-------------------
# class Employee:
#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept
#         self.monthly_scores = []

#     def add_score(self, score):
#         self.monthly_scores.append(score)

#     def average_score(self):
#         total = 0
#         for s in self.monthly_scores:
#             total += s
#         avg = total / len(self.monthly_scores)
#         return avg

#     def performance_level(self):
#         avg = self.average_score()
#         if avg >= 90:
#             return "Excellent"
#         elif avg >= 75:
#             return "Good"
#         elif avg >= 60:
#             return "Average"
#         else:
#             return "Poor"
        
# emp1 = Employee("Alice", "HR")
# emp2 = Employee("Bob", "Sales")
# emp3 = Employee("Charlie", "IT")
# emps = [emp1, emp2, emp3]
# import random
# for e in emps:
#     for i in range(5):  # 5 months
#         e.add_score(random.randint(50, 100))
# for e in emps:
#     print("\nName:", e.name)
#     print("Dept:", e.dept)
#     print("Average Score:", round(e.average_score(), 2))
#     print("Performance:", e.performance_level())


# ----------------------------Lab # 06------------------------
# Line Cipher
def playfair_prepare_key(keyword):
    """
    Prepares 5x5 Playfair matrix from a keyword.
    Merges I/J into a single letter.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J merged
    key = ""
    # Add unique letters from keyword
    for ch in keyword.upper():
        if ch not in key and ch in alphabet:
            key += ch
    # Add remaining letters
    for ch in alphabet:
        if ch not in key:
            key += ch

    # Create 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
      row = key[i:i+5]  # Take 5 letters slice for this row
      matrix.append(row)
    return matrix

def find_position(matrix, letter):
    """Finds row and column of a letter in the matrix"""
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None

def preprocess_text(text):
    """
    Prepares text for Playfair cipher:
    - Uppercase, replace J with I
    - Split into digraphs
    - Insert X between repeated letters
    - Append X if length is odd
    """
    text = text.upper().replace("J", "I")
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i+1 < len(text):
            b = text[i+1]
        if a == b or b == '':
            b = 'X'
            i += 1
        else:
            i += 2
        digraphs.append(a+b)

    return digraphs

def playfair_encrypt(plaintext, matrix):
    ciphertext = ""
    digraphs = preprocess_text(plaintext)
    for pair in digraphs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        # Rule 1: Same row
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        # Rule 2: Same column
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        # Rule 3: Rectangle
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    digraphs = []
    for i in range(0, len(ciphertext), 2):
      pair = ciphertext[i:i+2]
      digraphs.append(pair)
      
    for pair in digraphs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        # Rule 1: Same row
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        # Rule 2: Same column
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        # Rule 3: Rectangle
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

# ------------------- Example Usage -------------------


keyword = "SECURITY"
matrix = playfair_prepare_key(keyword)
print("Playfair Matrix:")
for row in matrix:
    print(row)

plaintext = "TALHACRICKET"
ciphertext = playfair_encrypt(plaintext, matrix)
decrypted = playfair_decrypt(ciphertext, matrix)

print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)


# ---------------------------------------------------------------------------

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)
iv = get_random_bytes(16)

plain_text = &quot;Hello, this is AES!&quot;

def pad(text):
   while len(text) % 16 != 0:
     text += &#39; &#39;
 return text

cipher = AES.new(key, AES.MODE_CBC, iv)
padded_text = pad(plain_text).encode(&#39;utf-8&#39;)
cipher_text = cipher.encrypt(padded_text)

cipher_text_base64 = base64.b64encode(cipher_text).decode(&#39;utf-8&#39;)
print(&quot;Encrypted Text:&quot;, cipher_text_base64)

cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher_decrypt.decrypt(cipher_text).decode(&#39;utf-8&#39;).strip()
print(&quot;Decrypted Text:&quot;, decrypted_text)