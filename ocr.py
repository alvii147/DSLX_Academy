import os, io
from google.cloud import vision
from google.cloud.vision_v1.types.image_annotator import Image
import pandas as pd
from py_common_subseq import find_common_subsequences

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"MyFirstProject-da5d6b04be74.json"

def getData(image_path):
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    return response

def processData(response):
    symbolsData = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        symbolsData.append((symbol.text, symbol.confidence))
    word = ""
    for i in symbolsData:
        word += i[0]
    return word, symbolsData

def assess(origWord, writtenWord):
    lcs = max(find_common_subsequences(origWord, writtenWord), key=len)
    i = 0
    j = 0
    retList = []
    while i < len(lcs):
        if lcs[i] == origWord[j]:
            retList.append((origWord[j], 1))
            i += 1
        else:
            retList.append((origWord[j], 0))
        j += 1
    return retList

if __name__ == "__main__":
    writtenWord, characters = processData(getData('static/img2.png'))
    print(assess("Pronounciation", writtenWord))