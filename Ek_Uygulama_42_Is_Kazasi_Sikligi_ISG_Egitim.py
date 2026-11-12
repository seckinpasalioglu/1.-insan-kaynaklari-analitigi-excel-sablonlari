import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: ISG_Egitim_Saati, Is_Kazasi_Sayisi
df = pd.read_excel("sirket_verisi.xlsx")

kor_isg = df['ISG_Egitim_Saati'].corr(df['Is_Kazasi_Sayisi'])

print("--- UYGULAMA 42: İŞ KAZASI SIKLIĞI VE İSG EĞİTİM SAATLERİ ---")
print(f"İSG Eğitim Saati & İş Kazası Sayısı Korelasyonu: {kor_isg:.4f}")
