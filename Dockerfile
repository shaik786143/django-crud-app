    # Use an official Python runtime as a parent image
    FROM python:3.12-slim-bullseye

    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    # Set the working directory in the container
    WORKDIR /app

    # Install system dependencies and build tools
    RUN apt-get update && \
        apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev \
        python3-dev \
        libffi-dev \
        pkg-config \
        default-libmysqlclient-dev && \
        rm -rf /var/lib/apt/lists/*

    # Copy the requirements file into the container at /app
    COPY requirements.txt /app/

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the rest of the application code into the container
    COPY . /app/

    # Expose the port Gunicorn will listen on
    EXPOSE 8000

    # Run the application using Gunicorn
    CMD ["gunicorn", "aws.wsgi:application", "--bind", "0.0.0.0:8000"]