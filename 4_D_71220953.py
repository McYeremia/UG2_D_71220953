while True:
    print('\t !! Selamat datang di H+ GYM !!')
    print('Silahkan pilih menu dibawah ini: \n 1. Menambah data \n 2. Menampilkan data \n 3. Keluar')
    pil1 = int(input('Silahkann masukan pilihan yang anda inginkan: '))
    
    if pil1 == 1:
        pel= (input('Masukan Nama Pelanggan:'))
        mem =(input('Masukan Jenis Member: '))
        print('Data berhasil ditambahkan!')
    elif pil1 == 2:
        print(f'Pelanggan\t Member: \n {pel}\t {mem}')

    elif pil1 == 3:
        print('Sistem Berhenti')
        break
