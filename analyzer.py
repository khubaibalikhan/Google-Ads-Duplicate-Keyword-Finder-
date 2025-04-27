# analyzer.py

import re

def normalize_keyword(keyword):
    """Lowercase and remove extra spaces and symbols."""
    keyword = keyword.lower()
    keyword = re.sub(r'\s+', ' ', keyword)  # Replace multiple spaces with one
    keyword = re.sub(r'[^\w\s]', '', keyword)  # Remove special characters
    return keyword.strip()


def exact_match_duplicates(keywords):
    """Find exact duplicates (after normalization)."""
    seen = {}
    duplicates = {}

    for idx, keyword in enumerate(keywords):
        norm_keyword = normalize_keyword(keyword)
        if norm_keyword in seen:
            # If already seen, it's a duplicate
            if norm_keyword not in duplicates:
                duplicates[norm_keyword] = [seen[norm_keyword]]  # store first occurrence
            duplicates[norm_keyword].append(idx)
        else:
            seen[norm_keyword] = idx
    
    return duplicates


def loose_match_duplicates(keywords, threshold=0.7):
    """Find loose duplicates based on word set similarity."""
    normalized_keywords = [normalize_keyword(k) for k in keywords]
    checked = set()
    duplicates = {}

    for i, kw1 in enumerate(normalized_keywords):
        if i in checked:
            continue

        words1 = set(kw1.split())

        for j in range(i + 1, len(normalized_keywords)):
            if j in checked:
                continue

            words2 = set(normalized_keywords[j].split())

            if not words1 or not words2:
                continue

            overlap = len(words1 & words2) / len(words1 | words2)

            if overlap >= threshold:
                key = keywords[i]  # Use original keyword as main one
                if key not in duplicates:
                    duplicates[key] = []
                duplicates[key].append(keywords[j])

                checked.add(j)

    return duplicates


def analyze_keywords(keywords):
    """Main function to ask user and find duplicates."""
    mode = input("Do you want exact match duplicates? (yes/no): ").strip().lower()

    if mode == 'yes':
        duplicates = exact_match_duplicates(keywords)
    else:
        duplicates = loose_match_duplicates(keywords)

    if not duplicates:
        print("No duplicates found.")
        return

    print("\nFound Duplicates:")
    for main_kw, dup_list in duplicates.items():
        print(f"'{main_kw}' has duplicates:")
        for dup in dup_list:
            print(f"   -> {dup}")
