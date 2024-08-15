FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files (during build)
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]