import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Teknik_Test_Skoru, Ilk_Yil_Performans_Puani
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Teknik_Test_Skoru'])
y = df['Ilk_Yil_Performans_Puani']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 7: İŞE ALIM ÖNGÖRÜCÜ GÜÇ ANALİZİ ---")
print(f"Teknik Test Skoru Eğim Katsayısı (b1): {model.params['Teknik_Test_Skoru']:.4f}")
print(f"Katsayı Güvenilirlik Derecesi (t-İstatistiği): {model.tvalues['Teknik_Test_Skoru']:.2f}")
print(f"Testin Başarı Açıklama Oranı (R-Kare): %{model.rsquared * 100:.1f}")
