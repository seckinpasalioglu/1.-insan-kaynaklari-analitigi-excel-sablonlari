import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Egitim_Suresi, Yillik_Hata_Sayisi
df = pd.read_excel("sirket_verisi.xlsx")

df['Egitim_Karesi'] = df['Egitim_Suresi'] ** 2
X = sm.add_constant(df[['Egitim_Suresi', 'Egitim_Karesi']])
y = df['Yillik_Hata_Sayisi']

model = sm.OLS(y, X).fit()
b1 = model.params['Egitim_Suresi']
b2 = model.params['Egitim_Karesi']
optimum_egitim = -b1 / (2 * b2)

print("--- UYGULAMA 1: EĞİTİM VE HATA ANALİZİ SONUÇLARI ---")
print(f"Hatanın En Düşük Olduğu Optimum Eğitim Süresi: {optimum_egitim:.2f} Saat/Yıl")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
