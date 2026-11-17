import numpy as np
import pandas as pd
import statsmodels.api as sm

# Uygulama 23: Eğitmen Kalitesi ve Eğitim NPS Skoru Analizi
np.random.seed(23)
n = 100
egitmen_puani = np.random.uniform(2.5, 5.0, n)
egitim_nps = -15 + 21.5 * egitmen_puani + np.random.normal(0, 6, n)

df = pd.DataFrame({"Egitmen_Kalitesi": egitmen_puani, "Egitim_NPS": egitim_nps})
X = sm.add_constant(df["Egitmen_Kalitesi"])
model = sm.OLS(df["Egitim_NPS"], X).fit()

print("==========================================================")
print("UYGULAMA 23: EĞİTMEN KALİTESİ VE EĞİTİM NPS SKORU")
print("==========================================================")
print(model.summary().tables[1])
print(f"Model Açıklayıcılık Gücü (R-Kare): %{model.rsquared*100:.2f}")
