import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Analitik_Yatirim_Butcesi, Yillik_Kurumsal_Net_Tasarruf
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Analitik_Yatirim_Butcesi'])
y = df['Yillik_Kurumsal_Net_Tasarruf']

model = sm.OLS(y, X).fit()
b0 = model.params['const']
b1 = model.params['Analitik_Yatirim_Butcesi']

ornek_maliyet = 150.0
toplam_getiri = b0 + (b1 * ornek_maliyet)
net_roi_orani = ((toplam_getiri - ornek_maliyet) / ornek_maliyet) * 100

print("--- UYGULAMA 20: İK ANALİTİĞİ ROI MODELİ ---")
print(f"Yatırım Başına Tasarruf Üretim Katsayısı (b1): {b1:.2f}")
print(f"150 Bin TL Yatırım İçin Projekte Edilen Net ROI: %{net_roi_orani:.1f}")
