import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Performans_Skoru, PIP_Durumu
df = pd.read_excel("sirket_verisi.xlsx")

ozet_pip = df.groupby('PIP_Durumu')['Performans_Skoru'].agg(['count', 'min', 'max', 'mean'])

print("--- UYGULAMA 26: PIP PERFORMANS EŞİK ANALİZİ ---")
print(ozet_pip)
