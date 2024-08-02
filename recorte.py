import fitz  # PyMuPDF
from PIL import Image

def pdf_page_screenshot(pdf_path, page_number, output_image_path, zoom_factor=2):
    # Abrir el documento PDF
    pdf_document = fitz.open(pdf_path)
    
    # Obtener la página específica (número de página comienza desde 0)
    page = pdf_document.load_page(page_number - 1)
    
    # Establecer el factor de zoom (resolución)
    mat = fitz.Matrix(zoom_factor, zoom_factor)
    
    # Renderizar la página en una imagen (pixmap) con el factor de zoom
    pix = page.get_pixmap(matrix=mat)
    
    # Guardar el pixmap como un archivo de imagen
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(output_image_path, "PNG")

# Uso de la función
pdf_path = "/home/samuelperez/Codes/easy_ocr/foo.pdf"
page_number = 1  # Número de la página que deseas capturar
output_image_path = "pantallazo.png"
zoom_factor = 3  # Factor de zoom para aumentar la resolución

pdf_page_screenshot(pdf_path, page_number, output_image_path, zoom_factor)
