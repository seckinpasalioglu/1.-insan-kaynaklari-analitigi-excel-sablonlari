import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Kesintisiz_Izin_Suresi, Donus_Sonrasi_Verimlilik_Artisi
df = pd.read_excel("sirket_verisi.xlsx")

df['Izin_Karesi'] = df['Kesintisiz_Izin_Suresi'] ** 2
X = sm.add_constant(df[['Kesintisiz_Izin_Suresi', 'Izin_Karesi']])
y = df['Donus_Sonrasi_Verimlilik_Artisi']

model = sm.OLS(y, X).fit()
b1 = model.params['Kesintisiz_Izin_Suresi']
b2 = model.params['Izin_Karesi']
optimum_izin = -b1 / (2 * b2)

print("--- UYGULAMA 12: İZİN VE VERİMLİLİK OPTİMİZASYONU ---")
print(f"Verimliliği Maksimum Yapan İdeal Blok İzin Süresi: {optimum_izin:.2f} Gün")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
