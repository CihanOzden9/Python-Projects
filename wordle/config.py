import get_words
import text_editor 


def game_start():
    get_words.game_settings() #Oyun başlarken kelime ayarları yapılsın
    word = get_words.get_word() # Oyun kelimesi seç
    word = list(word)
    WORD_LEN = 5
    health = WORD_LEN
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
                health += 1
                break

    if health == 0:
        print("--- Kaybettiniz ---")
        word = " ".join(word)
        print(f"kelime; {word}")
    res =  restart()
    return res

def restart():
    print("==========")
    print("Yeniden başlamak için \"1\"\nÇıkmak için \"q\"")
    r = input("\n")
    if r == "q":
        return 0
    elif r == "1":
        return 1
    else:
        print("--- Lütfen geçerli bir işlem girin! ---")
        restart()