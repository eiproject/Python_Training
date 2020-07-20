# Basic print
print("Hello World")

# Basic variable
A = 1
B = 2
C = A + B
print(C)

# Basic string
A = '1'
B = '2'
C = A + B
print(C)

# basic conversion
A = '1'
B = 2
C = A + str(B)
print(C)

# Operasi aritmatika
A = 10
B = 3
print(A+B, A-B, A*B,
      A/B, A//B, A%B, A**B)
# Penjumlahan, Pengurangan, Perkalian,
# Pembagian, Pembagian (pembulatan ke bawah), Modulus, Pangkat dua

# Basic List
A = (1, 2, 3)
B = (4, 5, 6)
C = A + B
print(C)

# Call from list
A = ('ayam', 'telur', 'kucing', 'ikan')
ambil_data = A[1]
print(ambil_data)

# Input and if else statement
x = int(input("Masukkan angka mu = "))
if x%2==0:
    print('genap')
else:
    print("ganjil")

# Looping while
num = 0
while True:
    if num>10:
        break
    else:
        print(num)
        num+=1

# Looping for
A = ('ayam', 'telur', 'kucing', 'ikan')
for i in A:
    print(A)

# Latihan
# Looping untuk hitung faktorial
number = int(input("Masukkan angka yang akan dihitung : "))
result = 1
for i in range(number):
    result = result*(i+1)

print(result)
