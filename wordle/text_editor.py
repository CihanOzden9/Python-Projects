import pyfiglet
from colorama import Fore, Back, Style, init

WORD_LEN = 5

init(autoreset=True) # Renk ayarlarını sıfırlama
fig = pyfiglet.Figlet(font="slant")

COLOR_MAP = {
    1: Fore.GREEN,
    0: Fore.CYAN,
   -1: Fore.RED,
}


def text(text, color):
    text = text.upper()
    art = pyfiglet.figlet_format(text,font="big") #Yazıyı consol textine dönüştür
    color = color.upper() #Gelen rengi method için upper yap
    fore_color = getattr(Fore, color, Fore.WHITE)  # geçersiz renk olursa beyaz kullan
    return fore_color + art



def input_word(ctrl_list, word):
    """
        kullanıcıdan gelen texte göre çıktı verecek
        Ctrl değişkeni -1 0 1 olabilir
        -1 yanlış; kırmızı
        0 Doğru ama yeri yanlış; cyan
        1 Yeride doğru; Yeşil
    """
    if all(x == 1 for x in ctrl_list):
        return 1

    assert len(ctrl_list) == len(word), "ctrl_list ve word uzunlukları eşit olmalı"

    # Her harfi render edip satırlara böl
    rendered = []
    for ch, ctrl in zip(word, ctrl_list):
        art = fig.renderText(ch)                 # çok satırlı string
        lines = art.splitlines()                 # satır listesi
        color = COLOR_MAP.get(ctrl, Fore.WHITE)  # varsayılan beyaz
        # Rengi satıra uygula (birleştirirken sorun çıkmasın)
        colored_lines = [color + ln + Style.RESET_ALL for ln in lines]
        rendered.append(colored_lines)

    # En uzun harfin satır sayısını referans al
    max_rows = max(len(x) for x in rendered)

    # Satır satır yan yana birleştir
    combined_lines = []
    for row in range(max_rows):
        parts = []
        for letter_lines in rendered:
            # Son satır kontrolü
            ln = letter_lines[row] if row < len(letter_lines) else ""
            parts.append(ln)
        combined_lines.append("  ".join(parts))  # harfler arası boşluk ayarlama

    print("\n".join(combined_lines))
    






