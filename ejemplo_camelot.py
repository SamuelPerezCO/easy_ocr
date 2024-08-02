import camelot

# Leer el PDF de ejemplo
tables = camelot.read_pdf('/home/samuelperez/Codes/easy_ocr/foo.pdf')

# Guardar cada tabla extraída en archivos CSV separados
for i, table in enumerate(tables):
    csv_filename = f'tabla_{i+1}.csv'
    table.to_csv(csv_filename)
    print(f'Tabla {i+1} guardada en {csv_filename}')
