from openai import OpenAI
import os
import json
from dotenv import load_dotenv


load_dotenv()


def generate_json(text: str):

    if not text:
        raise ValueError

    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    )

    system_prompt = """
    The user will provide text containing driver's license. Please parse the details into key-value pair and output them in JSON format. Leave the value to null if there's not enough information.

    EXAMPLE JSON OUTPUT:
    {
        "dln": "A129074192",
        "exp": "03/25/2025",
        "family_name": "WAN",
        "given_name": "UMAR",
        "address": "NO 2, JLN TANAH MERAH, 40000 SHAH ALAM, SELANGOR",
        "sex": "M",
        "height": "5-10",
        "weight": "185",
        "eyes": "BLUE",
        "dob": "02/24/1999",
        "class": "C",
        "iss": "03/25/2015",
        "endorsements": "NONE",
        "restrictions": "5"
    }
    """

    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )

    event = completion.choices[0].message.content
    json_event = json.loads(event)

    return json_event
