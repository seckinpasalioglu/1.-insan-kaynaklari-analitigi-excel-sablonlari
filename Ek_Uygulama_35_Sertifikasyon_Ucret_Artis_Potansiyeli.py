import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Sertifika_Sayisi, Ucret_Artis_Potansiyeli_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

kor_sertifika = df['Sertifika_Sayisi'].corr(df['Ucret_Artis_Potansiyeli_Skoru'])

print("--- UYGULAMA 35: SERTİFİKASYON VE ÜCRET ARTIŞ POTANSİYELİ ---")
print(f"Sertifika Sayısı & Ücret Artış Potansiyeli Korelasyonu: {kor_sertifika:.4f}")
