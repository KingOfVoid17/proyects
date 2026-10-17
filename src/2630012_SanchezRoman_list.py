'''
PORTADA
Nombre de la Materia: Metodologías de la programación
Nombre del Alumno:  [Tu Nombre Completo]
Matrícula:          [Tu Matrícula]
Grupo:              [Tu Grupo]
Fecha:              [Fecha de Entrega]
'''

'''
EXECUTIVE SUMMARY
- Lists in Python are ordered, mutable collections used to store dynamic items.
- Tuples are ordered, immutable collections ideal for fixed structure data.
- Dictionaries store key-value pairs, enabling fast lookups by key.
- Mutability allows lists to be changed in place, whereas tuple values cannot.
- Dictionaries associate unique keys with target values for structured data.
- This script covers 6 distinct problems illustrating real-world applications
  including shopping management, geometry, catalogs, grades, text analysis,
  and CRUD operations in a contact book using Python collections.
'''

'''
PRINCIPLES AND BEST PRACTICES
- Use lists when items need frequent addition, removal, or reordering.
- Use tuples for constant data (e.g., coordinates, configuration settings).
- Use dictionaries for quick value retrieval using explicit keys.
- Avoid modifying a list while iterating over it with a for loop.
- Choose descriptive snake_case key names in dictionaries.
- Ensure clear variable naming conventions and clean formatted outputs.
'''


'''
PROBLEM 1: Shopping list basics (list operations)
Description:
  Manages a list of products and their quantities. Parses an initial string,
  appends a new product, calculates total count, and verifies item presence.

Inputs:
  - initial_items_text (str): Comma-separated list of items.
  - new_item (str): Item to append.
  - search_item (str): Item to search in the list.

Outputs:
  - Printed messages in Spanish showing inputs, list status, and search results.

Validations:
  - Strip spaces and split string safely into a list.
  - Ensure new_item and search_item are sanitized with strip().

Test cases:
  1) Normal: Standard list of items with typical addition and search.
  2) Border: Single-item string or empty spaces processed correctly.
'''

print("--- PROBLEMA 1: Caso Normal ---")
# Hardcoded Inputs (Normal)
initial_items_text = "manzana, plátano, naranja"
new_item = "uva"
search_item = "plátano"

# Print Input Variables
print(f"Entradas -> initial_items_text: '{initial_items_text}', new_item: '{new_item}', search_item: '{search_item}'")

# Processing
items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
items_list.append(new_item.strip())
total_items = len(items_list)
is_in_list = search_item.strip().lower() in [i.lower() for i in items_list]

# Output (Spanish)
print(f"Lista de elementos: {items_list}")
print(f"Total de elementos: {total_items}")
print(f"Elemento encontrado: {'Sí' if is_in_list else 'No'}")

print("\n--- PROBLEMA 1: Caso Borde ---")
# Hardcoded Inputs (Border: single element with spaces)
initial_items_text = "  mango  "
new_item = "kiwi"
search_item = "sandía"

# Print Input Variables
print(f"Entradas -> initial_items_text: '{initial_items_text}', new_item: '{new_item}', search_item: '{search_item}'")

# Processing
items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
items_list.append(new_item.strip())
total_items = len(items_list)
is_in_list = search_item.strip().lower() in [i.lower() for i in items_list]

# Output (Spanish)
print(f"Lista de elementos: {items_list}")
print(f"Total de elementos: {total_items}")
print(f"Elemento encontrado: {'Sí' if is_in_list else 'No'}")


'''
PROBLEM 2: Points and distances with tuples
Description:
  Represents two points in a 2D plane using tuples, calculates the Euclidean
  distance between them, and computes the midpoint coordinate.

Inputs:
  - x1, y1, x2, y2 (float): Coordinates for points A and B.

Outputs:
  - Printed messages in Spanish displaying input coordinates, points, distance, and midpoint.

Validations:
  - Numeric values converted to float.

Test cases:
  1) Normal: Two distinct positive and negative coordinates.
  2) Border: Identical coordinates resulting in 0 distance.
'''

print("\n--- PROBLEMA 2: Caso Normal ---")
# Hardcoded Inputs (Normal)
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0

# Print Input Variables
print(f"Entradas -> x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")

# Processing
point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

# Output (Spanish)
print(f"Punto A: {point_a}")
print(f"Punto B: {point_b}")
print(f"Distancia: {round(distance, 4)}")
print(f"Punto Medio: {midpoint}")

print("\n--- PROBLEMA 2: Caso Borde ---")
# Hardcoded Inputs (Border: Same coordinates)
x1, y1 = 0.0, 0.0
x2, y2 = 0.0, 0.0

# Print Input Variables
print(f"Entradas -> x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")

# Processing
point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

# Output (Spanish)
print(f"Punto A: {point_a}")
print(f"Punto B: {point_b}")
print(f"Distancia: {round(distance, 4)}")
print(f"Punto Medio: {midpoint}")


