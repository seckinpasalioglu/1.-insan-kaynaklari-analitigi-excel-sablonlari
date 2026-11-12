import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Teknik_Yetkinlik, Liderlik_Potansiyeli, Performans_Gecmisi
df = pd.read_excel("sirket_verisi.xlsx")

scaler = MinMaxScaler(feature_range=(0, 100))
norm_veriler = scaler.fit_transform(df[['Teknik_Yetkinlik', 'Liderlik_Potansiyeli', 'Performans_Gecmisi']])

df['Yetenek_Endeksi'] = (norm_veriler[:, 0] * 0.40) + (norm_veriler[:, 1] * 0.35) + (norm_veriler[:, 2] * 0.25)

print("--- UYGULAMA 6: ÇOK BOYUTLU YETENEK ENDEKSİ ---")
print(f"En Yüksek Yetenek Endeksi Skoru: {df['Yetenek_Endeksi'].max():.2f}")
print(f"Organizasyon Yetenek Endeks Ortalaması: {df['Yetenek_Endeksi'].mean():.2f}")
print(f"75 Puan Üzeri Yüksek Potansiyelli (HiPo) Kişi Sayısı: {len(df[df['Yetenek_Endeksi'] >= 75])}")
