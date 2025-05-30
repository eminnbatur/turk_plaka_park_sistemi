# 🚗 Park Yönetim Sistemi

Bu proje, araç giriş-çıkış işlemlerini yönetebilen ve fatura hesaplaması yapabilen, hem grafik arayüz (GUI) hem de komut satırı (CLI) desteği bulunan bir **Park Yönetim Sistemi**dir.

## 📌 Proje Özellikleri

- Araç giriş/çıkış kaydı
- Park yerlerinin takibi (bisiklet, motor, araba)
- Park edilmiş araçların listelenmesi
- Boş yerlerin görüntülenmesi
- Park süresine göre fatura oluşturma
- Türk plakalarına uygunluk kontrolü (regex)
- Hem terminal hem de GUI desteği (Tkinter)

## 🧩 Kullanılan Modüller & Dosyalar

| Dosya Adı              | Açıklama |
|------------------------|----------|
| `parking_gui.py`       | Tkinter ile grafik arayüz tasarımı yapılmıştır. Butonlar, giriş kutuları ve fatura ekranı buradadır. |
| `parking_management.py`| Komut satırı menüsü ile çalışan terminal tabanlı uygulamadır. |
| `vehicle_operations.py`| Araç bilgilerini listeye ekleyen, kaldıran ve listeleyen fonksiyonları içerir. |
| `billing.py`           | Park süresine göre ücret hesaplama ve fatura oluşturma işlemleri burada yapılır. |

## 🧪 Kullanılan Kütüphaneler

- `tkinter` – Arayüz oluşturma
- `tkinter.ttk` – Gelişmiş bileşenler (ComboBox)
- `tkinter.messagebox` – Uyarı ve bilgi mesajları
- `re` – Plaka formatı doğrulama (Regex)

> ❗ Bu proje yalnızca dahili listelerle çalışır. Kalıcı veri saklamaz.

## ⚙️ Kurulum ve Çalıştırma

1. Python 3 yüklü olduğundan emin olun.
2. Proje dosyalarını indirin veya klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/park-yonetim-sistemi.git
   cd park-yonetim-sistemi
Grafik arayüz için:

bash
Kopyala
Düzenle
python parking_gui.py
Terminal sürümü için:

bash
Kopyala
Düzenle
python parking_management.py
🛠️ Geliştirme İçin Öneriler
SQLite gibi veritabanı desteği eklenerek veriler kalıcı hale getirilebilir.

Kullanıcı girişi ve yönetimi yapılabilir.

Faturalar .pdf olarak oluşturulabilir.

Web arayüzü (Flask/Django) geliştirilebilir.

QR kod veya plaka tanıma sistemi entegre edilebilir.
