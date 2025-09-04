import fitz  # PyMuPDF
import argparse

parser = argparse.ArgumentParser(description='pdf cleaner')
parser.add_argument("-i", "--input", type=str, help="Введите путь до файла: ")
args = parser.parse_args()

if args.input:
    inputPdfPath = args.input
    outputPdfPath = args.input.split('.pdf')[0] + '_cleaned.pdf'
else:
    inputPdfPath = input("Введите путь до файла: ")
    outputPdfPath = inputPdfPath.split('.pdf')[0] + '_cleaned.pdf'


def remove_images(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    for page in doc:
        img_list = page.get_images()
        page.delete_image(img_list[-1][0])

    doc.save(output_pdf)


remove_images(inputPdfPath, outputPdfPath)
