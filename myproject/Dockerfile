FROM python:3.12

# Set the working directory in the container
WORKDIR /workspace

# Creating a virtual environment in the working directory
RUN python3 -m venv venv

# Activating the virtual environment and updating pip
RUN . venv/bin/activate && pip install --upgrade pip

# Copy the requirements and install them
COPY requirements.txt .
RUN . venv/bin/activate && pip install -r requirements.txt

# Copying the rest of your application
COPY . .

# Make the entrypoint script executable
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Setting the script as the entrypoint
ENTRYPOINT ["./entrypoint.sh"]

# Exposing the port and setting the command to start Gunicorn
EXPOSE 8000
CMD ["venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
