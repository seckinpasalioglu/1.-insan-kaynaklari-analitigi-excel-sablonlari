import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Departman, Kullanilmayan_Izin_Gun, Yasal_Dava_Riski_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

departman_ozet = df.groupby('Departman').agg(
    Toplam_Personel=('Kullanilmayan_Izin_Gun', 'count'),
    Ortalama_Biriken_Izin=('Kullanilmayan_Izin_Gun', 'mean'),
    Ortalama_Risk_Skoru=('Yasal_Dava_Riski_Skoru', 'mean')
)
kor_izin = df['Kullanilmayan_Izin_Gun'].corr(df['Yasal_Dava_Riski_Skoru'])

print("--- UYGULAMA 27: BİRİKEN YILLIK İZİNLER VE RİSK ANALİZİ ---")
print(departman_ozet)
print(f"Kullanılmayan İzin & Yasal Risk Korelasyonu: {kor_izin:.4f}")
