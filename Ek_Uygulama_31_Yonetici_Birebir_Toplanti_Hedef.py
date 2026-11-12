import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Toplanti_Kalitesi_Skoru, Hedef_Gercekleme_Yuzdesi
df = pd.read_excel("sirket_verisi.xlsx")

kor_toplanti = df['Toplanti_Kalitesi_Skoru'].corr(df['Hedef_Gercekleme_Yuzdesi'])

print("--- UYGULAMA 31: TOPLANTI KALİTESİ VE HEDEF GERÇEKLEŞME ---")
print(f"Toplantı Kalitesi & Hedef Gerçekleşme Korelasyonu: {kor_toplanti:.4f}")
