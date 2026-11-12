import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Tavsiye_Skoru (0-10 arası)
df = pd.read_excel("sirket_verisi.xlsx")

toplam_kisi = len(df)
destekleyenler = len(df[df['Tavsiye_Skoru'] >= 9])
kotuleyenler = len(df[df['Tavsiye_Skoru'] <= 6])

destek_yuzde = (destekleyenler / toplam_kisi) * 100
kotu_yuzde = (kotuleyenler / toplam_kisi) * 100
enps_skoru = destek_yuzde - kotu_yuzde

print("--- UYGULAMA 8: eNPS BAĞLILIK ANALİZİ ---")
print(f"Destekleyen Personel Oranı: %{destek_yuzde:.2f}")
print(f"Kötüleyici Personel Oranı: %{kotu_yuzde:.2f}")
print(f"Kurumsal Nihai eNPS Endeks Skoru: {enps_skoru:.2f}")
