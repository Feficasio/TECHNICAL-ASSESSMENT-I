def deret_aritmatika(n):
    # Input Dengan Angka pertama 4, dan selisih 3
    start = 2
    difference = 3
    deret = []

    for i in range(n):
        deret.append(start)
        start += difference

    return deret

n = int(input("Masukkan Jumlah Deret: "))
hasil = deret_aritmatika(n)
print("Output:", ','.join(map(str, hasil)))