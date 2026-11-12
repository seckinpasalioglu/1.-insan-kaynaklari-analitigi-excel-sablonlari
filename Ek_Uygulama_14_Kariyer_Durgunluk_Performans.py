import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Unvanda_Bekleme_Suresi, Yillik_KPI_Performans_Puani
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Unvanda_Bekleme_Suresi'])
y = df['Yillik_KPI_Performans_Puani']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 14: KARİYER DURGUNLUK ANALİZİ ---")
print(f"Unvanda Kalınan Her Ayın Performansa Olumsuz Etkisi (b1): {model.params['Unvanda_Bekleme_Suresi']:.4f} Puan")
print(f"Model Katsayı Anlamlılığı (t-İstatistiği): {model.tvalues['Unvanda_Bekleme_Suresi']:.2f}")