'''
PROBLEM 3: Product catalog with dictionary
Description:
  Manages a product catalog in a dictionary (product -> price). Checks if
  a product exists and calculates total cost.

Inputs:
  - product_name (str): Name of the requested product.
  - quantity (int): Number of units to purchase.

Outputs:
  - Printed messages in Spanish showing input variables, unit price, quantity, and total.

Validations:
  - Check key presence in catalog.
  - Ensure quantity > 0.

Test cases:
  1) Normal: Existing product with standard quantity.
  2) Border: Purchase quantity of 1 for minimum cost check.
'''

catalog = {"manzana": 12.5, "plátano": 8.0, "naranja": 10.0}

print("\n--- PROBLEMA 3: Caso Normal ---")
# Hardcoded Inputs (Normal)
product_name = "manzana"
quantity = 3

# Print Input Variables
print(f"Entradas -> product_name: '{product_name}', quantity: {quantity}")

# Processing & Output (Spanish)
product_key = product_name.strip().lower()
if product_key in catalog and quantity > 0:
    unit_price = catalog[product_key]
    total_price = unit_price * quantity
    print(f"Precio unitario: ${unit_price}")
    print(f"Cantidad: {quantity}")
    print(f"Total a pagar: ${total_price}")
else:
    print("Error: Producto no encontrado")

print("\n--- PROBLEMA 3: Caso Borde ---")
# Hardcoded Inputs (Border: Minimum quantity)
product_name = "plátano"
quantity = 1

# Print Input Variables
print(f"Entradas -> product_name: '{product_name}', quantity: {quantity}")

# Processing & Output (Spanish)
product_key = product_name.strip().lower()
if product_key in catalog and quantity > 0:
    unit_price = catalog[product_key]
    total_price = unit_price * quantity
    print(f"Precio unitario: ${unit_price}")
    print(f"Cantidad: {quantity}")
    print(f"Total a pagar: ${total_price}")
else:
    print("Error: Producto no encontrado")


'''
PROBLEM 4: Student grades with dict and list
Description:
  Stores student names and lists of grades. Computes average score and
  determines pass status (average >= 70.0).

Inputs:
  - student_name (str): Name of the student.

Outputs:
  - Printed messages in Spanish with input variable, grades, average, and approval status.

Validations:
  - Verify student exists in dictionary and grade list is non-empty.

Test cases:
  1) Normal: Student with multiple high grades passing easily.
  2) Border: Student right on the threshold average score (70.0).
'''

grades_db = {
    "alicia": [85.0, 90.0, 95.0],
    "roberto": [70.0, 70.0, 70.0]
}

print("\n--- PROBLEMA 4: Caso Normal ---")
# Hardcoded Inputs (Normal)
student_name = "alicia"

# Print Input Variables
print(f"Entrada -> student_name: '{student_name}'")

# Processing & Output (Spanish)
key_name = student_name.strip().lower()
if key_name in grades_db and len(grades_db[key_name]) > 0:
    grades_list = grades_db[key_name]
    avg_score = sum(grades_list) / len(grades_list)
    is_passed = avg_score >= 70.0
    print(f"Calificaciones: {grades_list}")
    print(f"Promedio: {round(avg_score, 2)}")
    print(f"Estatus: {'Aprobado' if is_passed else 'Reprobado'}")
else:
    print("Error: Estudiante no encontrado")

print("\n--- PROBLEMA 4: Caso Borde ---")
# Hardcoded Inputs (Border: Exact passing grade)
student_name = "roberto"

# Print Input Variables
print(f"Entrada -> student_name: '{student_name}'")

# Processing & Output (Spanish)
key_name = student_name.strip().lower()
if key_name in grades_db and len(grades_db[key_name]) > 0:
    grades_list = grades_db[key_name]
    avg_score = sum(grades_list) / len(grades_list)
    is_passed = avg_score >= 70.0
    print(f"Calificaciones: {grades_list}")
    print(f"Promedio: {round(avg_score, 2)}")
    print(f"Estatus: {'Aprobado' if is_passed else 'Reprobado'}")
else:
    print("Error: Estudiante no encontrado")


'''
PROBLEM 5: Word frequency counter (list + dict)
Description:
  Tokenizes a sentence into words, counts occurrences using a dictionary,
  and identifies the most frequent word.

Inputs:
  - sentence (str): Input sentence to analyze.

Outputs:
  - Printed messages in Spanish displaying input sentence, word list, frequencies, and most common word.

Validations:
  - Remove punctuation marks and convert text to lowercase.

Test cases:
  1) Normal: Multi-word sentence with repeating words.
  2) Border: Single word sentence.
'''

print("\n--- PROBLEMA 5: Caso Normal ---")
# Hardcoded Inputs (Normal)
sentence = "Python es genial y Python es muy flexible!"

