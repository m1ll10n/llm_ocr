import easyocr
import os


def extract_text(file: str):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(os.path.join("/app/sample_input", file))

    texts = []
    for i in result:
        _, text, _ = i
        texts.append(text)

    return " ".join(texts)
