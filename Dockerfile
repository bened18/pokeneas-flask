FROM python:3.8

# Create app directory
WORKDIR /usr/src/pokeneas

# Copy the Flask app source to the working directory
COPY . .

# Install Flask
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 8080

# Specify the command to run the Flask app
CMD ["python", "pokeneas.py"]