import PyPDF2
import pycryptodome


def merge_pdfs(pdf1_path, pdf2_path, output_path):
    try:
        # Abrir los archivos PDF en modo de lectura binaria
        with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
            # Crear objetos PdfFileReader para ambos archivos
            pdf1_reader = PyPDF2.PdfReader(pdf1_file)
            pdf2_reader = PyPDF2.PdfReader(pdf2_file)

            # Crear un objeto PdfFileWriter para el archivo de salida
            pdf_writer = PyPDF2.PdfWriter()

            # Agregar páginas del primer PDF al nuevo PDF
            for page_num in range(len(pdf1_reader.pages)):
                page = pdf1_reader.pages[page_num]
                pdf_writer.addPage(page)

            # Agregar páginas del segundo PDF al nuevo PDF
            for page_num in range(len(pdf2_reader.pages)):
                page = pdf2_reader.pages[page_num]
                pdf_writer.addPage(page)

            # Escribir el nuevo PDF al archivo de salida
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f'La fusión de PDFs se completó con éxito. El nuevo archivo se guardó en: {output_path}')

    except Exception as e:
        print(f"Se produjo un error: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    pdf1_path = r'C:\Dev\Python\DOCs\Doc. contractual _ Iván José Brito _ 13_10_2022 (part 1) - signed.pdf'  # Reemplaza con la ruta de tu primer PDF
    pdf2_path = r'C:\Dev\Python\DOCs\ANEXO_CONTRATO.pdf'  # Reemplaza con la ruta de tu segundo PDF
    output_path = f'C:\Dev\Python\DOCs\contrato.pdf'  # Reemplaza con la ruta del nuevo PDF fusionado

    merge_pdfs(pdf1_path, pdf2_path, output_path)