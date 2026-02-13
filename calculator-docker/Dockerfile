# -------- Stage 1: Build Stage --------
FROM python:3.11 AS builder

WORKDIR /install

COPY requirements.txt .
RUN pip install --user -r requirements.txt


# -------- Stage 2: Final Runtime Stage --------
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy app code
COPY app.py .

# Set path
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]
