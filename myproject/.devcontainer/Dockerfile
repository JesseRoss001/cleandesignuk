# Use the official Python 3.12 image from Microsoft Container Registry
FROM mcr.microsoft.com/devcontainers/python:3.12

# Set the working directory to /workspace
WORKDIR /workspace

# Copy the requirements.txt file to the container
COPY requirements.txt /workspace/

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Set up virtual environment
RUN python -m venv /workspace/venv

# Copy the entire project into the container
COPY . /workspace

# Activate the virtual environment and run migrations
RUN /bin/bash -c "source /workspace/venv/bin/activate && python manage.py migrate"

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["./venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
