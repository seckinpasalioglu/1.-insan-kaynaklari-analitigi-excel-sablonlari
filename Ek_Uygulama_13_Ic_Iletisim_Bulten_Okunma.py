import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Kelime_Sayisi, Okunma_Tamamlama_Orani
df = pd.read_excel("sirket_verisi.xlsx")

df['Kelime_Karesi'] = df['Kelime_Sayisi'] ** 2
X = sm.add_constant(df[['Kelime_Sayisi', 'Kelime_Karesi']])
y = df['Okunma_Tamamlama_Orani']

model = sm.OLS(y, X).fit()
b1 = model.params['Kelime_Sayisi']
b2 = model.params['Kelime_Karesi']
optimum_kelime = -b1 / (2 * b2)

print("--- UYGULAMA 13: İÇ İLETİŞİM BÜLTEN OPTİMİZASYONU ---")
print(f"Okunma Oranını Zirveye Taşıyan İdeal İçerik Uzunluğu: {optimum_kelime:.2f} Kelime")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
