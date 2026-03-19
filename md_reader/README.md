# Markdown Reader Pro v6.0

Modern ve şık bir arayüze sahip, açık/koyu tema destekli profesyonel bir Markdown görüntüleyici masaüstü uygulamasıdır. PyQt6 kullanılarak geliştirilmiştir ve Markdown dosyalarınızı GitHub tarzı özel bir CSS tasarımıyla oluşturur.

## 🚀 Özellikler

* **Karanlık / Aydınlık Tema Desteği:** Tek tıklamayla göz yormayan karanlık veya daha ferah aydınlık temalar arasında geçiş yapabilirsiniz.
* **Modern Arayüz:** Sade, kullanıcı dostu ve akıcı bir okuma deneyimi sunan GitHub stili CSS tasarımı.
* **Geniş Markdown Özellikleri:** Tablolar, kod blokları (renklendirme), listeler, içindekiler tablosu (TOC) ve daha fazlası desteklenir.
* **Hızlı Görüntüleme:** Dosya seçici ile bilgisayarınızdaki `.md` uzantılı dosyaları kolayca açın ve anında görüntüleyin.

## 🛠️ Gereksinimler

Projeyi çalıştırabilmek için bilgisayarınızda Python 3.x ve aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

* `PyQt6` (Arayüz için)
* `Markdown` (Markdown dosyasını HTML'e dönüştürmek için)

Gerekli paketleri kurmak için:

```bash
pip install PyQt6 Markdown
```

## 💻 Kullanım

Projeyi bilgisayarınıza indirdikten sonra, terminal veya komut istemcisi üzerinden proje klasörüne gidin ve aşağıdaki komutu çalıştırın:

```bash
python md_viewer.py
```

1. Uygulama açıldığında üst kısımdaki **"📂 Dosya Aç"** butonuna tıklayarak bilgisayarınızdan bir `.md` dosyası seçebilirsiniz.
2. Sağ üst köşedeki mod butonunu kullanarak tema geçişi yapabilirsiniz.

## 🗂️ Proje Dosyaları

* `md_viewer.py` : Ana uygulama kütüphanesi ve UI bileşenlerini içerir.
* `README.md` : Proje tanıtım ve kullanım dosyası (Bu dosya).
