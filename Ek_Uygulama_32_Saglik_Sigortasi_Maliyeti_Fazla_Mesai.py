import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Fazla_Mesai_Saat, Saglik_Sigortasi_Maliyet_TL
df = pd.read_excel("sirket_verisi.xlsx")

kor_saglik = df['Fazla_Mesai_Saat'].corr(df['Saglik_Sigortasi_Maliyet_TL'])

print("--- UYGULAMA 32: FAZLA MESAİ VE SAĞLIK SİGORTASI MALİYETİ ---")
print(f"Fazla Mesai & Sağlık Sigortası Maliyeti Korelasyonu: {kor_saglik:.4f}")
