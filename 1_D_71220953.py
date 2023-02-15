print('========== MAKANAN ==========')
print('1. Telur Bakar\t   : Rp. 7.000')
print('2. Lele Terbang\t : Rp. 10.000')
print('3. Es Coklat\t    : Rp. 5.000')
print('4. Es Doger\t: Rp. 13.000')

tbkr = 7000
lelet = 10000
cklt = 5000
doger = 13000
print('')

print('========= Pesanan ==========')
jtbkr = int(input('Telur Bakar\t : '))
jelelt = int(input('Lele Terbang\t : '))
jcklt = int(input('Es Coklat\t : '))
jdoger = int(input('Es Doger\t : '))

total_telur = tbkr * jtbkr
total_lele = lelet * jelelt
total_coklat = cklt * jcklt
total_doger = doger * jdoger
hasil = total_telur + total_lele + total_coklat + total_doger

print('========== TOTAL ==========')
print(f'TOTAL TELUR BAKAR x {jtbkr}\t : Rp. {total_telur}')
print(f'TOTAL LELE TERBANG x {jelelt}\t : Rp. {total_lele}')
print(f'TOTAL ES COKLAT x {jcklt}\t : Rp. {total_coklat}')
print(f'TOTAL ES DOGER x {jdoger}\t : Rp. {total_doger}')



print('Jumlah total biaya yang harus dibayar adalah', hasil)
