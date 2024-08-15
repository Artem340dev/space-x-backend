FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR .

# Copy only the necessary files (during build)

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]