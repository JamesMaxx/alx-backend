# Queuing System in JS

This project demonstrates how to use Redis as a data store and Kue as a queue system in a Node.js application.

## Prerequisites

- Node.js
- Redis

## Installation

1. Install Node.js dependencies:

npm install

2.Start the Redis server:

redis-server

3.Start the application:

node server.js

## Usage

The application provides a simple Express server that interacts with Redis and Kue. You can send HTTP requests to the server to perform various operations, such as storing data in Redis, creating jobs in the queue, and processing jobs.

### Redis Operations

- **Store a hash value**: Send a `POST` request to `/data` with a JSON payload containing a `key` and `value`.
- **Retrieve a hash value**: Send a `GET` request to `/data?key=<key>`.

### Queue Operations

- **Create a job**: Send a `POST` request to `/queue` with a JSON payload containing a `job` object.
- **Process jobs**: The application automatically processes jobs from the queue using Kue.

## Redis Client

The Redis client is initialized in `redis.js` and exported as a singleton instance. It provides methods for interacting with Redis, such as `set`, `get`, and `hset`.

## Kue Queue

The Kue queue is initialized in `queue.js`. It defines a job type called `email` that logs a message when processed. The `processJobs` function continuously processes jobs from the queue.

## Express Server

The Express server is defined in `server.js`. It sets up routes for handling Redis and queue operations, and starts processing jobs from the queue.
