FROM python:3.8-slim

# install needed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql \
    gcc \
    libcairo2-dev \
    libpq-dev

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the project files into the container
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change to the project directory
WORKDIR /project_dium/backend

# Run database migrations and start the server
CMD python manage.py migrate && gunicorn configurations.wsgi