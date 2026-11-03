#for this code to work, make sure you are using visual studio code and you are in the right folder within the terminal. The comment section is to create a file in case that you need to, most times, it will be created already. just change the names of the files in lines 15 and 18 always respecting the .pdf file extension
from pypdf import PdfWriter

#pdf_writer = PdfWriter()
#pdf_writer.add_blank_page(595.28, 841.89)

#with open("pdf1.pdf", "wb") as f:
#    pdf_writer.write(f)

#with open("pdf2.pdf", "wb") as f:
#    pdf_writer.write(f)

pdf_merger = PdfWriter()

with open("exercise_1v2.pdf", 'rb') as file1:
    pdf_merger.append(file1)

with open("exercise_2v2.pdf", 'rb') as file2:
    pdf_merger.append(file2)

with open("unidos.pdf", 'wb') as output_file:
    pdf_merger.write(output_file)
