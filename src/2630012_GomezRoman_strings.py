# Portada
'''
Nombre: Roman Francisco Sanchez Gomez
Matricula: 2630012
Grupo: M-I 2-1
'''

'''
4. EXECUTIVE SUMMARY
A Python string is an immutable sequence of Unicode characters,
meaning that once created, its content cannot be modified directly. Fundamental 
string operations include concatenation using the + operator,
determining length with len(), extracting substrings via slicing [a:b], 
searching for patterns using find() or 'in', and replacing text with replace().
Normalizing and validating input text—such as email addresses, names, and passwords—is crucial 
for ensuring system reliability,preventing runtime errors, and eliminating junk data. 
This project covers six structured string manipulation tasks, demonstrating input validation,
text transformation, and detailed test cases, alongside the complete implementation of the programs.

5. PRINCIPLES AND BEST PRACTICES
- Strings are immutable: Any operation or modification generates a completely 
new string object in memory.
- Clean and normalize inputs: It is best practice to use strip() and lower() 
before performing text comparisons.
- Avoid magic numbers: Do not hardcode arbitrary index values; explicitly document 
what each slice extracts.
- Leverage built-in string methods: Use standard Python methods instead of 
re-implementing basic logic manually.
- Design clear validations: Always structure checks sequentially, verifying that 
the string is non-empty before evaluating format rules.
- Write readable code: Use clear, descriptive lower_snake_case variable names and 
understandable, user-friendly error messages.
'''
'''
Problem 1: Full name formatter (name + initials)
Description: Normalizes a full name input by stripping unnecessary leading/trailing 
              and consecutive whitespaces, converts the text to Title Case, and 
              extracts uppercase initials separated by periods. 
 Inputs:
   - full_name (str): Full name provided as a single string.
 Outputs:
   - Formatted name in Title Case.
   - Uppercase initials (e.g., "J.C.T.").
 Validations:
   - full_name must not be empty or contain only whitespaces after strip().
   - Must contain at least two words (first name and last name).
 Test Cases:
   1) Normal: "  roman francisco sanchez gomez " -> Formatted name: "Roman Francisco Sanchez Gomez", Initials: "R.F.S.G."
   2) Border: "a b" -> Formatted name: "A B", Initials: "A.B."
'''
print('promblem 1.')
print('For the first problem, it will be a standard case: we will use a full name and derive from it both the name with the ' \
'initial letter capitalized and the initials themselves use title()\n.')
full_name='roman francisco Sanchez Gomez'
print("Normal problem\n")
print(full_name)
print(f'{full_name.title()} nombre en mayuscula \n')
print('iniciales\n')
words = full_name.strip().split()
initials_list = [word[0].upper() for word in words]
initials = ".".join(initials_list)
print(f'{initials} nombre con iniciales\n.')

full_name= 'a b'
print("Border problem\n")
print(full_name)
print(f'{full_name.title()} nombre en mayuscula \n')
print('iniciales\n')
words = full_name.strip().split()
initials_list = [word[0].upper() for word in words]
initials = ".".join(initials_list)
print(f'{initials} nombre con iniciales\n.')

'''
Problem 2: Simple email validator (structure + domain)
Description:Validates whether an email address meets basic format criteria: 
            contains exactly one '@', has no whitespaces, and includes at least 
            one dot '.' after the '@' symbol. If valid, extracts the domain.
Inputs:
 - email_text (str): Email address entered by the user.
Outputs:
 - "Valid email: true" or "Valid email: false"
 - If valid: "Domain: <domain_part>"
Validations:
 - email_text must not be empty after strip().
 - Must contain exactly one '@' character.
 - Must not contain any whitespace characters.
 - Must have at least one '.' in the domain part (after '@').
Test Cases:
 1) Normal: "user@example.com" -> Valid email: true, Domain: example.com
 2) Border: "a@b.c" -> Valid email: true, Domain: b.c
'''
print("Promblem 2.")
email_text ='sancjhez@gmail.com\n'.strip()
print("Normal problem\n")
print(email_text)
is_valid = False
if email_text and " " not in email_text:
    if email_text.count("@") ==1:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1:]
        if domain_part and "." in domain_part:
            is_valid = True
