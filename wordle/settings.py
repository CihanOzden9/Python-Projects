import get_words
import text_editor 
import pandas as pd

WORD_LEN = 5

get_words.game_settings() #Oyun başlarken kelime ayarları yapılsın
word = get_words.get_word() # Oyun kelimesi seç
word = list(word)

health = WORD_LEN

print(text_editor.text("Start game","white"))
print("""
=== OYUN KURALLARI ===
1- Kelime 5 harflidir.
2- Her tahminde doğru harfler renkle gösterilir:
   - Yeşil: Doğru yerde
   - Cyan: Kelimede var ama yeri yanlış
   - Kırmızı: Kelimede yok
3- 5 hakkın var!
4- ş,ç,ğ harfleri yok.
======================
""")


while health > 0:
    
    color_map = []
    """
        Kelimeyi al
        Color map oluştur liste olarak döndür
        kullanıcıdan girilen kelimeyi ve mapi text_editör e gönder
    
    """
    user_word = input("tahmin; ")
    if len(user_word) != 5:
        print("--- Geçerli bir kelime giriniz ---")
        continue
    else:
        health -= 1
        user_word = list(user_word.lower())

        for i in range(WORD_LEN):
            if user_word[i] == word[i]:
                color_map.append(1)
            elif user_word[i] in word:
                color_map.append(0) 
            else:
                color_map.append(-1)

        output = text_editor.input_word(color_map,"".join(user_word))
        if output:
            print(text_editor.text("".join(word),"green"))
            print(text_editor.text("tebrikler","white"))
            break

print("--- Kaybettiniz ---")
word = " ".join(word)
print(f"kelime; {word}")
