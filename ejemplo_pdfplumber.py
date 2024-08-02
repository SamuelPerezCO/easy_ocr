import pdfplumber

# Leer el PDF
with pdfplumber.open('/home/samuelperez/Codes/easy_ocr/foo.pdf') as pdf:
    page = pdf.pages[0]
    table = page.extract_table()

# Convertir a DataFrame de pandas
import pandas as pd
df = pd.DataFrame(table[1:], columns=table[0])

# Guardar en un archivo CSV
df.to_csv('tabla.csv', index=False)
