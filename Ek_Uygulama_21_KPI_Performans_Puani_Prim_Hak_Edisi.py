import numpy as np
import pandas as pd
import statsmodels.api as sm

# Uygulama 21: KPI Performans Puanı ve Prim Hak Edişi Modeli
np.random.seed(21)
n = 120
kpi_puani = np.random.uniform(50, 100, n)
prim_tutari = 1500 + 85 * kpi_puani + np.random.normal(0, 450, n)

df = pd.DataFrame({"KPI_Puani": kpi_puani, "Prim_Tutari_TL": prim_tutari})
X = sm.add_constant(df["KPI_Puani"])
model = sm.OLS(df["Prim_Tutari_TL"], X).fit()

print("==========================================================")
print("UYGULAMA 21: KPI PERFORMANS PUANI VE PRİM HAK EDİŞİ")
print("==========================================================")
print(model.summary().tables[1])
print(f"Model Açıklayıcılık Gücü (R-Kare): %{model.rsquared*100:.2f}")
