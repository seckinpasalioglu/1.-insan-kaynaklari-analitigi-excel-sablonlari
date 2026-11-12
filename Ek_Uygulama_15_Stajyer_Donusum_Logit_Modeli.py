import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Mentor_Degerlendirme_Puani, Kadroya_Gecti_Mi
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Mentor_Degerlendirme_Puani'])
y = df['Kadroya_Gecti_Mi']

model = sm.Logit(y, X).fit()

print("--- UYGULAMA 15: STAJYER LOGİT DÖNÜŞÜM ANALİZİ ---")
print(f"Mentör Puanının Log-Odds Katsayısı (b1): {model.params['Mentor_Degerlendirme_Puani']:.4f}")
print(f"Model Başarı Gücü (Pseudo R-Kare): %{model.prsquared * 100:.1f}")
