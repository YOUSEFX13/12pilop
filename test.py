from docx import Document


def detect_titles(docx_path, title_style="Title"):
    document = Document(docx_path)

    titles = []

    for paragraph in document.paragraphs:
        if paragraph.style.name == title_style:
            titles.append(paragraph.text)

    return titles


# Example usage
docx_path = "zenci.docx"
titles = detect_titles(docx_path, title_style="Title")

print("Detected Titles:")
for title in titles:
    print(title)
