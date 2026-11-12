import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Rotasyon_Sayisi, Baglilik_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

kor_rot = df['Rotasyon_Sayisi'].corr(df['Baglilik_Skoru'])

print("--- UYGULAMA 37: ROTASYON SIKLIĞI VE BAĞLILIK ANALİZİ ---")
print(f"Rotasyon Sıklığı & Bağlılık Skoru Korelasyonu: {kor_rot:.4f}")
