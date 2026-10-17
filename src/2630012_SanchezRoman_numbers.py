"""
===============================================================================
HEADER / COVER
===============================================================================
Nombre:Roman Francisco Sanchez Gomez
Matricula:2630012
Group: I-M 1-2
===============================================================================
"""

"""
===============================================================================
EXECUTIVE SUMMARY
===============================================================================
In Python, integer (int) and floating-point (float) data types differ in precision 
and intent: int is used to count discrete elements, whereas float represents 
continuous numerical values and measurements with decimals. A boolean (bool) 
represents a truth value (True or False) obtained primarily through relational 
comparisons and logical operations. Validating input data and ranges is critical 
to prevent execution errors such as division by zero or processing physically 
impossible values. This document provides solutions to 6 practical problems 
utilizing type casting, logical operators, relational comparisons, and formatted outputs.
===============================================================================
"""

"""
===============================================================================
PRINCIPLES AND BEST PRACTICES
===============================================================================
1. Appropriate Type Selection: Use int for counters/choices and float for financial, 
   temperature, or physical body metrics.
2. Code Clarity & Reuse: Store intermediate calculation results in variables with 
   expressive names formatted in lower_snake_case.
3. Preventive Validations: Verify ranges and logical conditions before executing 
   critical arithmetic operations.
4. Clear Output Messages: Display readable console output in Spanish.
5. Boolean Interpretation: Ensure True/False flags accurately reflect the 
   evaluated logical state.
===============================================================================
"""


# PROBLEM 1: Temperature converter and range flag

"""
Problem 1: Temperature converter and range flag
Description:
Converts temperature from Celsius to Fahrenheit and Kelvin, and evaluates 
whether the temperature in Celsius is high (greater than or equal to 30.0).

Inputs:
- temp_c (float)

Outputs:
- Input Celsius temperature: <temp_c>
- Fahrenheit: <temp_f>
- Kelvin: <temp_k>
- High temperature: true|false

Validations:
- Prevent temperatures below absolute zero in Kelvin (temp_k < 0.0).

Test cases:
1) Normal: temp_c = 25.0 -> Fahrenheit: 77.0, Kelvin: 298.15, High temperature: False
2) Border: temp_c = 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: True
"""

# Problem 1 Code - Normal Case
print("--- Problema 1: Caso Normal ---")
temp_c = 25.0
temp_k = temp_c + 273.15

print("Temperatura Celsius de entrada:", temp_c)
if temp_k < 0.0:
    print("Error: entrada inválida")
else:
    temp_f = (temp_c * 9 / 5) + 32
    is_high_temperature = temp_c >= 30.0
    print("Fahrenheit:", temp_f)
    print("Kelvin:", temp_k)
    print("Temperatura alta:", is_high_temperature)

# Problem 1 Code - Border Case
print("\n--- Problema 1: Caso Borde ---")
temp_c = 30.0
temp_k = temp_c + 273.15

print("Temperatura Celsius de entrada:", temp_c)
if temp_k < 0.0:
    print("Error: entrada inválida")
else:
    temp_f = (temp_c * 9 / 5) + 32
    is_high_temperature = temp_c >= 30.0
    print("Fahrenheit:", temp_f)
    print("Kelvin:", temp_k)
    print("Temperatura alta:", is_high_temperature)

# PROBLEM 2: Work hours and overtime payment

"""
Problem 2: Work hours and overtime payment
Description:
Calculates total weekly pay including regular pay (up to 40 hours) and overtime 
pay (150% rate for hours over 40). Also determines if overtime occurred.

Inputs:
- hours_worked (float)
- hourly_rate (float)

Outputs:
- Input hours worked: <hours_worked>
- Input hourly rate: <hourly_rate>
- Regular pay: <regular_pay>
- Overtime pay: <overtime_pay>
- Total pay: <total_pay>
- Has overtime: true|false

Validations:
- hours_worked >= 0
- hourly_rate > 0

Test cases:
1) Normal: hours_worked = 45.0, hourly_rate = 10.0 -> Regular pay: 400.0, Overtime pay: 75.0, Total pay: 475.0, Has overtime: True
2) Border: hours_worked = 40.0, hourly_rate = 10.0 -> Regular pay: 400.0, Overtime pay: 0.0, Total pay: 400.0, Has overtime: False
"""

# Problem 2 Code - Normal Case
print("\n--- Problema 2: Caso Normal ---")
hours_worked = 45.0
hourly_rate = 10.0

print("Horas trabajadas de entrada:", hours_worked)
print("Pago por hora de entrada:", hourly_rate)

if hours_worked < 0 or hourly_rate <= 0:
    print("Error: entrada inválida")
