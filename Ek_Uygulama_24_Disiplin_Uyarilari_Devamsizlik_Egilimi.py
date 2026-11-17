import numpy as np
import pandas as pd
import statsmodels.api as sm

# Uygulama 24: Disiplin Uyarıları ve Devamsızlık Eğilimi Erken Uyarı Modeli
np.random.seed(24)
n = 130
disiplin_uyari_sayisi = np.random.poisson(1.2, n)
yillik_devamsizlik_gun = (
    2.5 + 3.4 * disiplin_uyari_sayisi + np.random.normal(0, 1.5, n)
)

df = pd.DataFrame({
    "Disiplin_Uyari": disiplin_uyari_sayisi,
    "Devamsizlik_Gun": yillik_devamsizlik_gun,
})
X = sm.add_constant(df["Disiplin_Uyari"])
model = sm.OLS(df["Devamsizlik_Gun"], X).fit()

print("==========================================================")
print("UYGULAMA 24: DİSİPLİN UYARILARI VE DEVAMSIZLIK EĞİLİMİ")
print("==========================================================")
print(model.summary().tables[1])
print(f"Model Açıklayıcılık Gücü (R-Kare): %{model.rsquared*100:.2f}")
