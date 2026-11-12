import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Disiplin_Uyari_Sayisi, Kritik_Is_Hatasi_Sayisi
df = pd.read_excel("sirket_verisi.xlsx")

df['Uyari_Karesi'] = df['Disiplin_Uyari_Sayisi'] ** 2
X = sm.add_constant(df[['Disiplin_Uyari_Sayisi', 'Uyari_Karesi']])
y = df['Kritik_Is_Hatasi_Sayisi']

model = sm.OLS(y, X).fit()
b1 = model.params['Disiplin_Uyari_Sayisi']
b2 = model.params['Uyari_Karesi']
optimum_uyari = -b1 / (2 * b2)

print("--- UYGULAMA 16: DİSİPLİN ERKEN UYARI ANALİZİ ---")
print(f"Caydırıcılığın Zirve Yaptığı Optimum Uyarı Sınırı: {optimum_uyari:.2f} Adet")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
