import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Devamsizlik_Gun, Aidiyet_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

kor_devam = df['Devamsizlik_Gun'].corr(df['Aidiyet_Skoru'])

print("--- UYGULAMA 38: DEVAMSIZLIK VE TURNOVER ÖNCÜSÜ ANALİZİ ---")
print(f"Devamsızlık Gün Sayısı & Aidiyet Skoru Korelasyonu: {kor_devam:.4f}")
