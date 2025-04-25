from file_parser import parse_file

# CSV
with open("test_files/sample.csv", "r") as f:
    df_csv = parse_file(f, "csv")
    print("CSV:\n", df_csv.head())

# TSV
with open("test_files/sample.tsv", "r") as f:
    df_tsv = parse_file(f, "tsv")
    print("TSV:\n", df_tsv.head())

# XLSX
df_xlsx = parse_file("test_files/sample.xlsx", "xlsx")
print("XLSX:\n", df_xlsx.head())

# XML
df_xml = parse_file("test_files/sample.xml", "xml")
print("XML:\n", df_xml.head())

# DOCX
df_docx = parse_file("test_files/sample.docx", "docx")
print("DOCX:\n", df_docx.head())
