import fitz  # PyMuPDF
import argparse

parser = argparse.ArgumentParser(description='pdf cleaner')
parser.add_argument('input_pdf_path', type=str, help='Введите путь до файла: ')
args = parser.parse_args()


def remove_images(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_images()
        page.delete_image(img_list[-1][0])

    doc.save(output_pdf)


input_pdf_path = args.input_pdf_path
output_pdf_path = args.input_pdf_path.split('.pdf')[0] + '_cleaned.pdf'

remove_images(input_pdf_path, output_pdf_path)
