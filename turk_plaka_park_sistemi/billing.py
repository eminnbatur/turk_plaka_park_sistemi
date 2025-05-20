
# billing.py
import re
from vehicle_operations import Vehicle_Number, Vehicle_Type, Date, Time

def ucret_bilgisi():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tPark Ücretleri")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*1. Bisiklet      20 TL / Saat")
    print("*2. Motor         40 TL / Saat")
    print("*3. Araba         60 TL / Saat")
    print("----------------------------------------------------------------------------------------------------------------------")

def fatura_olustur():
    print("............................................. Fatura Oluşturuluyor .......................................................")
    while True:
        Vno = input("\tFaturası oluşturulacak araç numarasını giriniz (örn: 56 AZ 485) - ").upper()
        if Vno == "":
            print("###### Araç numarası giriniz ######")
        elif re.match(r"^\d{2} [A-ZÇĞİÖŞÜ]{1,3} \d{1,4}$", Vno):
            if Vno in Vehicle_Number:
                i = Vehicle_Number.index(Vno)
                break
            else:
                print("###### Böyle bir araç kayıtlı değil ######")
        else:
            print("###### Geçerli bir Türk plaka formatı giriniz (örn: 34 AB 1234) ######")

    print(f"\tAraç Giriş Saati: {Time[i]}")
    print(f"\tAraç Giriş Tarihi: {Date[i]}")
    print(f"\tAraç Tipi: {Vehicle_Type[i]}")

    while True:
        hr = input("\tAraç kaç saat park etti? - ")
        if hr == "":
            print("###### Saat giriniz ######")
        else:
            try:
                hr_int = int(hr)
                if hr_int == 0:
                    amt = {"Bisiklet": 20, "Motor": 40}.get(Vehicle_Type[i], 60)
                else:
                    amt = {"Bisiklet": hr_int * 20, "Motor": hr_int * 40}.get(Vehicle_Type[i], hr_int * 60)
                break
            except:
                print("###### Geçerli sayı giriniz ######")

    print(f"\tPark Ücreti: {amt} TL")
    ac = 0.18 * amt
    print(f"\tEkstra Ücret %18: {ac:.2f} TL")
    print(f"\tToplam Ücret: {amt + ac:.2f} TL")
    print("............................................. Hizmetimizi kullandığınız için teşekkür ederiz .......................................................")
    input("\tDevam etmek için bir tuşa basınız - ")
