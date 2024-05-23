# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /workspace

# Copy the requirements file into the container
COPY requirements.txt /workspace/

# Install any needed packages specified in requirements.txt
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . /workspace/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the migrations and collect static files
RUN . venv/bin/activate && python manage.py migrate && python manage.py collectstatic --noinput

# Run the application
CMD ["/workspace/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]