if is_valid:
    print("Valid email: true")
    print(f"Domain: {domain_part}\n")
else:
    print("Valid email: false")

email_text ='san@gml.m\n'.strip()
print("Border problem\n")
print(email_text)
is_valid = False
if email_text and " " not in email_text:
    if email_text.count("@") ==1:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1:]
        if domain_part and "." in domain_part:
            is_valid = True
if is_valid:
    print("Valid email: true")
    print(f"Domain: {domain_part}\n")
else:
    print("Valid email: false")

'''
Problem 3: Palindrome checker (ignoring spaces and case)
 Description: Evaluates whether a given phrase reads the same forward and backward. 
              Ignores whitespaces and letter casing during the evaluation.
 Inputs:
   - phrase (str): Text phrase assigned directly to a variable.
 Outputs:
   - "Is palindrome: true" or "Is palindrome: false"
 Validations:
   - phrase must not be empty after strip().
   - Cleaned phrase (without spaces) must have a length of at least 3 characters.
 Test Cases:
   1) Normal: "Anita lava la tina" -> Is palindrome: true
   2) Border: "Aba" -> Is palindrome: true
'''
print("Problem 3")
raw_phrase = "Anita lava la tina"
print("Normal problem\n")
print(raw_phrase)
cleaned_raw = raw_phrase.strip()
if not cleaned_raw:
    print("Error: invalid input")
else:
    cleaned_phrase = cleaned_raw.replace(" ", "").lower()

    if len(cleaned_phrase) < 3:
        print("Error: invalid input")
    else:
        is_palindrome = cleaned_phrase == cleaned_phrase[::-1]       
        if is_palindrome:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")

print("Border problem\n")
raw_phrase = "Aba"
print(raw_phrase)
cleaned_raw = raw_phrase.strip()
if not cleaned_raw:
    print("Error: invalid input")
else:
    cleaned_phrase = cleaned_raw.replace(" ", "").lower()
    if len(cleaned_phrase) < 3:
        print("Error: invalid input")
    else:
        is_palindrome = cleaned_phrase == cleaned_phrase[::-1]
        if is_palindrome:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")

'''
Problem 4: Sentence word stats (lengths and first/last word)
Description: Splits a sentence into words and calculates total word count, 
              first word, last word, shortest word, and longest word.
Inputs:
   - sentence (str): Sentence assigned directly to a variable.
Outputs:
   - Total word count, First word, Last word, Shortest word, Longest word.
Validations:
   - sentence must not be empty after strip().
   - Must contain at least one valid word after split().
Test Cases:
   1) Normal: "The quick brown fox jumps" -> Count: 5, First: The, Last: jumps...
   2) Border: "   Hello   " -> Count: 1, First: Hello, Last: Hello...
'''

sentence = "The quick brown fox jumps"
print(sentence)
print("Normal problem\n")
cleaned_sentence = sentence.strip()

if not cleaned_sentence:
    print("Error: invalid input")
