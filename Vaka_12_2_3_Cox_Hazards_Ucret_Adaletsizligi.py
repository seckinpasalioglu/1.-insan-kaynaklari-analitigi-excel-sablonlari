import numpy as np
import pandas as pd
from lifelines import CoxPHFitter

# 120 yazılım mühendisi için süreç sağkalım verisi simülasyonu
np.random.seed(42)
n_muhendis = 120
gini_sapmasi = np.random.uniform(-20, 20, n_muhendis)

# Süreç analizi risk katsayısı yerleştiriliyor
kalma_suresi = np.exp(3.0 - (0.1484 * gini_sapmasi)) + np.random.exponential(5, n_muhendis)
kalma_suresi = np.clip(kalma_suresi, 1, 48)  # Hizmet süresi aylık bazda sınırlandırılıyor
istifa_olayi = np.where(gini_sapmasi < 0, np.random.choice([0, 1], size=n_muhendis, p=[0.3, 0.7]), np.random.choice([0, 1], size=n_muhendis, p=[0.8, 0.2]))

cox_matris = pd.DataFrame({
    'Personel_ID': np.arange(2001, 2001 + n_muhendis),
    'Sirkette_Kalma_Suresi': kalma_suresi,
    'Istifa_Olayi': istifa_olayi,
    'Gini_Sapmasi': gini_sapmasi
})

# Egzersiz şablonu olarak okuyucunun indirmesi için Excel formatında kaydediliyor
cox_matris.to_excel("cox_ucret_sagkalim_egzersizi.xlsx", index=False)

# Model matris düzenlemesi
df_cox = cox_matris[['Sirkette_Kalma_Suresi', 'Istifa_Olayi', 'Gini_Sapmasi']]

# Lifelines kütüphanesi motoruyla Cox modelinin koşturulması
cph = CoxPHFitter()
cph.fit(df_cox, duration_col='Sirkette_Kalma_Suresi', event_col='Istifa_Olayi')

print("--- COX PROPORTIONAL HAZARDS MODEL SONUÇLARI ---")
print(f"Concordance (Uyum İndeksi) Başarı Notu: {cph.concordance_index_:.2f}")
print(f"Risk Katsayısı (coef): {cph.params.loc['Gini_Sapmasi']:.4f}")
print(f"Anlık İstifa Risk Çarpanı (Hazard Ratio): {np.exp(cph.params.loc['Gini_Sapmasi']):.4f}")
