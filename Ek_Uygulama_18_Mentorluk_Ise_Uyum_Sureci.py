import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Mentorluk_Suresi_Hafta, Tam_Uyum_Suresi_Gun
df = pd.read_excel("sirket_verisi.xlsx")

df['Mentor_Karesi'] = df['Mentorluk_Suresi_Hafta'] ** 2
X = sm.add_constant(df[['Mentorluk_Suresi_Hafta', 'Mentor_Karesi']])
y = df['Tam_Uyum_Suresi_Gun']

model = sm.OLS(y, X).fit()
b1 = model.params['Mentorluk_Suresi_Hafta']
b2 = model.params['Mentor_Karesi']
optimum_mentor = -b1 / (2 * b2)

print("--- UYGULAMA 18: MENTÖRLÜK SÜREÇ OPTİMİZASYONU ---")
print(f"Uyum Süresini Minimuma İndiren İdeal Mentörlük: {optimum_mentor:.2f} Hafta")
print(f"Model Açıklama Gücü (R-Kare): %{model.rsquared * 100:.1f}")
