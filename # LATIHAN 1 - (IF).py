# LATIHAN 1 - (IF)
print("Menentukan bilangan terbesar dari 4 bilangan")

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

terbesar = a

if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

print("Bilangan terbesar adalah:", terbesar)