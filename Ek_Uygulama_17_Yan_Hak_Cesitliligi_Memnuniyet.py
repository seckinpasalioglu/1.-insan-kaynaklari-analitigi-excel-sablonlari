import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Sunulan_Hak_Cesidi, Genel_Memnuniyet_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

df['Cesit_Karesi'] = df['Sunulan_Hak_Cesidi'] ** 2
X = sm.add_constant(df[['Sunulan_Hak_Cesidi', 'Cesit_Karesi']])
y = df['Genel_Memnuniyet_Skoru']

model = sm.OLS(y, X).fit()
b1 = model.params['Sunulan_Hak_Cesidi']
b2 = model.params['Cesit_Karesi']
optimum_cesit = -b1 / (2 * b2)

print("--- UYGULAMA 17: YAN HAK DOYUM OPTİMİZASYONU ---")
print(f"Memnuniyeti Maksimum Yapan İdeal Sepet Çeşidi: {optimum_cesit:.2f} Adet")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
