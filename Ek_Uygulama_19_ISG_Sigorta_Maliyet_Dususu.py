import pandas as pd
import statsmodels.api as sm

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Yillik_Isg_Faaliyet_Adeti, Sigorta_Prim_Maliyet_Dususu
df = pd.read_excel("sirket_verisi.xlsx")

X = sm.add_constant(df['Yillik_Isg_Faaliyet_Adeti'])
y = df['Sigorta_Prim_Maliyet_Dususu']

model = sm.OLS(y, X).fit()

print("--- UYGULAMA 19: İSG SİGORTA MALİYET ANALİZİ ---")
print(f"Faaliyet Başına Yıllık Net Prim Tasarrufu (b1): {model.params['Yillik_Isg_Faaliyet_Adeti']:.2f} Bin TL")
print(f"Model Katsayı Güvenilirliği (t-İstatistiği): {model.tvalues['Yillik_Isg_Faaliyet_Adeti']:.2f}")
