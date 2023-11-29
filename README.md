# Support Assistant Web Application

## Overview

This project is a Flask-based web application designed to function as a support assistant. It leverages OpenAI's ChatGPT API to answer user queries. The application first searches for answers in a predefined FAQ (Frequently Asked Questions) dataset and, if no relevant answer is found, it falls back to querying the ChatGPT API.

## Features

- **User Interface:** Provides a form for users to submit their questions.
- **FAQ-Based Response System:** Quickly delivers answers from a predefined set of frequently asked questions.
- **OpenAI ChatGPT API Integration:** For queries that go beyond the FAQ, the application queries the ChatGPT API for more detailed answers.
- **Simple and User-Friendly Interface:** Designed for ease of use, ensuring a smooth user experience.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python is installed on your machine.
- You have an API key from OpenAI for using the ChatGPT API.

## Setup and Installation

**Install Required Packages:**

Install Flask and requests using pip:

```bash
pip install Flask requests
```

## Set Up Your API Key

In the `app.py` file, replace `YOUR_API_KEY` with your actual OpenAI API key.

## Running the Application

Start the application with the Flask command:

```bash
flask run
```

## Usage

### Access the Application

1. **Open Your Web Browser:**
   - Navigate to `http://localhost:5000` in your web browser to access the Support Assistant application.

### Submit Your Question

2. **Enter Your Question:**

   - Find the input field labeled "Запитання" (Question).
   - Type your question into this field.

3. **Submit the Question:**
   - Click on the "Answer" button to submit your question to the application.

### Receive an Answer

4. **Get the Response:**
   - After submitting your question, the application processes it and displays the response.
   - The answer is either fetched from a pre-defined FAQ database or obtained dynamically from the ChatGPT API, depending on whether the FAQ contains a relevant response.
