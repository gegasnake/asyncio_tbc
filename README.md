# Async API Requests with `aiohttp` and `asyncio`

This project demonstrates how to fetch data from an API asynchronously using Python's `asyncio` and `aiohttp` libraries.

## Project Overview

The script fetches 77 posts from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts/) API asynchronously. 
This approach allows for concurrent requests, significantly improving performance compared to sequential execution.

### Files Created

- `async_posts.json`: The fetched posts saved in JSON format.

## Requirements

- Python 3.7+
- Install the following Python package:

  ```bash
  pip install -r requirements.txt

## How to Run
1. Clone this repository and navigate to the project directory.
2. Run the script:
     python fetch_posts.py
The script will:

  .Asynchronously fetch all posts using asyncio and aiohttp.
  .Save the results in async_posts.json.
  .Display the execution time in the console.

## Asyncio and Aiohttp Implementation
  fetch_post: An asynchronous function that fetches a single post from the API using aiohttp.
  fetch_all_posts: A function that runs all fetch operations concurrently using asyncio.gather.
  asyncio.run: Executes the asynchronous code and handles the event loop.
This approach leverages non-blocking I/O, making the program efficient for multiple API requests.

## Typical Performance
  Fetching 77 posts using this method typically takes 0.6 - 1.2 seconds, depending on network conditions.
