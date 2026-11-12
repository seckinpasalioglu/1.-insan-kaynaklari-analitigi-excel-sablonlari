import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Unvanda_Kalma_Suresi_Yil, Terfi_Olasiligi_Yuzde
df = pd.read_excel("sirket_verisi.xlsx")

ozet_terfi = df.groupby('Unvanda_Kalma_Suresi_Yil')['Terfi_Olasiligi_Yuzde'].mean()
kor_dusuk_yil = df[df['Unvanda_Kalma_Suresi_Yil'] < 5]['Unvanda_Kalma_Suresi_Yil'].corr(df['Terfi_Olasiligi_Yuzde'])
kor_yuksek_yil = df[df['Unvanda_Kalma_Suresi_Yil'] >= 5]['Unvanda_Kalma_Suresi_Yil'].corr(df['Terfi_Olasiligi_Yuzde'])

print("--- UYGULAMA 30: TERFİ OLASILIĞI VE TAVAN SINIRI ANALİZİ ---")
print(ozet_terfi)
print(f"5 Yıldan Az Kıdemlerde Korelasyon: {kor_dusuk_yil:.4f}")
print(f"5 Yıl ve Üzeri Kıdemlerde Korelasyon (Tavan Kırılması): {kor_yuksek_yil}")
