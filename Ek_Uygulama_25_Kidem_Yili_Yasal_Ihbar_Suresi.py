import numpy as np
import pandas as pd
import statsmodels.api as sm

# Uygulama 25: Kıdem Yılı ve Yasal İhbar Süresi (Tavan Sınırı Modeli)
np.random.seed(25)
n = 110
kidem_yili = np.random.uniform(0.2, 12.0, n)
# 4857 Sayılı İş Kanunu Madde 17 tavan sınırı (8 hafta = 56 gün) yaklaşımı
ihbar_gun = np.minimum(56, 14 + 5.2 * kidem_yili) + np.random.normal(0, 2, n)

df = pd.DataFrame({"Kidem_Yili": kidem_yili, "Ihbar_Suresi_Gun": ihbar_gun})
df["Kidem_Kare"] = df["Kidem_Yili"] ** 2
X = sm.add_constant(df[["Kidem_Yili", "Kidem_Kare"]])
model = sm.OLS(df["Ihbar_Suresi_Gun"], X).fit()

print("==========================================================")
print("UYGULAMA 25: KIDEM YILI VE YASAL İHBAR SÜRESİ (TAVAN SINIRI)")
print("==========================================================")
print(model.summary().tables[1])
print(f"Model Açıklayıcılık Gücü (R-Kare): %{model.rsquared*100:.2f}")
