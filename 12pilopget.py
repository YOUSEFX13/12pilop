import time

import g4f

from g4f.Provider import Bard

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

# print("Detected Titles:")
# for title in titles:
#    print(title)

niga = time.time()

anan = titles[0]

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=Bard,
    messages=[{"role": "user", "content": anan}],
    auth=True,
)  # Alternative model setting

print(response)


sui = time.time()
print(sui - niga)  # prints the response from chatGPTpip install setuptools


with open("sui.txt", "w") as f:
    f.write(response)

    print("zenci")
    f.close
