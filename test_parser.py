from file_parser import parse_file

# CSV
with open("sample.csv", "r") as f:
    df_csv = parse_file(f, "csv")
    print("CSV:\n", df_csv.head())


# XLSX
df_xlsx = parse_file("sample.xlsx", "xlsx")
print("XLSX:\n", df_xlsx.head())

# XML
df_xml = parse_file("sample.xml", "xml")
print("XML:\n", df_xml.head())

