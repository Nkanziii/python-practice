def multiply(a: int, b: int) -> int:
    return a * b

def get_initials(name: str) -> str:
    return name[0].upper()

#print(multiply(3, 8))
#print(get_initials())

def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

print(add(2, 4))

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Returns the BMI"""
    return round(weight_kg / (height_m * height_m), 2)

print(calculate_bmi(55.5, 1.58))