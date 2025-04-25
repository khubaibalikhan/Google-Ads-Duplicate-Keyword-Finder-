import pandas as pd
from docx import Document

def parse_file(file, filetype):
    if filetype == 'csv':
        return pd.read_csv(file)
