Here's an updated version of the FastAPI project README with the instructions for seeding data to MongoDB using Postman:

---

# FastAPI Project Readme

Welcome to your FastAPI project! This document provides instructions on how to set up, run the project, and seed data to MongoDB using Postman.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Environment Setup](#environment-setup)
4. [Installation](#installation)
5. [Running the Development Server](#running-the-development-server)
6. [Seeding Data to MongoDB](#seeding-data-to-mongodb)
7. [Additional Resources](#additional-resources)

## Introduction

This project is built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It includes functionalities for user authentication (login and signup) and fuzzy search for job listings. MongoDB is used as the data storage solution.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or later
- MongoDB server (you can use MongoDB Atlas for a cloud solution)

## Environment Setup

Set the following environment variables in a `.env` file at the root of your project:

```plaintext
MONGODB_URL=
DATABASE_NAME=job_search_db

JWT_SECRET=
ALGORITHM=HS256
```

## Installation

To install the necessary packages, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/syedhadi209/job_search_backend.git)
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**

   On Windows:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Development Server

To run the development server, use the following command:

```sh
uvicorn app.main:app --reload
```

The server will start on `http://localhost:8000`. Open your browser and navigate to this URL to see the application in development mode.

## Seeding Data to MongoDB

To seed data to MongoDB, follow these steps:

1. **Run the Development Server:**
   Start the FastAPI development server as described above.

2. **Seed Data Endpoint:**
   Use a tool like Postman to send a GET request to the following endpoint after running the dev server:

   ```
   GET http://localhost:8000/api/user/seed-data
   ```

   This endpoint will read data from a CSV file (`jobs_data.csv`), create documents based on the data, and insert them into the MongoDB collection.

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)

If you have any questions or need further assistance, please feel free to contact the project maintainer or visit the official documentation.

---

Happy coding! 🚀
