import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# 180 satış temsilcisi için holding veri simülasyonu başlatılıyor
np.random.seed(42)
n_temsilci = 180

# Kukla değişkenlerin (Dummy) kurgulanması
# Her temsilcinin eğitim öncesi (0) ve eğitim sonrası (1) ikişer satır kaydı simüle edilir
egitim_grubu = np.repeat(np.random.choice([0, 1], size=n_temsilci), 2)
zaman_donemi = np.tile([0, 1], n_temsilci)

# b3 etkileşim katsayısı (28.50 Bin TL) formüle enjekte ediliyor
ciro = 450.0 + (15.0 * egitim_grubu) + (85.0 * zaman_donemi) + (28.50 * egitim_grubu * zaman_donemi) + np.random.normal(0, 10, n_temsilci * 2)

# Veri çerçevesinin birleştirilmesi
did_matris = pd.DataFrame({
    'Temsilci_ID': np.repeat(np.arange(1001, 1001 + n_temsilci), 2),
    'Egitim_Grubu': egitim_grubu,
    'Zaman_Donemi': zaman_donemi,
    'Aylik_Ciro_Hacmi': ciro
})

# Egzersiz şablonu olarak okuyucunun indirmesi için Excel formatında kaydediliyor
did_matris.to_excel("tedid_egitim_veri_egzersizi.xlsx", index=False)

# Statsmodels OLS Motoru ile Farkların Farkı Regresyonunun Çalıştırılması
model_formulu = "Aylik_Ciro_Hacmi ~ Egitim_Grubu * Zaman_Donemi"
did_model = smf.ols(formula=model_formulu, data=did_matris).fit()

b2 = did_model.params.iloc[2]  # Piyasa Doğal Büyüme Etkisi
b3 = did_model.params.iloc[3]  # Saf TEDID Etkisi

# ROI Hesaplama Paneli
toplam_maliyet = 2000.0  # 2.000.000 TL bütçe
toplam_saf_getiri = b3 * n_temsilci
net_kar_tasarruf = toplam_saf_getiri - toplam_maliyet
net_roi_yuzdesi = (net_kar_tasarruf / toplam_maliyet) * 100

print(f"--- TEDID MODEL ETKİ DEĞERLEME VE ROI RAPORU ---")
print(f"Piyasa/Zaman Kaynaklı Doğal Ciro Artış Etkisi (b2): {b2:.2f} Bin TL")
print(f"Eğitimin Temsilci Başına SAF NET Ciro Katkısı (b3): {b3:.2f} Bin TL")
print(f"--------------------------------------------------")
print(f"Holding Genelinde Sağlanan Toplam Brüt Getiri : {toplam_saf_getiri:.2f} Bin TL")
print(f"Eğitim Bütçesi Düşüldükten Sonra Kalan Net Kâr: {net_kar_tasarruf:.2f} Bin TL")
print(f"İleri İkna Akademisi Onaylı Net Finansal ROI  : %{net_roi_yuzdesi:.1f}")
