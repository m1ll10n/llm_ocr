Running the app:
- cd app
- gunicorn -b 0.0.0.0:8000 app:app

need /extract endpoint

example request
{
  "file_base64": "<BASE64_ENCODED_PNG_OR_PDF>"
}

* file must be simulated from document/certificate (transcript, diploma, license)
sample must be included in repo

----------------------------------------------------------------------

expected output
* extracted key-value fields
{
  "Name": "John Doe",
  "DateOfBirth": "April 5, 1995",
  "Program": "Bachelor of Engineering in Computer Science",
  "Institution": "University of AI",
  "StartDate": "September 2017",
  "CompletionDate": "June 2021",
  "CertificateNo": "123456789"
}

----------------------------------------------------------------------
Requirements

##Functional
Endpoint: POST /extract

Input: base64-encoded PNG or PDF


Output: structured fields in JSON


Use OCR (e.g., PaddleOCR, Tesseract, or EasyOCR) to extract raw text


Use LLM (OpenAI, DeepSeek, or Hugging Face) to extract structured data from raw text


##Tech Stack
Flask + Gunicorn


Docker (containerized app)


.env.example for secrets (e.g., API keys)


One-click run via: docker-compose up or docker run

----------------------------------------------------------------------

README should include:
Setup instructions (docker build, docker run)


How to test the endpoint


Example input/output


Model/API used (OpenAI, DeepSeek, etc.)

----------------------------------------------------------------------

🧪 Bonus
✅ Add GitHub Actions for:
Linting (flake8)


Unit testing (e.g., pytest)


Docker image build validation


✅ Add error handling and graceful failover
✅ Unit test at least one internal module (OCR or LLM call)
