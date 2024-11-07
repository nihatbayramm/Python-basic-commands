# Python Temel Kodları

# 1. Değişkenler ve Veri Tipleri
sayi = 5                     # integer (tam sayı) tipinde bir değişken
ondalik_sayi = 3.14          # float (ondalıklı sayı) tipinde bir değişken
isim = "Python"              # string (metin) tipinde bir değişken
aktif_mi = True              # boolean (mantıksal) tipinde bir değişken

# 2. Matematiksel Operatörler
toplam = sayi + ondalik_sayi   # toplama işlemi
fark = sayi - ondalik_sayi     # çıkarma işlemi
carpim = sayi * ondalik_sayi   # çarpma işlemi
bolum = sayi / ondalik_sayi    # bölme işlemi
mod = sayi % 2                 # mod alma (kalan bulma) işlemi
kuvvet = sayi ** 2             # üs alma işlemi

# 3. String İşlemleri
mesaj = "Merhaba, " + isim     # string birleştirme
mesaj_uzunlugu = len(isim)     # string uzunluğunu bulma
buyuk_isim = isim.upper()      # tüm harfleri büyük yapma
kucuk_isim = isim.lower()      # tüm harfleri küçük yapma

# 4. Listeler
sayilar = [1, 2, 3, 4, 5]      # bir liste oluşturma
sayilar.append(6)              # listeye eleman ekleme
ilk_sayi = sayilar[0]          # listedeki ilk elemanı alma
dilim_sayilar = sayilar[1:3]   # listeden dilim alma
sayilar.pop()                  # listedeki son elemanı çıkarma
sayilar.reverse()              # listeyi ters çevirme

# 5. Koşullu İfadeler (if-else)
if sayi > 0:                     # sayi sıfırdan büyükse
    print("sayi pozitif")         # bu mesajı yazdır
elif sayi < 0:                   # sayi sıfırdan küçükse
    print("sayi negatif")         # bu mesajı yazdır
else:                            # diğer durumlarda
    print("sayi sıfır")           # bu mesajı yazdır

# 6. Döngüler
for eleman in sayilar:           # listedeki her bir eleman için
    print(eleman)                # elemanı yazdır

i = 0                            # while döngüsü için başlangıç değeri
while i < len(sayilar):          # i, listenin uzunluğundan küçük olduğu sürece
    print(sayilar[i])            # listenin i. elemanını yazdır
    i += 1                       # i'yi 1 artır

# 7. Fonksiyonlar
def topla(a, b):                 # iki parametre alan bir fonksiyon tanımlama
    return a + b                 # iki sayının toplamını döndür

sonuc = topla(10, 20)            # fonksiyonu çağır ve sonucu sakla

# 8. Sözlükler (Dictionaries)
ogrenci = {"isim": "Ahmet", "yas": 21, "not": "A"}  # sözlük tanımlama
ogrenci_ismi = ogrenci["isim"]                      # sözlükten değeri alma
ogrenci["yas"] = 22                                 # sözlükteki değeri güncelleme
ogrenci["bolum"] = "Mühendislik"                    # yeni bir anahtar-değer çifti ekleme
print(ogrenci.keys())                               # tüm anahtarları listeleme
print(ogrenci.values())                             # tüm değerleri listeleme

# 9. Hata Yönetimi (Try-Except)
try:
    print(10 / 0)               # sıfıra bölme hatası yap
except ZeroDivisionError:       # hata oluşursa bu bloğa gir
    print("Sıfıra bölme hatası!")  # hata mesajı yazdır

# 10. Dosya İşlemleri
with open("dosya.txt", "w") as dosya:   # dosya açma (yazma modu)
    dosya.write("Merhaba, Python!")     # dosyaya yazma

# 11. Küme İşlemleri
kume1 = {1, 2, 3}                      # bir küme tanımlama
kume2 = {3, 4, 5}                      # başka bir küme tanımlama
birlesim = kume1 | kume2               # kümelerin birleşimi
kesisim = kume1 & kume2                # kümelerin kesişimi
fark = kume1 - kume2                   # kümelerin farkı
ayrık_mı = kume1.isdisjoint(kume2)     # kümeler ayrık mı (kesişim yok mu?)

# 12. Liste Anlama (List Comprehension)
kareler = [x**2 for x in range(10)]    # 0'dan 9'a kadar sayıların karelerini listeleme
cift_sayilar = [x for x in range(20) if x % 2 == 0]  # 0'dan 19'a kadar çift sayıları listeleme

# 13. Lambda Fonksiyonları
topla = lambda a, b: a + b             # lambda fonksiyonuyla toplama işlemi tanımlama
sonuc = topla(3, 7)                    # lambda fonksiyonunu çağırma

# 14. Modül Kullanımı (math modülü örneği)
import math                            # math modülünü içe aktarma
karekok = math.sqrt(16)                # karekök hesaplama
pi_degeri = math.pi                    # pi sayısını kullanma

# 15. Nesne Yönelimli Programlama (OOP) - Sınıf ve Nesne Tanımlama
class Araba:                           # Araba adında bir sınıf tanımlama
    def __init__(self, marka, model):  # yapıcı metod (constructor)
        self.marka = marka             # marka değişkeni
        self.model = model             # model değişkeni

    def bilgileri_goster(self):        # bilgi gösteren bir metod
        return f"Araba: {self.marka} {self.model}"

araba1 = Araba("Toyota", "Corolla")    # Araba sınıfından bir nesne oluşturma
print(araba1.bilgileri_goster())       # nesne ile metoda erişim

