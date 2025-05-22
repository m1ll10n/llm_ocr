from openai import OpenAI
from pydantic import BaseModel
from datetime import date

client = OpenAI(api_key="", base_url="")


system_prompt = """
The user will provide text. Please parse the details into key-value pair and output them in JSON format.

EXAMPLE INPUT:
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "uid": "NR-019231",
    "title": "Certificate Title",
    "name": "Student Name",
    "course": "Course in Business Management",
    "issuer": "UKM school of business",
    "date": "23.04.2019"
}
"""

completion = client.chat.completions.create(
    model="",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "some data"},
    ],
    response_format={"type": "json_object"},
)

event = completion.choices[0].message.content

print(event)
