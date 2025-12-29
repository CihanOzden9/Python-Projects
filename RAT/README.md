# Rent A Tech - Python Ürün Kiralama Sistemi

Bu proje, teknolojik ürünlerin saatlik olarak kiralanmasını sağlayan bir envanter yönetim ve kiralama sistemi simülasyonudur.

## 🚀 Özellikler
- **Kullanıcı Yönetimi:** Kayıt olma ve Admin/Standart kullanıcı girişi.
- **Kategori Sistemi:** Ürünleri kategorize etme ve dinamik kategori ekleme.
- **Ürün Yönetimi:** Adminler için ürün ekleme ve aktiflik kontrolü.
- **Kiralama Mantığı:** Saatlik ücret üzerinden otomatik tutar hesaplama.
- **Yetkilendirme:** Role göre (Admin/User) farklı menü erişimleri.

## 📁 Dosya Yapısı
- `main.py`: Uygulamanın giriş noktası ve menü döngüsü.
- `models.py`: Veritabanı tablo sınıfları (Users, Products, Rentals).
- `utils.py`: Yardımcı fonksiyonlar (Hesaplamalar, ekran temizleme).
- `rentatech.db`: SQLite veritabanı dosyası.

## 🛠 Kurulum ve Çalıştırma
1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/kullaniciadi/rent-a-tech.git](https://github.com/kullaniciadi/rent-a-tech.git)