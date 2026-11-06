import numpy as np
import pandas as pd
import statsmodels.api as sm

# Simülasyon için 500 kişilik örnek veri seti mizanpajı oluşturuluyor
np.random.seed(42)
gozetim = np.random.uniform(20, 95, 500)
# Parabolik (eğrisel) aşınma fonksiyonu formüle ediliyor
verim = -185.33 + (12.00 * gozetim) - (0.0900 * (gozetim**2)) + np.random.normal(0, 5, 500)

dplam_matris = pd.DataFrame({'Gozetim_Skoru': gozetim, 'Haftalik_Verim_Orani': verim})

# Parabolik Regresyon Modelinin İnşası (X ve X^2 Terimlerinin Matrise Eklenmesi)
X = np.column_stack((dplam_matris['Gozetim_Skoru'], dplam_matris['Gozetim_Skoru']**2))
X = sm.add_constant(X) 
y = dplam_matris['Haftalik_Verim_Orani']

# En Küçük Kareler (OLS) Motorunun Çalıştırılması
dplam_model = sm.OLS(y, X).fit()

b0 = dplam_model.params.iloc[0]
b1 = dplam_model.params.iloc[1]
b2 = dplam_model.params.iloc[2]

# Türev Alma ve Vertex (Tepe Noktası) Matematiksel Optimizasyonu
optimum_denetim_saati = -b1 / (2 * b2)
maksimum_verim_skoru = b2 * (optimum_denetim_saati ** 2) + b1 * optimum_denetim_saati + b0

print(f"--- DPLAM MODEL SAĞLIĞI VE OPTİMİZASYON RAPORU ---")
print(f"Kurumsal Taban Verim Sabiti (b0): {b0:.2f}")
print(f"Dijital Gözetim Doğrusal İvme Katsayısı (b1): {b1:.2f}")
print(f"Karesel Aşınma ve Stres Ceza Katsayısı (b2): {b2:.4f}")
print(f"--------------------------------------------------")
print(f"Maksimum Verim Sağlayan Optimum Gözetim Sınırı (Vertex): {optimum_denetim_saati:.2f} Saat/Hafta")
