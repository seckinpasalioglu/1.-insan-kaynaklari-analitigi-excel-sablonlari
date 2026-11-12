import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Sirkette_Kidem_Yili, Yasal_Tazminat_Karsiligi
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Sirkette_Kidem_Yili'])
y = df['Yasal_Tazminat_Karsiligi']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 5: KIDEM TAZMİNATI KARŞILIKLARI ANALİZİ ---")
print(f"Kıdem Başına Yıllık Ek Tazminat Yükü (b1): {model.params['Sirkette_Kidem_Yili']:.2f} Bin TL")
print(f"Katsayı Güvenilirlik Testi (t-İstatistiği): {model.tvalues['Sirkette_Kidem_Yili']:.2f}")
