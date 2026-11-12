import pandas as pd

# Okuyucunun kendi Excel dosyasını otomatik okur
# Gerekli Excel Sütunları: Tesvik_Tutari_TL, Anket_Katilim_Yuzdesi
df = pd.read_excel("sirket_verisi.xlsx")

kor_dusuk_odul = df[df['Tesvik_Tutari_TL'] < 250]['Tesvik_Tutari_TL'].corr(df['Anket_Katilim_Yuzdesi'])
kor_yuksek_odul = df[df['Tesvik_Tutari_TL'] >= 250]['Tesvik_Tutari_TL'].corr(df['Anket_Katilim_Yuzdesi'])

print("--- UYGULAMA 33: ANKET TEŞVİK VE TAVAN SINIRI ANALİZİ ---")
print(f"250 TL Altı Ödüllerde Korelasyon: {kor_dusuk_odul:.4f}")
print(f"250 TL ve Üstü Ödüllerde Korelasyon (Tavan Kırılması): {kor_yuksek_odul}")
