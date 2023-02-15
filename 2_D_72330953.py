edigit = str(input('Masukan Nomor Telepon(12 Digit):'))
edigit2 = int(edigit)
if edigit >= ('081700000000'):
    print('Operator anda tidak diketahui')
elif edigit < ('081400000000'):
    print('Operator anda tidak diketahui')
elif edigit < ('081500000000'):
    print('anda menggunakan operator Telkomsel')
elif edigit < ('081700000000'):
    print('anda menggunakan operator Indosat')

if (edigit2/2) == ('1'):
    print('Nomor anda berakhiran genap')
else:
    print('Nomor anda berakhiran ganjil')