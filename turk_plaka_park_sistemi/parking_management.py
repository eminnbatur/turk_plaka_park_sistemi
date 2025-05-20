
# parking_management.py

from vehicle_operations import (
    arac_giris,
    arac_cikar,
    park_edilen_araclari_goster,
    bos_yerleri_goster,
)
from billing import ucret_bilgisi, fatura_olustur

def main():
    while True:
        print("----------------------------------------------------------------------------------------")
        print("\t\tPark Yönetim Sistemi")
        print("----------------------------------------------------------------------------------------")
        print("1. Araç Girişi")
        print("2. Araç Çıkışı")
        print("3. Park Edilen Araçları Görüntüle")
        print("4. Boş Park Yerlerini Görüntüle")
        print("5. Ücret Bilgisi")
        print("6. Fatura Oluştur")
        print("7. Programı Kapat")
        print("----------------------------------------------------------------------------------------")
        try:
            ch = int(input("\tSeçiminizi yapınız: "))
            if ch == 1:
                arac_giris()
            elif ch == 2:
                arac_cikar()
            elif ch == 3:
                park_edilen_araclari_goster()
            elif ch == 4:
                bos_yerleri_goster()
            elif ch == 5:
                ucret_bilgisi()
            elif ch == 6:
                fatura_olustur()
            elif ch == 7:
                print("............................................. Hizmetimizi kullandığınız için teşekkür ederiz .......................................................")
                print("                                   ********** (: Hoşça kalın :) **********")
                break
            else:
                print("###### Geçerli bir seçenek giriniz ######")
        except ValueError:
            print("###### Lütfen sayı giriniz ######")

if __name__ == "__main__":
    main()
