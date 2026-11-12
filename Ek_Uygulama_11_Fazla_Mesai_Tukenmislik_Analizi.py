import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Aylik_Fazla_Mesai_Suresi, Tukenmislik_Stres_Puani
df = pd.read_excel("sirket_verisi.xlsx")

df['Mesai_Karesi'] = df['Aylik_Fazla_Mesai_Suresi'] ** 2
X = sm.add_constant(df[['Aylik_Fazla_Mesai_Suresi', 'Mesai_Karesi']])
y = df['Tukenmislik_Stres_Puani']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 11: TÜKENMİŞLİK VE STRES ANALİZİ ---")
print(f"Mesai Süresi Doğrusal Katsayı Etkisi (b1): {model.params['Aylik_Fazla_Mesai_Suresi']:.4f}")
print(f"Karesel Stres İvme Katsayısı (b2): {model.params['Mesai_Karesi']:.4f}")
print(f"Model İzleme Gücü (R-Kare): %{model.rsquared * 100:.1f}")
