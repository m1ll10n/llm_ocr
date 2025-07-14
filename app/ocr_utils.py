import easyocr
import os


def extract_text(file: str):
    reader = easyocr.Reader(
        ["en"],
        gpu=False,
        model_storage_directory="./models/ocr",
        download_enabled=False,
    )
    result = reader.readtext(os.path.join("./sample_input", file))

    texts = []
    for i in result:
        _, text, _ = i
        texts.append(text)

    return " ".join(texts)
