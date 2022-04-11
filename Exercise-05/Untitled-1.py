mahasiswa = [["joko yulianto" "jl. elang no 5" "123456"], 
            ["anwar wibowo" "jl. megamendung 4" "4567890"]]
alamat_mahasiswa = ''' 
    nama mahasiwa   \t:{0},
    alamat rumah    \t:{1},
    no telp         \t:{2},
    '''
#program utama
print("daftar mahasiswa TI UNS")
print("=======================")

for indeks in range (len(mahasiswa)):
    print(alamat_mahasiswa.format(mahasiswa[indeks][0],
                                  mahasiswa[indeks][1],
                                  mahasiswa[indeks][2]))
print()
print("==============================")
