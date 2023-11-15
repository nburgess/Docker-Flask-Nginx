FROM python:3.8-slim

# working directory to /app
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install dependencies in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# listen on 5000
EXPOSE 5000

# Run app.py when container launches
CMD ["python", "app.py"]