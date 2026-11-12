import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Mentorluk_Seans_Sayisi, Yonetici_Olma_Suresi_Yil
df = pd.read_excel("sirket_verisi.xlsx")

kor_ment = df['Mentorluk_Seans_Sayisi'].corr(df['Yonetici_Olma_Suresi_Yil'])

print("--- UYGULAMA 39: MENTORLUK VE YÖNETİCİ OLMA SÜRESİ ---")
print(f"Mentorluk Seansı & Yönetici Olma Süresi Korelasyonu: {kor_ment:.4f}")
