import pandas as pd
from docx import Document

def parse_file(file, filetype):
    filetype = filetype.lower()
    
    # CSV
    if filetype in ['csv']:
        return pd.read_csv(file)
    
    # XLSX (Excel files)
    elif filetype == 'xlsx':
        return pd.read_excel(file)
    
    # XML (XML files)
    elif filetype == 'xml':
        return pd.read_xml(file)
    

    # Unsupported file type
    else:
        raise ValueError(f"Unsupported file type: {filetype}")