else:
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(hours_worked - 40.0, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40.0

    print("Pago regular:", regular_pay)
    print("Pago por horas extra:", overtime_pay)
    print("Pago total:", total_pay)
    print("Tiene horas extra:", has_overtime)

# Problem 2 Code - Border Case
print("\n--- Problema 2: Caso Borde ---")
hours_worked = 40.0
hourly_rate = 10.0

print("Horas trabajadas de entrada:", hours_worked)
print("Pago por hora de entrada:", hourly_rate)

if hours_worked < 0 or hourly_rate <= 0:
    print("Error: entrada inválida")
else:
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(hours_worked - 40.0, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40.0

    print("Pago regular:", regular_pay)
    print("Pago por horas extra:", overtime_pay)
    print("Pago total:", total_pay)
    print("Tiene horas extra:", has_overtime)


# PROBLEM 3: Discount eligibility with booleans

"""
Problem 3: Discount eligibility with booleans
Description:
Determines eligibility for a 10% discount based on student status, senior status, 
or purchase total exceeding 1000.0. Calculates final payable total.

Inputs:
- purchase_total (float)
- is_student_text (string)
- is_senior_text (string)

Outputs:
- Input purchase total: <purchase_total>
- Input is student: <is_student_text>
- Input is senior: <is_senior_text>
- Discount eligible: true|false
- Final total: <final_total>

Validations:
- purchase_total >= 0.0
- Text inputs must be strictly "YES" or "NO" (case insensitive).

Test cases:
1) Normal: purchase_total = 500.0, student = "YES", senior = "NO" -> Discount eligible: True, Final total: 450.0
2) Border: purchase_total = 1000.0, student = "NO", senior = "NO" -> Discount eligible: True, Final total: 900.0
"""

# Problem 3 Code - Normal Case
print("\n--- Problema 3: Caso Normal ---")
purchase_total = 500.0
is_student_text = "YES"
is_senior_text = "NO"

print("Total de compra de entrada:", purchase_total)
print("Es estudiante (entrada):", is_student_text)
print("Es adulto mayor (entrada):", is_senior_text)

valid_answers = ["YES", "NO"]
student_upper = is_student_text.strip().upper()
senior_upper = is_senior_text.strip().upper()

if purchase_total < 0.0 or student_upper not in valid_answers or senior_upper not in valid_answers:
    print("Error: entrada inválida")
else:
    is_student = student_upper == "YES"
    is_senior = senior_upper == "YES"
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    final_total = purchase_total * 0.9 if discount_eligible else purchase_total

    print("Elegible para descuento:", discount_eligible)
    print("Total final:", final_total)

# Problem 3 Code - Border Case
print("\n--- Problema 3: Caso Borde ---")
purchase_total = 1000.0
is_student_text = "NO"
is_senior_text = "NO"

print("Total de compra de entrada:", purchase_total)
print("Es estudiante (entrada):", is_student_text)
print("Es adulto mayor (entrada):", is_senior_text)

student_upper = is_student_text.strip().upper()
senior_upper = is_senior_text.strip().upper()

if purchase_total < 0.0 or student_upper not in valid_answers or senior_upper not in valid_answers:
    print("Error: entrada inválida")
else:
    is_student = student_upper == "YES"
    is_senior = senior_upper == "YES"
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    final_total = purchase_total * 0.9 if discount_eligible else purchase_total

    print("Elegible para descuento:", discount_eligible)
    print("Total final:", final_total)


# PROBLEM 4: Basic statistics of three integers

"""
Problem 4: Basic statistics of three integers
Description:
Reads three integer values and calculates their sum, average, maximum, 
minimum, and checks if all three numbers are even.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- Input integers: <n1>, <n2>, <n3>
- Sum: <sum_value>
- Average: <average_value>
- Max: <max_value>
- Min: <min_value>
- All even: true|false

Validations:
- Validate integer values.

Test cases:
1) Normal: n1 = 4, n2 = 8, n3 = 12 -> Sum: 24, Average: 8.0, Max: 12, Min: 4, All even: True
2) Border: n1 = 0, n2 = 2, n3 = 3 -> Sum: 5, Average: 1.666..., Max: 3, Min: 0, All even: False
"""

# Problem 4 Code - Normal Case
print("\n--- Problema 4: Caso Normal ---")
n1, n2, n3 = 4, 8, 12

print(f"Enteros de entrada: n1={n1}, n2={n2}, n3={n3}")

sum_value = n1 + n2 + n3
average_value = sum_value / 3.0
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

print("Suma:", sum_value)
print("Promedio:", average_value)
print("Máximo:", max_value)
print("Mínimo:", min_value)
print("Todos pares:", all_even)

# Problem 4 Code - Border Case
print("\n--- Problema 4: Caso Borde ---")
n1, n2, n3 = 0, 2, 3

print(f"Enteros de entrada: n1={n1}, n2={n2}, n3={n3}")

sum_value = n1 + n2 + n3
average_value = sum_value / 3.0
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

print("Suma:", sum_value)
print("Promedio:", average_value)
print("Máximo:", max_value)
print("Mínimo:", min_value)
print("Todos pares:", all_even)



# PROBLEM 5: Loan eligibility (income and debt ratio)

"""
Problem 5: Loan eligibility (income and debt ratio)
Description:
Evaluates loan eligibility based on monthly income, monthly debt, and credit score. 
Calculates debt ratio and verifies all requirements.

Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Outputs:
- Input monthly income: <monthly_income>
- Input monthly debt: <monthly_debt>
- Input credit score: <credit_score>
- Debt ratio: <debt_ratio>
- Eligible: true|false

Validations:
- monthly_income > 0.0 (prevent division by zero)
- monthly_debt >= 0.0
- credit_score >= 0

Test cases:
1) Normal: monthly_income = 10000.0, monthly_debt = 2000.0, credit_score = 700 -> Debt ratio: 0.2, Eligible: True
2) Border: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650 -> Debt ratio: 0.4, Eligible: True
"""

# Problem 5 Code - Normal Case
print("\n--- Problema 5: Caso Normal ---")
monthly_income = 10000.0
monthly_debt = 2000.0
credit_score = 700

print("Ingreso mensual de entrada:", monthly_income)
print("Deuda mensual de entrada:", monthly_debt)
print("Puntaje de crédito de entrada:", credit_score)

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: entrada inválida")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    print("Relación de deuda:", debt_ratio)
    print("Elegible:", eligible)

# Problem 5 Code - Border Case
print("\n--- Problema 5: Caso Borde ---")
monthly_income = 8000.0
monthly_debt = 3200.0
credit_score = 650

print("Ingreso mensual de entrada:", monthly_income)
print("Deuda mensual de entrada:", monthly_debt)
print("Puntaje de crédito de entrada:", credit_score)

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: entrada inválida")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    print("Relación de deuda:", debt_ratio)
    print("Elegible:", eligible)


# PROBLEM 6: Body Mass Index (BMI) and category flag

"""
Problem 6: Body Mass Index (BMI) and category flag
Description:
Calculates Body Mass Index (BMI) given weight and height, rounding to 2 decimals, 
and sets categorical flags for underweight, normal, or overweight status.

Inputs:
- weight_kg (float)
- height_m (float)

Outputs:
- Input weight (kg): <weight_kg>
- Input height (m): <height_m>
- BMI: <bmi>
- Underweight: true|false
- Normal: true|false
- Overweight: true|false

Validations:
- weight_kg > 0.0
- height_m > 0.0

Test cases:
1) Normal: weight_kg = 70.0, height_m = 1.75 -> BMI: 22.86, Underweight: False, Normal: True, Overweight: False
2) Border: weight_kg = 72.0, height_m = 1.70 -> BMI: 24.91, Underweight: False, Normal: True, Overweight: False
"""

# Problem 6 Code - Normal Case
print("\n--- Problema 6: Caso Normal ---")
weight_kg = 70.0
height_m = 1.75

print("Peso (kg) de entrada:", weight_kg)
print("Estatura (m) de entrada:", height_m)

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: entrada inválida")
else:
    bmi_raw = weight_kg / (height_m ** 2)
    bmi = round(bmi_raw, 2)
    is_underweight = bmi < 18.5
    is_normal = (18.5 <= bmi) and (bmi < 25.0)
    is_overweight = bmi >= 25.0

    print("IMC (BMI):", bmi)
    print("Bajo peso:", is_underweight)
    print("Peso normal:", is_normal)
    print("Sobrepeso:", is_overweight)

# Problem 6 Code - Border Case
print("\n--- Problema 6: Caso Borde ---")
weight_kg = 72.0
height_m = 1.70

print("Peso (kg) de entrada:", weight_kg)
print("Estatura (m) de entrada:", height_m)

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: entrada inválida")
else:
    bmi_raw = weight_kg / (height_m ** 2)
    bmi = round(bmi_raw, 2)
    is_underweight = bmi < 18.5
    is_normal = (18.5 <= bmi) and (bmi < 25.0)
    is_overweight = bmi >= 25.0

    print("IMC (BMI):", bmi)
    print("Bajo peso:", is_underweight)
    print("Peso normal:", is_normal)
    print("Sobrepeso:", is_overweight)


"""
===============================================================================
CONCLUSIONS
===============================================================================
Combining integer (int) and floating-point (float) data types enables precise 
modeling of both discrete and continuous domain quantities in software engineering. 
Generating boolean flags through relational comparisons and logical operators 
(and, or, not) streamlines conditional evaluation and structured decision-making. 
Validating input values is essential to safeguard application stability by avoiding 
unhandled exceptions like division by zero or domain-invalid inputs. These logical 
patterns form the core foundations for developing real-world automated systems.
===============================================================================
"""

"""
===============================================================================
REFERENCES
===============================================================================
1) Python Software Foundation. (2024). Built-in Types: Numeric Types — int, float. 
   Python Documentation. https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
2) Python Software Foundation. (2024). Boolean Values — bool. 
   Python Documentation. https://docs.python.org/3/library/stdtypes.html#boolean-values
3) Python Software Foundation. (2024). Built-in Functions: round(), min(), max(). 
   Python Documentation. https://docs.python.org/3/library/functions.html
4) Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.
5) Severance, C. (2016). Python for Everybody: Exploring Data in Python 3. CreateSpace Independent Publishing Platform.
===============================================================================
"""