else:
    words = cleaned_sentence.split()
    
    if len(words) < 1:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)

        print(f"Total words: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

print("Border problem\n")
sentence = "   Hello   "
print(sentence)
cleaned_sentence = sentence.strip()

if not cleaned_sentence:
    print("Error: invalid input")
else:
    words = cleaned_sentence.split()
    
    if len(words) < 1:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)

        print(f"Total words: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

'''
Problem 5: Password strength classifier
Description: Evaluates a password and classifies its strength as weak, medium, 
              or strong based on length, uppercase, lowercase, numbers, and symbols.
Inputs:
   - password_input (str): Password string assigned directly to a variable.
 Outputs:
   - "Password strength: weak", "medium", or "strong"
 Validations:
   - password_input must not be empty.
Test Cases:
   1) Normal: "P@ssword123" -> Password strength: strong
   2) Border: "Password1" -> Password strength: medium
'''

print("Normal problem\n")
password_input = "P@ssword123"
print(password_input)

if not password_input:
    print("Error: invalid input")
else:
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_symbol = any(not c.isalnum() for c in password_input)
    is_long_enough = len(password_input) >= 8

    categories_count = sum([has_upper, has_lower, has_digit, has_symbol])

    if is_long_enough and categories_count == 4:
        strength = "strong"
    elif is_long_enough and categories_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")

print("Border problem\n")
password_input = "Password1"
print(password_input)

if not password_input:
    print("Error: invalid input")
else:
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_symbol = any(not c.isalnum() for c in password_input)
    is_long_enough = len(password_input) >= 8

    categories_count = sum([has_upper, has_lower, has_digit, has_symbol])

    if is_long_enough and categories_count == 4:
        strength = "strong"
    elif is_long_enough and categories_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")

'''
 Problem 6: Product label formatter (fixed-width text)
 Description: Formats a product name and price into a single line label, 
              truncating or padding spaces to guarantee exactly 30 characters.
Inputs:
   - product_name (str): Product name assigned directly to a variable.
   - price_value (float): Product price assigned directly to a variable.
Outputs:
   - Formatted label of exactly 30 characters.
 Validations:
   - product_name must not be empty after strip().
   - price_value must be a valid positive number.
Test Cases:
   1) Normal: "Laptop", 999.99 -> "Product: Laptop | Price: $999.99  " (30 chars)
   2) Border: "Super Ultra Megaphone Device", 10.0 -> "Product: Super Ultra Megaphone " (30 chare)
'''
print("Normal problem\n")
product_name = "Laptop"
price_value = 999.99
print(product_name)
print(price_value)

cleaned_product = product_name.strip()

if not cleaned_product or price_value < 0:
    print("Error: invalid input")
else:
    TARGET_LENGTH = 30
    formatted_label = f"Product: {cleaned_product} | Price: ${price_value:.2f}"
    
    if len(formatted_label) > TARGET_LENGTH:
        formatted_label = formatted_label[:TARGET_LENGTH]
    elif len(formatted_label) < TARGET_LENGTH:
        formatted_label = formatted_label.ljust(TARGET_LENGTH)
        
    print(f"'{formatted_label}'")
    print(f"Label length: {len(formatted_label)}")

print("Border problem\n")
product_name = "Super Ultra Megaphone Device"
price_value = 10.0
print(product_name)
print(price_value)

cleaned_product = product_name.strip()

if not cleaned_product or price_value < 0:
    print("Error: invalid input")
else:
    TARGET_LENGTH = 30
    formatted_label = f"Product: {cleaned_product} | Price: ${price_value:.2f}"
    
    if len(formatted_label) > TARGET_LENGTH:
        formatted_label = formatted_label[:TARGET_LENGTH]
    elif len(formatted_label) < TARGET_LENGTH:
        formatted_label = formatted_label.ljust(TARGET_LENGTH)
        
    print(f"'{formatted_label}'")
    print(f"Label length: {len(formatted_label)}")

'''
8. CONCLUSIONS
 String handling is fundamental for managing system inputs and outputs reliably, 
 ensuring clean data exchange between users and applications. Utilizing standard 
 methods like lower(), strip(), split(), and join() simplifies text cleanup and 
 standardizes structured strings efficiently. Normalizing text before evaluation 
 prevents unexpected logic errors caused by inconsistent capitalization or hidden 
 whitespace. Designing clear validation controls eliminates garbage data early and 
 prevents application crashes. Furthermore, understanding string immutability 
 highlights the efficiency of using slicing operations to create transformed 
 substrings without corrupting original data objects in memory.
9. REFERENCES
 1) Python Software Foundation. "Built-in Types: Text Sequence Type — str." 
    Python Documentation. https://docs.python.org/3/library/stdtypes.html#textseq
 2) Sweigart, Al. "Automating the Boring Stuff with Python: Manipulating Strings." 
    No Starch Press. https://automatetheboringstuff.com/2e/chapter6/
 3) Lutz, Mark. "Learning Python: Powerful Object-Oriented Programming." 
    O'Reilly Media, 5th Edition.
 4) Real Python. "Python Strings and Character Data in Python." 
    Real Python Tutorials. https://realpython.com/python-strings/
 5) W3Schools. "Python String Methods Reference." 
    W3Schools Online Web Tutorials. https://www.w3schools.com/python/python_ref_string.asp
'''