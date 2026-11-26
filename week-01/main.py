
import os


def read_notes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_lines(text):
    return len(text.splitlines())


def count_paragraphs(text):
    paragraphs = text.split("\n\n")

    non_empty_paragraphs = [
        paragraph for paragraph in paragraphs
        if paragraph.strip()
    ]

    return len(non_empty_paragraphs)


def count_keyword(text, keyword):
    return text.lower().count(keyword.lower())


def save_report(report):
    os.makedirs("output", exist_ok=True)

    with open("output/analysis_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport saved successfully!")


def main():
    filename = "sample_notes.txt"

    try:
        content = read_notes(filename)

        print("\n===== STUDY NOTES =====")
        print("-----------------------")
        print(content)

        print("\n===== NOTES ANALYSIS =====")

        characters = count_characters(content)
        words = count_words(content)
        lines = count_lines(content)
        paragraphs = count_paragraphs(content)

        print("Total Characters:", characters)
        print("Total Words:", words)
        print("Total Lines:", lines)
        print("Total Paragraphs:", paragraphs)

        keyword = input("\nEnter a keyword to search: ")

        keyword_count = count_keyword(content, keyword)

        print("Keyword:", keyword)
        print("Keyword Occurrences:", keyword_count)

        report = f"""
===== STUDY NOTES ANALYSIS =====

Characters: {characters}
Words: {words}
Lines: {lines}
Paragraphs: {paragraphs}

Keyword: {keyword}
Keyword Occurrences: {keyword_count}
"""

        save_report(report)

    except FileNotFoundError:
        print("\nError: sample_notes.txt was not found.")
        print("Please place the file in the week-01 folder.")


if __name__ == "__main__":
    main()
