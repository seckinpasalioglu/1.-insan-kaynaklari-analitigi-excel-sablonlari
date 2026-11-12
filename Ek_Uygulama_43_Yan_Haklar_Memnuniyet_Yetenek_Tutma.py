import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Yan_Hak_Memnuniyet_Skoru, Yetenek_Tutma_Yuzde
df = pd.read_excel("sirket_verisi.xlsx")

kor_yanhak = df['Yan_Hak_Memnuniyet_Skoru'].corr(df['Yetenek_Tutma_Yuzde'])

print("--- UYGULAMA 43: YAN HAKLAR MEMNUNİYETİ VE YETENEK TUTMA ---")
print(f"Yan Hak Memnuniyeti & Yetenek Tutma Korelasyonu: {kor_yanhak:.4f}")
