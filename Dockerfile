# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files to disk and to buffer stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app

# Install Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Expose port 8000 to the outside world
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run django's migrations
RUN python manage.py migrate

# Run the command to start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]