import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Referral_Prim_TL, Ise_Alim_Maliyet_TL
df = pd.read_excel("sirket_verisi.xlsx")

kor_ref = df['Referral_Prim_TL'].corr(df['Ise_Alim_Maliyet_TL'])

print("--- UYGULAMA 28: REFERRAL PRİMLERİ VE MALİYET ANALİZİ ---")
print(f"Referral Primleri & Dış İşe Alım Maliyeti Korelasyonu: {kor_ref:.4f}")
