import random

dt_bool = []
taruhan = ""
jumlahSpin = 0

def inputTaruhan():
    global taruhan, jumlahSpin
    taruhan = input("Masukan taruhan: ")
    jumlahSpin += 1

while True: 
    inputTaruhan()

    if jumlahSpin == 0:
        dt_bool = ["true", "true", "true", "true", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false"]
    elif jumlahSpin >= 1 and jumlahSpin <= 5:
        dt_bool = ["false", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false"]
    elif jumlahSpin >= 6 and jumlahSpin <= 10:
        dt_bool = ["false", "false", "false", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false"]
    else:
        dt_bool = ["false", "false", "false", "false", "false", "true", "false", "true", "false", "true", "false", "true", "false", "true", "false"]

    isHoki = random.choice(dt_bool)

    if isHoki == "true":
        dt_num = ["1.1", "1.1", "1.1", "1.1", "1.1", "1.1", "1.1", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2", "1.3", "1.3", "1.3", "1.3", "1.3", "1.4", "1.4", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "2.0", "3.0", "5.0"]
        kaliBerapa = random.choice(dt_num)

        untung = int(taruhan) * float(kaliBerapa)

        keuntungan = int(untung) - int(taruhan)
        
        print(f"You Win! dengan keuntungan Rp. {keuntungan:,.0f}")
    else:
        print("You Lose")