import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Toplam_Mesai_Saat, Kusurlu_Urun_Fire_Yuzde
df = pd.read_excel("sirket_verisi.xlsx")

kor_fire = df['Toplam_Mesai_Saat'].corr(df['Kusurlu_Urun_Fire_Yuzde'])

print("--- UYGULAMA 45: FAZLA MESAİ VE KUSURLU ÜRÜN FİRE ORANI ---")
print(f"Toplam Mesai Saati & Fire Yüzdesi Korelasyonu: {kor_fire:.4f}")
