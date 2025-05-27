
# LLM + OCR
Tech Stack:
- Flask + Gunicorn
- OCR: EasyOCR
- LLM: DeepSeek-V3
- Docker Compose


Starting the app:
- git clone https://github.com/m1ll10n/llm_ocr
- cd llm_ocr
- create .env by copying from .env.example on same folder and must fill the DEEPSEEK_API_KEY
- docker compose up --build

Testing the endpoint:
- File should be uploaded in base64 encoded .png format inside sample_input and must change accordingly to file in body: {"file": "new_file.png"}

```console
$ curl -X POST http://hpc-linux-1104:8000/extract -H "Content-Type: application/json" -d '{"file": "license.png"}'
```

Expected output:
```console
{
    "dln": "A9999999",
    "exp": "02/21/2018",
    "family_name": "JONES",
    "given_name": "ASEHENA",
    "address": "1234 COMMODORE JOSHUA BARNEY DRIVE, NE #1234 1 WASHINGTON, DC OOO00-0000",
    "sex": "E",
    "height": "5-02",
    "weight": "120",
    "eyes": "BRO",
    "dob": "02/21/1984",
    "class": "D",
    "iss": "02/17/2010",
    "endorsements": "NONE",
    "restrictions": "VETERAN"
}
```
