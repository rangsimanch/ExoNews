# Microservice A - News Aggregator and Summarizer

This microservice is designed to fetch cryptocurrency-related news from RSS feeds, extract and store the articles, summarize them using OpenAI's Assistant API, and store the summarized content in a local PostgreSQL database. The service runs periodically using a scheduler and can be deployed using Docker.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Environment Variables](#set-up-environment-variables)
  - [Install Dependencies](#install-dependencies)
- [Running the Application](#running-the-application)
  - [Using Docker Compose](#using-docker-compose)
  - [Running Locally](#running-locally)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetches cryptocurrency news from multiple RSS feeds.
- Extracts full articles from fetched news items.
- Stores raw news data in a local PostgreSQL database (`news_rss` table).
- Summarizes news articles using OpenAI's Assistant API.
- Stores summarized news in the PostgreSQL database (`news_ai` table).
- Runs scheduled tasks to fetch and process news periodically.
- Can be deployed using Docker for ease of setup and scalability.

## Project Structure
```plaintext
├── app/
│ ├── init.py
│ ├── main.py
│ ├── config.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── services/
│ │ ├── init.py
│ │ ├── news_fetcher.py
│ │ ├── rss_processor.py
│ │ ├── ai_summarizer.py
│ │ ├── ai_processor.py
│ │ └── scheduler.py
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```


## Requirements

- Python 3.8 or higher
- PostgreSQL database
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- Docker and Docker Compose (if using Docker)

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/microservice_a.git
cd microservice_a
```

### Set Up Environment Variables
Create a `.env` file in the root directory and set the necessary environment variables:
```bash
# .env
DATABASE_URL=postgresql://youruser:yourpassword@localhost:5432/yourdatabase
OPENAI_API_KEY=your_openai_api_key
ASSISTANT_ID=your_openai_assistant_id
RSS_FEEDS=https://www.coindesk.com/arc/outboundfeeds/rss/,https://cointelegraph.com/rss,https://cryptoslate.com/feed/
```

### Install Dependencies
Create a virtual environment and install the required packages:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application
### Using Docker Compose
Ensure you have Docker and Docker Compose installed on your system.
1. Build and start the containers:
```bash
docker-compose up --build
```
2. The application should now be running on `http://localhost:8000/`.

### Running Locally
If you prefer to run the application without Docker:
1. Ensure that PostgreSQL is installed and running on your local machine.
2. Set up the PostgreSQL database and user:
```bash
# Access PostgreSQL prompt
psql -U postgres

# Create database
CREATE DATABASE yourdatabase;

# Create user
CREATE USER youruser WITH PASSWORD 'yourpassword';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE yourdatabase TO youruser;
```
3. Activate your virtual environment and run the application:
 ```bash
 # Activate virtual environment
source venv/bin/activate   # Linux/Mac
# or
venv\Scripts\activate      # Windows

# Run the application
uvicorn app.main:app --reload
 ```

4. The application should now be running on `http://localhost:8000/`.


## Configuration
### Environment Variables
The application relies on several environment variables for configuration. These can be set in the `.env` file or directly in your system's environment.

- DATABASE_URL: Connection URL for the PostgreSQL database.
- OPENAI_API_KEY: API key for OpenAI.
- ASSISTANT_ID: ID of the assistant created in OpenAI's Assistant API.
- RSS_FEEDS: Comma-separated list of RSS feed URLs to fetch news from.

Example `.env` file:
```DOTENV
DATABASE_URL=postgresql://youruser:yourpassword@localhost:5432/yourdatabase
OPENAI_API_KEY=your_openai_api_key
ASSISTANT_ID=your_openai_assistant_id
RSS_FEEDS=https://www.coindesk.com/arc/outboundfeeds/rss/,https://cointelegraph.com/rss,https://cryptoslate.com/feed/
```

**Important**: Keep your API keys and sensitive information secure. Do not commit them to version control.

## Usage
- When the application is running, it will automatically fetch news from the specified RSS feeds every 30 minutes.
- It extracts the full article content and stores the news data in the news_rss table.
- The service then processes the news articles by sending them to OpenAI's Assistant API for summarization.
- Summarized news is stored in the news_ai table.
- You can access the root endpoint at http://localhost:8000/ to verify the service is running.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.

2. Create a new branch:
```BASH
git checkout -b feature/your-feature-name
```

3. Make your changes and commit them with descriptive messages.

4. Push to your branch:
```BASH
git push origin feature/your-feature-name
```

5. Submit a pull request with a clear description of your changes.

---

***Disclaimer***: This project is intended for educational purposes. Make sure to comply with the terms of service of the RSS feed providers and OpenAI when using their services. Always handle API keys and sensitive information securely.