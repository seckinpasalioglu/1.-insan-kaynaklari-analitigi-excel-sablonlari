import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Ogrenme_Kalicilik_Puani, Is_Performans_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

korelasyon = df['Ogrenme_Kalicilik_Puani'].corr(df['Is_Performans_Skoru'])

print("--- UYGULAMA 36: ÖĞRENME KALICILIĞI VE İŞ PERFORMANSI ---")
print(f"Öğrenme Kalıcılığı & İş Performansı Korelasyonu: {korelasyon:.4f}")
