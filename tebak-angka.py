import random

angkaRahasia = int(random.randint(1, 100))

print('Tebak Angka 1-100!')

while True:
    try:
        userInput = int(input('Masukan jawaban anda!'))

        if isinstance(userInput, int) and len(str(userInput)) <= 3 and int(userInput) <= 100 and int(userInput) >= 0:
            if userInput > angkaRahasia:
                print('Terlalu tinggi!')
            elif userInput < angkaRahasia:
                print('Terlalu rendah')
            else:
                print('Kamu Benar!')
                break
        else:
            print('Terjadi kesalahan dalam input!')
    except ValueError:
        print('Terjadi kesalahan dalam input!')
