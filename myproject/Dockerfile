FROM python:3.12

# Set the working directory in the container
WORKDIR /workspace/myproject

# Copy the requirements file into the container
COPY requirements.txt /workspace/myproject

# Install any needed packages specified in requirements.txt
RUN python -m venv venv && \
    /bin/bash -c "source venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt"

# Copy the rest of the working directory contents into the container
COPY . /workspace/myproject

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Use an entrypoint script to perform initial setup tasks
COPY entrypoint.sh /workspace/myproject
RUN chmod +x /workspace/myproject/entrypoint.sh
ENTRYPOINT ["/workspace/entrypoint.sh"]

# Run the application
CMD ["/workspace/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
