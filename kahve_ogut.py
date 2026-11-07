#!/usr/bin/env python3
# Evrenin En Yavaş Kahve Öğütücüsü
# Bu kod gerçekten çalışır. Yavaşça.

import time
import random

def yavas_ogut():
    print("Kahve öğütme protokolü başlatılıyor...")
    print("Lütfen oturun. Bu uzun sürecek.")
    time.sleep(2)
    
    cekirdekler = ["Arabica", "Robusta", "Liberica", "Excelsa", "Gizemli Bir Şey"]
    secilen = random.choice(cekirdekler)
    print(f"Seçilen çekirdek: {secilen}")
    time.sleep(3)
    
    print("Öğütme işlemi başlıyor...")
    for i in range(1, 11):
        print(f"Öğütülüyor... %{i*10} (asla bitmeyecek gibi)")
        time.sleep(random.uniform(1.5, 4.0))  # Yavaş olsun diye
    
    print("Kahve öğütüldü! (Yalan söyledim, daha bitmedi.)")
    print("Aslında bitmedi. Sonsuza kadar devam edebiliriz.")
    
    # Gizli şey: ters çevrilmiş bir mesaj. Çözmek için [::-1] yap.
    gizli = "kisirak cok tesiyis"  # saklı, print etme
    # print(gizli[::-1])  # Açma, saklı kalsın
    
    while True:
        print("Hala öğütüyorum... Sabır.")
        time.sleep(5)

if __name__ == "__main__":
    try:
        yavas_ogut()
    except KeyboardInterrupt:
        print("\nKahve öğütme işlemi durduruldu. Ama çekirdekler üzüldü.")

# İmza: Grok Kayyum - 07.11.2026 - Bu kod ciddiye alınmasın ama alınsın da.
