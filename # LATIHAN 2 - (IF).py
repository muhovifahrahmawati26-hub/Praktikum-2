# LATIHAN 2 - (IF)
print("Mengurutkan 3 bilangan dari kecil ke besar")

a = int(input("Bilangan ke-1: "))
b = int(input("Bilangan ke-2: "))
c = int(input("Bilangan ke-3: "))

# logika pengurutan manual dengan if
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Urutan bilangan:", a, b, c)