import random
import string

# --- Sabitler ---
# Şifrelenecek karakterler (küçük harfler ve rakamlar)
ORIJINAL_KARAKTERLER = list(string.ascii_lowercase + string.digits + ' ') # Boşluk da dahil

# --- Şifreleme Kuralları Veritabanı ---
# Burası rastgele oluşturulacak kuralları tutacak.
SIFRELEME_KURALLARI = {}

def rastgele_sifreleme_kurali_olustur():
    """
    Belirli karakterler için rastgele bir yerine koyma şifreleme kuralı oluşturur.
    Her çağırdığında farklı bir kural döndürür.
    """
    sifreli_kural = {}
    
    # Orijinal karakterlerin bir kopyasını alıp karıştır
    karistirilmis_karakterler = list(ORIJINAL_KARAKTERLER)
    random.shuffle(karistirilmis_karakterler)

    # Her orijinal karaktere karşılık gelen rastgele bir şifreli karakter ata
    for i, orijinal_karakter in enumerate(ORIJINAL_KARAKTERLER):
        sifreli_kural[orijinal_karakter] = karistirilmis_karakterler[i]
        
    return sifreli_kural

# --- 999 Adet Kuralı Oluşturma ---
print("999 adet şifreleme kuralı oluşturuluyor...")
for i in range(1, 1000): # 1'den 999'a kadar ID'ler için
    sifreleme_id = f"{i:03d}" # ID'yi 001, 002... 999 formatında yap
    SIFRELEME_KURALLARI[sifreleme_id] = rastgele_sifreleme_kurali_olustur()
print("Kurallar başarıyla oluşturuldu!")
print(f"Toplam {len(SIFRELEME_KURALLARI)} adet kural var.")

# --- Şifreleme ve Çözme Fonksiyonları (Önceki Koddan) ---

def sifrele_metin(mesaj, sifreleme_id):
    """
    Verilen mesajı, belirli bir şifreleme ID'sine göre şifreler.
    """
    if sifreleme_id not in SIFRELEME_KURALLARI:
        return "Hata: Belirtilen şifreleme ID'si bulunamadı."

    kural = SIFRELEME_KURALLARI[sifreleme_id]
    sifreli_mesaj_list = []
    
    for karakter in mesaj.lower(): # Basitlik için tüm harfleri küçük harfe çeviriyoruz
        sifreli_karakter = kural.get(karakter, karakter) # Kuralda yoksa karakteri olduğu gibi bırak
        sifreli_mesaj_list.append(sifreli_karakter)

    return f"{sifreleme_id}_" + "".join(sifreli_mesaj_list)

def coz_metin(sifreli_tam_mesaj):
    """
    Şifreleme ID'si içeren şifreli metni çözer.
    """
    try:
        sifreleme_id_str, sifreli_metin = sifreli_tam_mesaj.split('_', 1)
    except ValueError:
        return "Hata: Geçersiz şifreli mesaj formatı. (ID_şifreli_metin bekliyor)"

    if sifreleme_id_str not in SIFRELEME_KURALLARI:
        return "Hata: Şifreleme ID'si kurallarımızda bulunamadı."

    kural = SIFRELEME_KURALLARI[sifreleme_id_str]
    cozulmus_mesaj_list = []
    
    # Çözmek için ters bir kural sözlüğü oluşturmalıyız (değerler anahtar olacak)
    # Eğer kuralda aynı karaktere giden birden fazla orijinal karakter varsa bu tersine çevirme sorun yaratabilir.
    # Bu basit bir yerine koyma olduğu için böyle bir durum olmaz.
    ters_kural = {v: k for k, v in kural.items()} 

    for karakter in sifreli_metin:
        cozulmus_karakter = ters_kural.get(karakter, karakter) # Kuralda yoksa karakteri olduğu gibi bırak
        cozulmus_mesaj_list.append(cozulmus_karakter)
        
    return "".join(cozulmus_mesaj_list)

# --- Terminal Uygulaması ---
def main():
    while True:
        print("\n--- Dinamik Şifreleme Simülasyonu ---")
        print(f"Sistemde {len(SIFRELEME_KURALLARI)} adet şifreleme kuralı yüklü.")
        print("1. Metni Şifrele (Rastgele ID ile)")
        print("2. Metni Çöz")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3): ")

        if secim == '1':
            mesaj = input("Şifrelemek istediğiniz metni girin: ")
            
            # Rastgele bir şifreleme ID'si seç
            rastgele_id = random.choice(list(SIFRELEME_KURALLARI.keys()))
            
            sifreli_tam_mesaj = sifrele_metin(mesaj, rastgele_id)
            print(f"Şifrelenmiş Mesaj ({rastgele_id} ID ile): {sifreli_tam_mesaj}")
        elif secim == '2':
            sifreli_tam_mesaj = input("Çözmek istediğiniz şifreli metni girin (Örn: 001_nahytpt): ")
            cozulmus_mesaj = coz_metin(sifreli_tam_mesaj)
            print(f"Çözülmüş Mesaj: {cozulmus_mesaj}")
        elif secim == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()