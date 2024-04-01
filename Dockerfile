FROM python:3.12.2-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /app

# Suck it "PayCash Online Protocol", this perfect-numbered port is mine.
EXPOSE 8128

CMD ["flask", "run", "--host=0.0.0.0"]