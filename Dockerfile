FROM python:3.12-bookworm

ENV PYTHONBUFFERED=1

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

WORKDIR /app

# Download model and detection model
RUN apt install wget -y

RUN mkdir -p /app/models/ocr

RUN wget -O model.zip https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/english_g2.zip && \
    unzip model.zip -d ./models/ocr && \
    rm model.zip

RUN wget -O detection.zip https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip && \
    unzip detection.zip -d ./models/ocr && \
    rm detection.zip

# Install the application dependencies.
RUN uv sync --frozen --no-cache
