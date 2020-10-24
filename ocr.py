import os, io
from google.cloud import vision
from google.cloud.vision_v1.types.image_annotator import Image
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"MyFirstProject-da5d6b04be74.json"

def getString():
    client = vision.ImageAnnotatorClient()

    image_path = 'static/img.png'

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = Image(content=content)
    response = client.document_text_detection(image=image)
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

if __name__ == "__main__":
    getString()