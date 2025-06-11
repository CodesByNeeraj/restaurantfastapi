# AI Restaurant Idea Generator 

## This is a simple FastAPI application that uses Langchain and OpenAI GPT to generate creative restaurant names and menus based on a cuisine type provided by the user.

See Slide Deck For To Understand More About This Project: https://shorturl.at/vQtxe  

## Features
Takes a cuisine type as input (e.g., Italian, Japanese).

- Uses Langchain chains to:

  - Generate a unique restaurant name.

  - Generate a corresponding menu for that restaurant.

- Saves generated restaurants and menus in a SQLite database using SQLAlchemy.

- Provides API endpoints to create restaurants and retrieve history of generated restaurants.

- Includes CORS middleware to support frontend apps hosted on different domains.

- Simple frontend integration example that sends user input to backend and displays generated restaurant info.

## Tech Stack

- Python 3.9+

- FastAPI

- Langchain

- OpenAI API

- SQLAlchemy (SQLite)

- CORS Middleware

## Setup With Docker

1. Install Docker On Your Machine

2. Clone the repository (if you haven’t already):

git clone https://github.com/CodesByNeeraj/restaurantfastapi.git
cd <your-repo-folder>

3. Build the Docker image:

docker build -t langchain-restaurant-app .

langchain-restaurant-app is the image name; you can choose any name you prefer.

4. Run the Docker container:

docker run -p 8000:8000 langchain-restaurant-app

This runs the container and maps port 8000 inside the container to port 8000 on your machine.

5. Open the HTML file in your browser and interact with the application!

