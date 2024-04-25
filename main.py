import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# import data using glob
filepaths = glob.glob('animals/*.txt')
# looping over files to create multiple pdfs
for filepath in filepaths:
    df = pd.read_csv(filepath)
    # print(df)

    filename = Path(filepath).stem
    # print(filename)

    # creating Header PDF
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=0, h=12, txt=f'{filename}'.capitalize(), align='L')
    pdf.output(f'PDFs/{filename}.pdf')
