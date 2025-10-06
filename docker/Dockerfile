# ---- Builder stage ----
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Install Python dependencies into /install
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --prefix=/install -r requirements.txt

# ---- Runtime stage ----
FROM python:3.12-slim

WORKDIR /app

# Copy Python packages from builder image
COPY --from=builder /install /usr/local

# Copy application code
COPY app/ app/

# Create non-root user
RUN useradd -m portfolio
USER portfolio

# Expose container port
EXPOSE 8080

# Start Gunicorn (WSGI production server)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app.app:app"]