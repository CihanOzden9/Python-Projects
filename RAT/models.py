import sqlite3 as sql
import datetime as dt


DB_NAME = "rentatech.db"

#Kategoriler sınıfı
class Categories:
    #Veri tabanı bağlantısı
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_tables()

    #Kategoriler tablosu oluştur
    def create_tables(self):
        with sql.connect(self.db_name) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT)")

    #Kategori ekle
    def add_category(self, cat_name):
        with sql.connect(self.db_name) as conn:
            conn.execute("INSERT INTO categories (name) VALUES (?)", (cat_name,))


#Ürünler sınıfı
class Products:
    # Veri tabanı bağlantısı
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_tables()
    #ürünler tablosu oluştur
    def create_tables(self):
        with sql.connect(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    cat_id INTEGER,
                    name TEXT,
                    hourly_rate INTEGER,
                    is_active INTEGER,
                    owner_id INTEGER NOT NULL,
                    FOREIGN KEY (cat_id) REFERENCES categories (id)
                )""")
    #Ürün ekleme methodu
    def add_product(self, cat_id, name, hourly_rate, owner_id):
        with sql.connect(self.db_name) as conn:
            query = "INSERT INTO products (cat_id, name, hourly_rate, is_active, owner_id) VALUES (?, ?, ?, 1, ?)"
            conn.execute(query, (cat_id, name, hourly_rate, owner_id))

#Kullanıcılar sınıfı
class Users:
    #veri tabanı bağlantısı
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_tables()
    
    #Tablo oluşturma
    def create_tables(self): 
        with sql.connect(self.db_name) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    user_name TEXT UNIQUE,
                    password TEXT, -- Yeni eklenen alan
                    user_type INTEGER, 
                    gender INTEGER,
                    created_at DATETIME)""")

    def register(self, user_name, password, user_type, gender):
        # Veri hazırlığı
        created_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        params = (user_name, password, user_type, gender, created_at)
        
        query = """
                    INSERT INTO users (user_name, password, user_type, gender, created_at) 
                    VALUES (?, ?, ?, ?, ?)
                """

        try:
            with sql.connect(self.db_name) as conn:
                conn.execute(query, params)
                print(f" [+] '{user_name}' başarıyla kaydedildi.")
                return True
        except sql.IntegrityError:
            print(f" [!] Hata: '{user_name}' kullanıcı adı zaten kullanımda.")
            return False
        except Exception as e:
            print(f" [!] Beklenmedik hata: {e}")
            return False

    #Kullanıcı giriş.
    def login(self, user_name, password):
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Hem isim hem şifre eşleşmeli
            cursor.execute("SELECT id, user_type FROM users WHERE user_name = ? AND password = ?", 
                        (user_name, password))
            user = cursor.fetchone()
            
            if user:
                return user  # Başarılı: (id, type)
            return None      # Hatalı giriş


#Kira durumu sınıfı
class Rentals:
    def __init__(self, db_name = DB_NAME):
        self.db_name = db_name
        self.create_table()

    #Tablo oluşturma
    def create_table(self):
        with sql.connect(self.db_name) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS rental(
                         id INTEGER PRIMARY KEY,
                         user_id INTEGER,
                         product_id INTEGER,
                         start_time DATETIME,
                         end_time DATETIME,
                         total_price REAL,
                         status TEXT,
                         FOREIGN KEY (user_id) REFERENCES users (id),
                         FOREIGN KEY (product_id) REFERENCES products (id))""")
            
    def rent_product(self, user_id, product_id, hours):
        with sql.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # 1. Ücreti çek
            cursor.execute("SELECT hourly_rate FROM products WHERE id = ?", (product_id,))
            rate = cursor.fetchone()[0]
            
            # 2. Hesaplamalar
            total_price = rate * hours
            start_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end_time = (dt.datetime.now() + dt.timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M:%S")
            
            # 3. Kaydet
            cursor.execute("""INSERT INTO rental (user_id, product_id, start_time, end_time, total_price, status) 
                            VALUES (?, ?, ?, ?, ?, 'Aktif')""", 
                            (user_id, product_id, start_time, end_time, total_price))
            
            # 4. Ürünü pasife çek (Kiralandı olarak işaretle)
            cursor.execute("UPDATE products SET is_active = 0 WHERE id = ?", (product_id,))
            print(f" [+] Kiralama başarılı. Toplam Tutar: {total_price}")