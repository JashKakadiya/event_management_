import os
import pdfkit
import threading

# set path to wkhtmltopdf executable

# define function to convert a portion of the HTML file to PDF
def convert_part_to_pdf(html_part, pdf_file):
    pdfkit.from_string(html_part, pdf_file)

# define function to convert the HTML file to PDF using multi-threading
def convert_html_to_pdf(html_file, num_threads):
    # read the HTML file
    with open(html_file, 'r') as f:
        html = f.read()

    # calculate the number of parts to split the HTML file into
    num_parts = num_threads

    # split the HTML file into parts
    html_parts = [html[i::num_parts] for i in range(num_parts)]

    # create a list of corresponding PDF file names
    pdf_files = [os.path.splitext(html_file)[0] + '_' + str(i) + '.pdf' for i in range(num_parts)]

    # create a list of file pairs
    file_pairs = list(zip(html_parts, pdf_files))

    # set the number of threads
    num_threads = min(num_threads, len(file_pairs))

    # divide the file pairs into batches
    file_batches = [file_pairs[i:i+num_threads] for i in range(0, len(file_pairs), num_threads)]

    # create threads for each batch
    threads = [threading.Thread(target=convert_batch_to_pdf, args=(batch,)) for batch in file_batches]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

    # merge the PDF files
    merge_pdf_files(pdf_files, os.path.splitext(html_file)[0] + '.pdf')

# define function to convert a batch of HTML parts to PDF
def convert_batch_to_pdf(batch):
    for html_part, pdf_file in batch:
        convert_part_to_pdf(html_part, pdf_file)

# define function to merge multiple PDF files into a single file
# define function to merge multiple PDF files into a single file
# import the logging module
import logging

import os
import PyPDF2

# define function to merge multiple PDF files into a single file
def merge_pdf_files(input_files, output_file):
    # create a new PDF writer object
    writer = PyPDF2.PdfWriter()

    # iterate over the input PDF files and add each page to the writer object
    for input_file in input_files:
        with open(input_file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                writer.add_page(page)

    # write the merged PDF to the output file
    with open(output_file, 'wb') as f:
        writer.write(f)



# convert the HTML file to PDF using 4 threads
convert_html_to_pdf(os.path.abspath('templates/frontend/invoice.html/')  , 2)

