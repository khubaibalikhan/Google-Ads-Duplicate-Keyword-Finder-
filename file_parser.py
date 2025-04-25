import pandas as pd
from docx import Document

def parse_file(file, filetype):
    if filetype == 'csv':
        return pd.read_csv(file)
    elif filetype == 'docx':
        doc = Document(file)  # Loading the Word file
        data = []
        for table in doc.tables:
            for row in table.rows:
                data.append([cell.text.strip() for cell in row.cells])
        return pd.DataFrame(data[1:], columns=data[0])

