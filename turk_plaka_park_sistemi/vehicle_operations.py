
# vehicle_operations.py
import re

bikes = 100
cars = 250
bicycles = 78

Vehicle_Number = ['56 AZ 485']
Vehicle_Type = ['Motor']
vehicle_Name = ['Intruder']
Owner_Name = ['Unknown']
Date = ['22-22-3636']
Time = ['22:22:22']

def arac_giris():
    global bikes, cars, bicycles
    while True:
        Vno = input("\tAraç numarasını giriniz (örn: 56 AZ 485) - ").upper()
        if Vno == "":
            print("###### Araç numarası giriniz ######")
        elif Vno in Vehicle_Number:
            print("###### Araç numarası zaten mevcut ######")
        elif re.match(r"^\d{2} [A-ZÇĞİÖŞÜ]{1,3} \d{1,4}$", Vno):
            Vehicle_Number.append(Vno)
            break
        else:
            print("###### Geçerli bir Türk plaka formatı giriniz (örn: 34 AB 1234) ######")

    while True:
        Vtype = input("\tAraç tipi giriniz (Bisiklet=A/Motor=B/Araba=C): ").lower()
        if Vtype == "":
            print("###### Araç tipi giriniz ######")
        elif Vtype == "a":
            Vehicle_Type.append("Bisiklet")
            bicycles -= 1
            break
        elif Vtype == "b":
            Vehicle_Type.append("Motor")
            bikes -= 1
            break
        elif Vtype == "c":
            Vehicle_Type.append("Araba")
            cars -= 1
            break
        else:
            print("###### Geçerli araç tipi giriniz ######")

    while True:
        vname = input("\tAraç ismini giriniz - ")
        if vname == "":
            print("###### Araç ismi giriniz ######")
        else:
            vehicle_Name.append(vname)
            break

    while True:
        OName = input("\tSahibinin ismini giriniz - ")
        if OName == "":
            print("###### Sahip ismi giriniz ######")
        else:
            Owner_Name.append(OName)
            break

    while True:
        date = input("\tTarih giriniz (GG-AA-YYYY) - ")
        if date == "":
            print("###### Tarih giriniz ######")
        elif len(date) != 10:
            print("###### Geçerli tarih giriniz ######")
        else:
            Date.append(date)
            break

    while True:
        saat = input("\tSaat giriniz (SS:DD:SS) - ")
        if saat == "":
            print("###### Saat giriniz ######")
        elif len(saat) != 8:
            print("###### Geçerli saat giriniz ######")
        else:
            Time.append(saat)
            break

    print("\n....................................... Kayıt başarıyla eklendi .......................................")

def arac_cikar():
    global bikes, cars, bicycles
    while True:
        Vno = input("\tSilinecek araç numarasını giriniz (örn: 56 AZ 485) - ").upper()
        if Vno == "":
            print("###### Araç numarası giriniz ######")
        elif re.match(r"^\d{2} [A-ZÇĞİÖŞÜ]{1,3} \d{1,4}$", Vno):
            if Vno in Vehicle_Number:
                i = Vehicle_Number.index(Vno)
                tip = Vehicle_Type[i]
                Vehicle_Number.pop(i)
                Vehicle_Type.pop(i)
                vehicle_Name.pop(i)
                Owner_Name.pop(i)
                Date.pop(i)
                Time.pop(i)
                if tip == "Bisiklet":
                    bicycles += 1
                elif tip == "Motor":
                    bikes += 1
                elif tip == "Araba":
                    cars += 1
                print("\n....................................... Kayıt başarıyla silindi .......................................")
                break
            else:
                print("###### Böyle bir kayıt yok ######")
        else:
            print("###### Geçerli bir Türk plaka formatı giriniz ######")

def park_edilen_araclari_goster():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tPark Edilen Araçlar")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Araç No.\tAraç Tipi\tAraç İsmi\tSahip İsmi\tTarih\t\tSaat")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range(len(Vehicle_Number)):
        print(f"{Vehicle_Number[i]}\t  {Vehicle_Type[i]}\t\t{vehicle_Name[i]}\t\t{Owner_Name[i]}\t\t{Date[i]}\t{Time[i]}")
    print("----------------------------------------------------------------------------------------------------------------------")
    print(f"Toplam Kayıt Sayısı: {len(Vehicle_Number)}")
    print("----------------------------------------------------------------------------------------------------------------------")

def bos_yerleri_goster():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tBoş Park Yerleri")
    print("----------------------------------------------------------------------------------------------------------------------")
    print(f"\tBisiklet için boş yer sayısı: {bicycles}")
    print(f"\tMotor için boş yer sayısı: {bikes}")
    print(f"\tAraba için boş yer sayısı: {cars}")
    print("----------------------------------------------------------------------------------------------------------------------")
