import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Secilen_Hak_Cesidi, Toplam_Hak_Maliyeti
df = pd.read_excel("sirket_verisi.xlsx")

df['Cesit_Karesi'] = df['Secilen_Hak_Cesidi'] ** 2
X = sm.add_constant(df[['Secilen_Hak_Cesidi', 'Cesit_Karesi']])
y = df['Toplam_Hak_Maliyeti']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 10: ESNEK YAN HAK BÜTÇELEME MODELİ ---")
print(f"Hak Başına Doğrusal Maliyet Artış Etkisi (b1): {model.params['Secilen_Hak_Cesidi']:.2f} Bin TL")
print(f"Karesel Sepet Genişleme Ceza Katsayısı (b2): {model.params['Cesit_Karesi']:.4f}")
print(f"Model İzleme Gücü (R-Kare): %{model.rsquared * 100:.1f}")
