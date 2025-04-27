# main.py

from file_parser import parse_file
from analyzer import analyze_keywords

def main():
    filepath = input("Enter your file path: ").strip()
    filetype = filepath.split('.')[-1]

    # Parse the file
    df = parse_file(filepath, filetype)

    print("\nColumns detected:")
    print(list(df.columns))

    # Ask user to pick column
    column = input("Enter the column name that contains keywords: ").strip()

    if column not in df.columns:
        print("Invalid column name.")
        return

    # Get keywords list
    keywords = df[column].dropna().tolist()

    # Analyze keywords
    analyze_keywords(keywords)

if __name__ == "__main__":
    main()
