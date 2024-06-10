# Use an official Python runtime as a parent image
FROM python:3.11-slim

LABEL description="Send your telegram payload to this SERVER:PORT/convert - And it will return {state: boolean: content: text}"

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y ffmpeg flac && apt-get clean

# Copy the current directory contents into the container at /app
COPY .. .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 3008

# Define environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=3008"]

# docker build -t flask-stt .
# docker run -p 3008:3008 -e FLASK_ENV=development -e FLASK_DEBUG=1 --name flask-stt flask-stt