# Print Input Variables
print(f"Entrada -> sentence: '{sentence}'")

# Processing
cleaned_text = sentence.lower()
for char in [".", ",", "!", "?", ";"]:
    cleaned_text = cleaned_text.replace(char, "")

words_list = cleaned_text.split()
freq_dict = {}
for word in words_list:
    freq_dict[word] = freq_dict.get(word, 0) + 1

most_common_word = max(freq_dict, key=freq_dict.get) if freq_dict else ""

# Output (Spanish)
print(f"Lista de palabras: {words_list}")
print(f"Frecuencias: {freq_dict}")
print(f"Palabra más frecuente: '{most_common_word}'")

print("\n--- PROBLEMA 5: Caso Borde ---")
# Hardcoded Inputs (Border: Single word)
sentence = "Hola"

# Print Input Variables
print(f"Entrada -> sentence: '{sentence}'")

# Processing
cleaned_text = sentence.lower()
for char in [".", ",", "!", "?", ";"]:
    cleaned_text = cleaned_text.replace(char, "")

words_list = cleaned_text.split()
freq_dict = {}
for word in words_list:
    freq_dict[word] = freq_dict.get(word, 0) + 1

most_common_word = max(freq_dict, key=freq_dict.get) if freq_dict else ""

# Output (Spanish)
print(f"Lista de palabras: {words_list}")
print(f"Frecuencias: {freq_dict}")
print(f"Palabra más frecuente: '{most_common_word}'")


'''
PROBLEM 6: Simple contact book (dictionary CRUD)
Description:
  Implements CRUD operations (ADD, SEARCH, DELETE) on a contact book dictionary.

Inputs:
  - action_text (str): Action to execute ("ADD", "SEARCH", "DELETE").
  - name (str): Contact name.
  - phone (str): Phone number (used for "ADD").

Outputs:
  - Printed messages in Spanish confirming input variables, contact addition, search result, or deletion.

Validations:
  - Action normalized to uppercase.

Test cases:
  1) Normal: SEARCH operation for an existing contact.
  2) Border: ADD operation updating an existing contact.
'''

contacts = {"Alicia": "1234567890", "Roberto": "0987654321"}

print("\n--- PROBLEMA 6: Caso Normal ---")
# Hardcoded Inputs (Normal: SEARCH)
action_text = "SEARCH"
name = "Alicia"
phone = ""

# Print Input Variables
print(f"Entradas -> action_text: '{action_text}', name: '{name}', phone: '{phone}'")

# Processing & Output (Spanish)
action = action_text.strip().upper()
contact_name = name.strip()

if action == "ADD":
    contacts[contact_name] = phone.strip()
    print(f"Contacto guardado: {contact_name}, Teléfono: {phone.strip()}")
elif action == "SEARCH":
    if contact_name in contacts:
        print(f"Teléfono de {contact_name}: {contacts[contact_name]}")
    else:
        print("Error: Contacto no encontrado")
elif action == "DELETE":
    if contact_name in contacts:
        contacts.pop(contact_name)
        print(f"Contacto eliminado: {contact_name}")
    else:
        print("Error: Contacto no encontrado")

print("\n--- PROBLEMA 6: Caso Borde ---")
# Hardcoded Inputs (Border: ADD existing contact to update)
action_text = "ADD"
name = "Alicia"
phone = "5555555555"

# Print Input Variables
print(f"Entradas -> action_text: '{action_text}', name: '{name}', phone: '{phone}'")

# Processing & Output (Spanish)
action = action_text.strip().upper()
contact_name = name.strip()

if action == "ADD":
    contacts[contact_name] = phone.strip()
    print(f"Contacto guardado: {contact_name}, Teléfono: {phone.strip()}")
elif action == "SEARCH":
    if contact_name in contacts:
        print(f"Teléfono de {contact_name}: {contacts[contact_name]}")
    else:
        print("Error: Contacto no encontrado")
elif action == "DELETE":
    if contact_name in contacts:
        contacts.pop(contact_name)
        print(f"Contacto eliminado: {contact_name}")
    else:
        print("Error: Contacto no encontrado")


'''
CONCLUSIONS
- Selecting the appropriate data structure depends on mutability and access patterns.
- Lists offer high flexibility for growing or changing ordered elements.
- Tuples ensure data integrity for fixed structural data such as 2D coordinates.
- Dictionaries provide efficient key-value associations for direct lookups.
- Combining these collections (e.g., dictionary of lists) enables robust modeling.
'''

'''
REFERENCES
1) Python Documentation - Built-in Types (list, tuple, dict):
   https://docs.python.org/3/library/stdtypes.html
2) Severance, C. (2016). Python for Everybody: Exploring Data In Python 3.
3) Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media.
4) Real Python - Dictionaries in Python:
   https://realpython.com/python-dicts/
5) Real Python - Lists and Tuples in Python:
   https://realpython.com/python-lists-tuples/
'''