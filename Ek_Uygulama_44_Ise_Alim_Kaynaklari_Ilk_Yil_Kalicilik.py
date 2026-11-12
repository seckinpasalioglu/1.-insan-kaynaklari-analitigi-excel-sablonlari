import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Eslesme_Kalite_Skoru, Ilk_Yil_Kalicilik_Yuzde
df = pd.read_excel("sirket_verisi.xlsx")

kor_kaynak = df['Eslesme_Kalite_Skoru'].corr(df['Ilk_Yil_Kalicilik_Yuzde'])

print("--- UYGULAMA 44: İŞE ALIM KAYNAKLARI VE İLK YIL KALICILIK ---")
print(f"Eşleşme Kalitesi & İlk Yıl Kalıcılık Korelasyonu: {kor_kaynak:.4f}")
