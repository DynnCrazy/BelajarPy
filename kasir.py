data_barang = [
    {
        "id": "1",
        "nama": "Roti",
        "harga": "3000",
        "diskon": ""
    },
    {
        "id": "2",
        "nama": "Buku tulis",
        "harga": "2000",
        "diskon": ""
    },
    {
        "id": "3",
        "nama": "Pensil",
        "harga": "2000",
        "diskon": ""
    },
    {
        "id": "4",
        "nama": "Pulpen",
        "harga": "2000",
        "diskon": ""
    },
    {
        "id": "5",
        "nama": "Penghapus",
        "harga": "1000",
        "diskon": ""
    }
]

matauang = "Rp."
numsamadengan = int("36")

print("=" * numsamadengan)
print(f"{'Nama'.ljust(15)} {'ID'.center(5)} {'Harga'.rjust(10)}")
print("=" * numsamadengan)

for barang in data_barang:
    if barang['diskon']:
        print(f"{barang['nama'].ljust(15)} {barang['id'].center(5)} {matauang.rjust(8)} {int(barang['harga']) - ( (int(barang['harga']) * ( int(barang['diskon'])) / 100 ) ):,.0f}")
    else:
        print(f"{barang['nama'].ljust(15)} {barang['id'].center(5)} {matauang.rjust(8)} {int(barang['harga']):,.0f}")

print("\n")

def cariBarang(barang_id):
    for idbarang in data_barang:
        if int(barang_id) == int(idbarang['id']):
            return idbarang #['id']
    return None

idBarangDiKeranjang = []
jumlahBarangDiKeranjang = []

while True:
    barang_id = str(input("Masukan ID barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): "))

    if barang_id.lower() == "0":
        break

    barang = cariBarang(barang_id)
    
    if barang:
        idBarangDiKeranjang.append(barang)
        barang_jumlah = str(input("Masukan jumlah barang yang ingin dibeli: "))
        jmlh_barang = int(barang_jumlah)
        if jmlh_barang >= 10:
            print("Barang yang tersedia tidak cukup! mohon membeli kurang dari 10")
            jumlahBarangDiKeranjang.append(str(0))
        elif jmlh_barang <= 0:
            print("Jumlah barang tidak boleh minus (-) atau 0")
            jumlahBarangDiKeranjang.append(str(0))
        else:
            jumlahBarangDiKeranjang.append(str(barang_jumlah))
    else:
        print("Barang tidak ditemukan!")

total_bayar = 0
print("\nBarang yang ada di keranjang:")

for index, barang in enumerate(idBarangDiKeranjang):
    jumlah = int(jumlahBarangDiKeranjang[index])
    if barang['diskon']:
        harga_setelah_diskon = int(barang['harga']) - (int(barang['harga']) * int(barang['diskon']) / 100)
        total_harga = jumlah * harga_setelah_diskon
        print(f"{barang['nama'].ljust(11)} ({jumlah}) | {matauang} {int(total_harga):,.0f}")
        total_bayar += total_harga
    else:
        total_harga = jumlah * int(barang['harga'])
        print(f"{barang['nama'].ljust(11)} ({jumlah}) | {matauang} {total_harga:,.0f}")
        total_bayar += total_harga

print("=" * numsamadengan)
print(f"{'Total'.ljust(15)} | {matauang} {total_bayar:,.0f}")
print("\n")