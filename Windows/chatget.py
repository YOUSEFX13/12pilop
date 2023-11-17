import os
import glob

import g4f

from g4f.Provider import Bard

from docx import Document





def get_desktop_folder():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def find_docx_files():
    desktop_folder = get_desktop_folder()
    docx_files = glob.glob(os.path.join(desktop_folder, '*.docx'))
    return docx_files



def detect_titles(docx_path, title_style="Title"):
    document = Document(docx_path)

    titles = []

    for paragraph in document.paragraphs:
        if paragraph.style.name == title_style:
            titles.append(paragraph.text)

    return titles


# Example usage

def chatget():
   


    path = find_docx_files()[0]
    #print(path)
    
    titles = detect_titles(path, title_style="Title")
    #print(titles[0])


    response = g4f.ChatCompletion.create(
       model="gpt-3.5-turbo",
       provider=Bard,
       messages=[{"role": "user", "content": titles[0]}],
       auth=True,
    )  # Alternative model setting


    return response
