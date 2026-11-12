import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Isg_Onleyici_Butce, Toplam_Kaza_Maliyeti
df = pd.read_excel("sirket_verisi.xlsx")

df['Isg_Karesi'] = df['Isg_Onleyici_Butce'] ** 2
X = sm.add_constant(df[['Isg_Onleyici_Butce', 'Isg_Karesi']])
y = df['Toplam_Kaza_Maliyeti']

model = sm.OLS(y, X).fit()
b1 = model.params['Isg_Onleyici_Butce']
b2 = model.params['Isg_Karesi']
optimum_isg_butcesi = -b1 / (2 * b2)

print("--- UYGULAMA 9: İSG MALİYET OPTİMİZASYONU ---")
print(f"Finansal Tasarrufu Maksimum Yapan İSG Bütçe Sınırı: {optimum_isg_butcesi:.2f} Bin TL")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
