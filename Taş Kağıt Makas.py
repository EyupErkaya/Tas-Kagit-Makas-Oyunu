import random

def oyun():
    can = 3
    puan = 0
    kazanma = 0
    kaybetme = 0
    berabere = 0

    game = ["tas", "kagit", "makas"]

    while can != 0:
        x = random.randint(0, 2)
        pc_hamle = game[x]
        hamle = input("Tas, kagit, makas? (Çıkmak için 'q' ya basın)\n").lower()

        if hamle == 'q':
            print("Oyundan çıkılıyor...")
            break
        
        if hamle not in game:
            print("Geçersiz giriş! Lütfen 'tas', 'kagit' veya 'makas' yazınız.")
            continue

        print(f"Bilgisayarın hamlesi: {pc_hamle}")

        if pc_hamle == hamle:
            berabere += 1
            print("Berabere!")
        elif hamle == "tas":
            if pc_hamle == "kagit":
                can -= 1
                kaybetme += 1
                print(f"Kaybettiniz, {can} canınız kaldı!")
            else:
                puan += 10
                kazanma += 1
                print("Tebrikler! 10 puan kazandınız!")
        elif hamle == "kagit":
            if pc_hamle == "makas":
                can -= 1
                kaybetme += 1
                print(f"Kaybettiniz, {can} canınız kaldı!")
            else:
                puan += 10
                kazanma += 1
                print("Tebrikler! 10 puan kazandınız!")
        elif hamle == "makas":
            if pc_hamle == "tas":
                can -= 1
                kaybetme += 1
                print(f"Kaybettiniz, {can} canınız kaldı!")
            else:
                puan += 10
                kazanma += 1
                print("Tebrikler! 10 puan kazandınız!")
        
        if puan >= 50:
            can += 1
            puan -= 50
            print("50 puan kazandınız, 1 can kazandınız!")

    print("Oyun bitti!")
    print(f"Toplam {puan} puan kazandınız.")
    print(f"Kazandığınız oyun sayısı: {kazanma}")
    print(f"Kaybettiğiniz oyun sayısı: {kaybetme}")
    print(f"Berabere kaldığınız oyun sayısı: {berabere}")

while True:
    basla = input("Oyuna başlamak ister misiniz? (Evet/Hayır): ").lower()
    if basla == "evet":
        oyun()
    elif basla == "hayır":
        print("Oyundan çıkılıyor...")
        break
    else:
        print("Lütfen 'Evet' veya 'Hayır' olarak cevap verin.")
