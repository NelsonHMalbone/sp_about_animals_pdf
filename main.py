import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# import data using glob
filepaths = glob.glob('animals/*.txt')
# creates pdf file
pdf = FPDF(orientation='p', unit='mm', format='A4')
# looping over files to create multiple pdfs
for filepath in filepaths:
    # add page to pdf
    pdf.add_page()
    #get file name with out extension
    df = pd.read_csv(filepath)
    # creating Header PDF
    filename = Path(filepath).stem
    # converts file name to cap
    name = filename.title()
    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=0, h=12, txt=name, align='L', ln=1)
    # gather content from pdf
    with open(filepath, 'r') as file:
        content = file.read()
    # adds content to pdf
    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# output
pdf.output('output.pdf')