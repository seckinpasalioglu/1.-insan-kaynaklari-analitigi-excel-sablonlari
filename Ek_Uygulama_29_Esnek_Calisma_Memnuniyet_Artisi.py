import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Uzaktan_Calisma_Gun, Memnuniyet_Skoru
df = pd.read_excel("sirket_verisi.xlsx")

ozet_memnuniyet = df.groupby('Uzaktan_Calisma_Gun')['Memnuniyet_Skoru'].agg(['count', 'mean'])
kor_esnek = df['Uzaktan_Calisma_Gun'].corr(df['Memnuniyet_Skoru'])

print("--- UYGULAMA 29: ESNEK ÇALIŞMA VE MEMNUNİYET ANALİZİ ---")
print(ozet_memnuniyet)
print(f"Uzaktan Çalışma & İş Memnuniyeti Korelasyonu: {kor_esnek:.4f}")
