import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Aylik_Seyahat_Suresi, Butce_Sapma_Orani
df = pd.read_excel("sirket_verisi.xlsx")

df['Seyahat_Karesi'] = df['Aylik_Seyahat_Suresi'] ** 2
X = sm.add_constant(df[['Aylik_Seyahat_Suresi', 'Seyahat_Karesi']])
y = df['Butce_Sapma_Orani']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 2: SEYAHAT BÜTÇE OPTİMİZASYONU SONUÇLARI ---")
print(f"Seyahat Süresi Doğrusal Etki Katsayısı (b1): {model.params['Aylik_Seyahat_Suresi']:.4f}")
print(f"Karesel Maliyet İvme Katsayısı (b2): {model.params['Seyahat_Karesi']:.4f}")
print(f"Model Bütünsel Gücü (R-Kare): %{model.rsquared * 100:.1f}")
