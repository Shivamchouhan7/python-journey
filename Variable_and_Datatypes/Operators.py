# All types of operators in python 


# 1. Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor Division



# 2. Assignment Operators

x = 5
print("\nAssignment Operators")

x += 3
print("x += 3 ->", x)

x -= 2
print("x -= 2 ->", x)

x *= 4
print("x *= 4 ->", x)

x //= 3
print("x //= 3 ->", x)



# 3. Comparison (Relational) Operators

p = 10
q = 20

print("\nComparison Operators")
print("p == q ->", p == q)
print("p != q ->", p != q)
print("p > q  ->", p > q)
print("p < q  ->", p < q)
print("p >= q ->", p >= q)
print("p <= q ->", p <= q)



# 4. Logical Operators

a = True
b = False

print("\nLogical Operators")
print("a and b ->", a and b)
print("a or b  ->", a or b)
print("not a   ->", not a)



# 5. Bitwise Operators

x = 5   # 0101
y = 3   # 0011

print("\nBitwise Operators")
print("x & y ->", x & y)   # AND
print("x | y ->", x | y)   # OR
print("x ^ y ->", x ^ y)   # XOR
print("~x    ->", ~x)      # NOT
print("x << 1 ->", x << 1) # Left Shift
print("x >> 1 ->", x >> 1) # Right Shift



# 6. Membership Operators

data = [10, 20, 30, 40]

print("\nMembership Operators")
print("20 in data ->", 20 in data)
print("50 not in data ->", 50 not in data)



# 7. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nIdentity Operators")
print("a is b ->", a is b)
print("a is c ->", a is c)
print("a is not c ->", a is not c)
