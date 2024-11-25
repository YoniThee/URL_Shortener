# Build stage
FROM python:3.11-slim-buster AS builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Runtime stage
FROM python:3.11-slim-buster
WORKDIR /app
COPY --from=builder /app .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]