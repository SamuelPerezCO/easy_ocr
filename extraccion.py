import fitz  # PyMuPDF
import easyocr
import numpy as np
from PIL import Image

def extract_text_from_pdf(pdf_path, zoom_factor=2):
    # Inicializar el lector de easyocr
    reader = easyocr.Reader(['en'])  # Puedes agregar más idiomas si es necesario
    pdf_document = fitz.open(pdf_path)
    texts = []
    
    # Convertir cada página a una imagen y extraer el texto
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        mat = fitz.Matrix(zoom_factor, zoom_factor)
        pix = page.get_pixmap(matrix=mat)
        
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_np = np.array(img)
        
        result = reader.readtext(img_np)
        page_text = "\n".join([text[1] for text in result])
        texts.append(page_text)
    
    return texts

# Uso de la función
pdf_path = "/home/samuelperez/Codes/easy_ocr/pantallazo.png"
texts = extract_text_from_pdf(pdf_path)

# Imprimir el texto extraído de cada página
for i, text in enumerate(texts):
    print(f"Texto de la página {i + 1}:\n{text}\n")
