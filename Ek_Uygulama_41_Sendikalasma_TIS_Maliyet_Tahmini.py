import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Sendikalasma_Orani, Sozlesme_Ek_Maliyet_Yuzde
df = pd.read_excel("sirket_verisi.xlsx")

kor_sendika = df['Sendikalasma_Orani'].corr(df['Sozlesme_Ek_Maliyet_Yuzde'])

print("--- UYGULAMA 41: SENDİKALAŞMA VE TİS MALİYET TAHMİNİ ---")
print(f"Sendikalaşma Oranı & Sözleşme Ek Maliyet Korelasyonu: {kor_sendika:.4f}")
