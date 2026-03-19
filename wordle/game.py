import config as config
import text_editor
import os
import sys

def rules():
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

def start():
    os.system('cls' if os.name=="nt" else 'clear')
    print(text_editor.text("wordle game","white"))
    rules()
    ctrl = config.game_start()
    if ctrl:
        start()
    
start()