import tkinter as tk
from tkinter import messagebox, ttk
import re

# Başlangıç verileri
bikes = 100
cars = 250
bicycles = 78

Vehicle_Number = []
Vehicle_Type = []
vehicle_Name = []
Owner_Name = []
Date = []
Time = []

root = tk.Tk()
root.title("Park Yönetim Sistemi")
root.geometry("600x500")

# Plaka format kontrolü
def gecerli_plaka(plaka):
    return re.match(r"^\d{2} [A-ZÇĞİÖŞÜ]{1,3} \d{1,4}$", plaka.upper())

# Araç ekleme
def arac_ekle():
    global bikes, cars, bicycles
    plaka = entry_plaka.get().upper()
    tur = combo_tur.get()
    isim = entry_arac.get()
    sahip = entry_sahip.get()
    tarih = entry_tarih.get()
    saat = entry_saat.get()

    if not gecerli_plaka(plaka):
        messagebox.showerror("Hata", "Geçerli plaka formatı girin (örn: 34 AB 1234)")
        return
    if plaka in Vehicle_Number:
        messagebox.showerror("Hata", "Bu plaka zaten kayıtlı.")
        return

    if tur == "Bisiklet":
        if bicycles == 0:
            messagebox.showinfo("Dolu", "Bisiklet park yeri kalmadı")
            return
        bicycles -= 1
    elif tur == "Motor":
        if bikes == 0:
            messagebox.showinfo("Dolu", "Motor park yeri kalmadı")
            return
        bikes -= 1
    elif tur == "Araba":
        if cars == 0:
            messagebox.showinfo("Dolu", "Araba park yeri kalmadı")
            return
        cars -= 1
    else:
        messagebox.showerror("Hata", "Araç türü seçiniz")
        return

    Vehicle_Number.append(plaka)
    Vehicle_Type.append(tur)
    vehicle_Name.append(isim)
    Owner_Name.append(sahip)
    Date.append(tarih)
    Time.append(saat)

    messagebox.showinfo("Başarılı", "Araç başarıyla eklendi")
    entry_plaka.delete(0, tk.END)
    entry_arac.delete(0, tk.END)
    entry_sahip.delete(0, tk.END)
    entry_tarih.delete(0, tk.END)
    entry_saat.delete(0, tk.END)
    combo_tur.set("")

# Araç çıkışı
def arac_cikar():
    global bikes, cars, bicycles
    plaka = entry_plaka.get().upper()
    if plaka in Vehicle_Number:
        i = Vehicle_Number.index(plaka)
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
        messagebox.showinfo("Başarılı", "Araç silindi")
    else:
        messagebox.showerror("Hata", "Araç bulunamadı")

# Park edilenleri göster
def goster():
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, "Plaka\tTip\tAraç İsmi\tSahip\tTarih\tSaat\n")
    text_output.insert(tk.END, "-"*80 + "\n")
    for i in range(len(Vehicle_Number)):
        line = f"{Vehicle_Number[i]}\t{Vehicle_Type[i]}\t{vehicle_Name[i]}\t{Owner_Name[i]}\t{Date[i]}\t{Time[i]}\n"
        text_output.insert(tk.END, line)

# Boş yerleri göster
def bos_yer():
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Bisiklet için boş yer: {bicycles}\n")
    text_output.insert(tk.END, f"Motor için boş yer: {bikes}\n")
    text_output.insert(tk.END, f"Araba için boş yer: {cars}\n")

# Fatura oluştur
def fatura():
    plaka = entry_plaka.get().upper()
    if plaka not in Vehicle_Number:
        messagebox.showerror("Hata", "Araç bulunamadı")
        return
    try:
        saat = int(entry_saat.get())
    except:
        messagebox.showerror("Hata", "Geçerli saat giriniz")
        return

    i = Vehicle_Number.index(plaka)
    tip = Vehicle_Type[i]
    oran = {"Bisiklet": 20, "Motor": 40, "Araba": 60}.get(tip, 60)
    tutar = oran * (saat if saat > 0 else 1)
    ekstra = tutar * 0.18
    toplam = tutar + ekstra

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Plaka: {plaka}\nTip: {tip}\nSaat: {saat}\nTutar: {tutar} TL\nKDV: {ekstra:.2f} TL\nToplam: {toplam:.2f} TL\n")

# Arayüz bileşenleri
frame = tk.Frame(root)
frame.pack(pady=10)

entry_plaka = tk.Entry(frame, width=20)
entry_plaka.grid(row=0, column=1)
tk.Label(frame, text="Plaka:").grid(row=0, column=0)

combo_tur = ttk.Combobox(frame, values=["Bisiklet", "Motor", "Araba"], state="readonly")
combo_tur.grid(row=1, column=1)
tk.Label(frame, text="Araç Tipi:").grid(row=1, column=0)

entry_arac = tk.Entry(frame, width=20)
entry_arac.grid(row=2, column=1)
tk.Label(frame, text="Araç İsmi:").grid(row=2, column=0)

entry_sahip = tk.Entry(frame, width=20)
entry_sahip.grid(row=3, column=1)
tk.Label(frame, text="Sahip İsmi:").grid(row=3, column=0)

entry_tarih = tk.Entry(frame, width=20)
entry_tarih.grid(row=4, column=1)
tk.Label(frame, text="Tarih (GG-AA-YYYY):").grid(row=4, column=0)

entry_saat = tk.Entry(frame, width=20)
entry_saat.grid(row=5, column=1)
tk.Label(frame, text="Saat (veya Süre):").grid(row=5, column=0)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Araç Ekle", command=arac_ekle).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Araç Çıkar", command=arac_cikar).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Park Listesi", command=goster).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Boş Yerler", command=bos_yer).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Fatura", command=fatura).grid(row=0, column=4, padx=5)

text_output = tk.Text(root, height=12, width=70)
text_output.pack(pady=10)

root.mainloop()