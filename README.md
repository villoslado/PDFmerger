# PDF Merger 📚

This simple Python web application merges multiple PDF files into a single PDF document. Built using Django and `PyPDF2`, it provides an easy-to-use interface for users to upload and merge PDF files. The application can be run within a Docker container.

## Features

- Upload and merge multiple PDF files into one.
- Dynamically add multiple file inputs to merge additional PDFs.
- Output the merged PDF file for download.
- Lightweight and easy-to-deploy solution.

## How To Run This or Use It

### Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/).
2. Ensure you have [Docker Compose](https://docs.docker.com/compose/install/) installed.
3. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/villoslado/PDFmerger.git
   cd PDFmerger

### Running the App with Docker

This project includes a `Dockerfile` and a `docker-compose.yml` file to make it easy to build and run the app in a container.

#### Build the Docker Image:

First, build the Docker image by running the following command:

`docker compose up --build`

#### Access the Application

Once the container is running, the application will be accessible at:

`http://localhost:8000/merge/`
