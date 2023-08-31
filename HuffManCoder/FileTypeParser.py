import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        with open(txt_path, 'w') as txt_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                txt_file.write(text)

def txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, 'r') as txt_file:
        text = txt_file.read()

    writer = PyPDF2.PdfWriter()

    page = writer.add_blank_page(width=612, height=792)  # Set page size to letter size (8.5 x 11 inches)
    page.merge_page(PyPDF2.pdf.PageObject.create_from_text(text))

    with open(pdf_path, 'wb') as pdf_file:
        writer.write(pdf_file)

# Example usage
pdf_path = 'some.pdf'
txt_path = 'output.txt'
converted_pdf_path = 'output.pdf'

# Convert PDF to text
pdf_to_txt(pdf_path, txt_path)

# Convert text back to PDF
txt_to_pdf(txt_path, converted_pdf_path)
