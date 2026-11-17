[13:19, 17.11.2026] Seckin: import numpy as np
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
[13:21, 17.11.2026] Seckin: import numpy as np
import pandas as pd
import statsmodels.api as sm

# Uygulama 22: Aday Yetkinlik Mülakatı ve İşe Alım Kabul Skoru (Logit)
np.random.seed(22)
n = 150
mulakat_skoru = np.random.uniform(40, 98, n)
log_odds = -6.5 + 0.095 * mulakat_skoru
olasilik = 1 / (1 + np.exp(-log_odds))
teklif_kabul = np.random.binomial(1, olasilik)

df = pd.DataFrame(
    {"Mulakat_Skoru": mulakat_skoru, "Teklif_Kabul": teklif_kabul}
)
X = sm.add_constant(df["Mulakat_Skoru"])
model = sm.Logit(df["Teklif_Kabul"], X).fit(disp=False)

print("==========================================================")
print("UYGULAMA 22: ADAY YETKİNLİK MÜLAKATI VE İŞE ALIM KABUL SKORU")
print("==========================================================")
print(model.summary().tables[1])
