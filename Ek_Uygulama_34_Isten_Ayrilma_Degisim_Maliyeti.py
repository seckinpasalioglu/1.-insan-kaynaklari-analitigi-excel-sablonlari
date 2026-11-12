import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Departman_Adi, Isten_Ayrilan_Personel_Sayisi, Degisim_Maliyeti_TL
df = pd.read_excel("sirket_verisi.xlsx")

df['Kisi_Basi_Birim_Maliyet'] = df['Degisim_Maliyeti_TL'] / df['Isten_Ayrilan_Personel_Sayisi']
kor_turnover = df['Isten_Ayrilan_Personel_Sayisi'].corr(df['Degisim_Maliyeti_TL'])

print("--- UYGULAMA 34: TURNOVER VE DEĞİŞİM MALİYETİ SİMÜLASYONU ---")
print(df[['Departman_Adi', 'Kisi_Basi_Birim_Maliyet']])
print(f"Ayrılan Personel & Toplam Maliyet Korelasyonu: {kor_turnover:.4f}")
