import easyocr


def extract_text(file_path: str):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path)

    texts = []
    for i in result:
        _, text, _ = i
        texts.append(text)

    return " ".join(texts)
