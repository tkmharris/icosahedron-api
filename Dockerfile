FROM python:3.12.2-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /app /app

EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]