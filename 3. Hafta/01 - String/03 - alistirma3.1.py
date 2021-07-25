"""Aşağıdaki satırın sonundaki sayıyı çıkarmak için find ()  ve dizi dilimlemeyi (bkz. Bölüm 6.10) kullanarak kod yazın. 
Çıkarılan değeri kayan noktalı sayıya dönüştürün ve yazdırın.
"""

text = "X-DSPAM-Confidence:    0.8475";
indexNumarasi = text.find(".")
yeniNumara = float(text[indexNumarasi-1:])
print(type(yeniNumara))
print(yeniNumara)