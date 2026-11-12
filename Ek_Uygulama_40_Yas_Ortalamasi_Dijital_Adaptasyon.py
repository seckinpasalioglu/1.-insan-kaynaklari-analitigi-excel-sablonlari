import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Yas_Ortalamasi, Uyum_Suresi_Hafta
df = pd.read_excel("sirket_verisi.xlsx")

kor_dij = df['Yas_Ortalamasi'].corr(df['Uyum_Suresi_Hafta'])

print("--- UYGULAMA 40: YAŞ ORTALAMASI VE DİJİTAL ADAPTASYON ---")
print(f"Yaş Ortalaması & Uyum Süresi Korelasyonu: {kor_dij:.4f}")
