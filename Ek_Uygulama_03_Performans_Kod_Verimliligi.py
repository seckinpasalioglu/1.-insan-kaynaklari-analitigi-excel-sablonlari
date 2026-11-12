import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Haftalik_Kod_Satiri, Sistem_Verimlilik_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

df['Kod_Karesi'] = df['Haftalik_Kod_Satiri'] ** 2
X = sm.add_constant(df[['Haftalik_Kod_Satiri', 'Kod_Karesi']])
y = df['Sistem_Verimlilik_Skoru']

model = sm.OLS(y, X).fit()
b1 = model.params['Haftalik_Kod_Satiri']
b2 = model.params['Kod_Karesi']
optimum_satir = -b1 / (2 * b2)

print("--- UYGULAMA 3: KOD VERİMLİLİĞİ OPTİMİZASYONU SONUÇLARI ---")
print(f"Maksimum Performans Sağlayan Haftalık Kod Sınırı: {optimum_satir:.2f} Bin Satır")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
