#uses Python 3.13 to run the app (slim so smaller size and faster build)
FROM python:3.13-slim

#setting the working directory inside the container to /app 
WORKDIR /app

#copies dependencies into the /app directory in the container
COPY requirements.txt .

#installs python packages listed in requirements.txt, no chache dir keeps the image size smaller by not storing temporary files
RUN pip install --no-cache-dir -r requirements.txt

#copies the whole app's code into the /app directory in the container
COPY . . 

#Docker knows this container will listen on port 8000
EXPOSE 8000

#Docker knows what to run when the container starts
CMD ["uvicorn","Main:app","--host","0.0.0.0","--port","8000"]

#to run this:
#type in ur terminal: 
# docker build -t [any name u like] .
# docker -run -p 8000:8000 [name you set earlier]


