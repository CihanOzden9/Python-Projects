
"""
    Her tuşa bastığında girilen harfler bir listeye atılır
    listedeki elemanlar birleştirilip ascıı art formatına dönüştürülür
    Consola listedeki elemanlar yazılır
    Alt kısmına art yapılır
"""
import msvcrt
import pyfiglet
import os

print("Yazmaya başla... (q ile çık)")
text_list = []

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        # BACKSPACE
        if key == b'\x08':
            if text_list:
                text_list.pop()
            # İşlem bitti → yeniden çiz
        else:
            ch = key.decode(errors="ignore")
            text_list.append(ch)

            if ch == "q":
                break

        # Ekranı **işlemden SONRA** temizle
        os.system('cls' if os.name=="nt" else 'clear')

        # Yeni metni oluştur
        text = "".join(text_list)
        art = pyfiglet.figlet_format(text, font="big")
        print(text)
        print(art)
