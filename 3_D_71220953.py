listbrand = input('Brand yang hendak dibeli (pisahkan dengan koma): ')
brand_split = listbrand.split(',')

b1 = brand_split[0]
b2 = brand_split[1]
b3 = brand_split[2]
b4 = brand_split[3]

a1 = int(input(f'Berapa harga barang {b1}? : '))
if a1 >= 25000000:
    print(f'Harga {b1}\t Rp {a1}\t diskon Rp. {(25/100)*(a1)}')
elif a1 >= 10000000:
    print(f'Harga {b1}\t Rp {a1}\t diskon Rp. {(10/100)*(a1)}')
else:
    print(f'Harga {b1}\t Rp {a1}\t diskon Rp. 0')

a2 = int(input(f'Berapa harga barang {b2}? : '))
if a2 >= 25000000:
    print(f'Harga {b2}\t Rp {a2}\t diskon Rp. {(25/100)*(a2)}')
elif a2 >= 10000000:
    print(f'Harga {b2}\t Rp {a2}\t diskon Rp. {(10/100)*(a2)}')
else:
    print(f'Harga {b2}\t Rp {a2}\t diskon Rp. 0')

a3 = int(input(f'Berapa harga barang {b3}? : '))
if a3 >= 25000000:
    print(f'Harga {b3}\t Rp {a3}\t diskon Rp. {(25/100)*(a3)}')
elif a3 >= 10000000:
    print(f'Harga {b3}\t Rp {a3}\t diskon Rp. {(10/100)*(a3)}')
else:
    print(f'Harga {b3}\t Rp {a3}\t diskon Rp. 0')

a4 = int(input(f'Berapa harga barang {b4}? : '))
if a4 >= 25000000:
    print(f'Harga {b4}\t Rp {a4}\t diskon Rp. {(25/100)*(a4)}')
elif a4 >= 10000000:
    print(f'Harga {b4}\t Rp {a4}\t diskon Rp. {(10/100)*(a4)}')
else:
    print(f'Harga {b4}\t Rp {a4}\t diskon Rp. 0')

print(f'Total diskon yang anda dapatkan adalah sebesar: Rp. {(0)+(a2*25/100)+(a3*10/100)+(a4*25/100)}')
hasil = print('Total uang yang harus anda bayarkan adalah: Rp.', (a1+a2+a3+a4)-((0)+(a2*25/100)+(a3*10/100)+(a4*25/100)))