FROM python:3.9-slim

WORKDIR /tmp
# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install all necessary python modules
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .

CMD [ "python3", "./2app.py" ]

# expose port
EXPOSE 5000
# expose path
VOLUME /app
