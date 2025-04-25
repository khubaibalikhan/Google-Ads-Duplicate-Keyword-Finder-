from file_parser import parse_file

# Test CSV
with open("sample.csv", "r") as f:
    df_csv = parse_file(f, "csv")
    print("CSV Output:")
    print(df_csv.head())