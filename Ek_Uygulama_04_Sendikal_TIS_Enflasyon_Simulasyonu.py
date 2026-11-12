import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Sendika_Zam_Talebi, Kurumsal_Nakit_Akis_Erimi
df = pd.read_excel("sirket_verisi.xlsx")

df['Zam_Karesi'] = df['Sendika_Zam_Talebi'] ** 2
X = sm.add_constant(df[['Sendika_Zam_Talebi', 'Zam_Karesi']])
y = df['Kurumsal_Nakit_Akis_Erimi']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 4: TİS ENFLASYON VE NAKİT AKIŞ SİMÜLASYONU ---")
print(f"Zam Talebi Doğrusal Aşındırma Etkisi (b1): {model.params['Sendika_Zam_Talebi']:.2f} Milyon TL")
print(f"Karesel Bütçe Daralma Katsayısı (b2): {model.params['Zam_Karesi']:.4f}")
print(f"Model İstatistiksel Anlamlılık Derecesi (F-Değeri): {model.fvalue:.2f}")
