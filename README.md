# Transfermarkt ETL using Apache Airflow

This project is an Extract, Transform, Load (ETL) pipeline for scraping football transfer data from Transfermarkt using Apache Airflow. The pipeline includes tasks for data retrieval, transformation, and storage in both CSV and MongoDB formats.
## Project Schema

![Project Schema](Transfermarket_ETL_using_Airflow.jpg)
## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Python](https://www.python.org/downloads/) installed
- [MongoDb](https://www.mongodb.com/try/download/community) installed

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Transfermarkt_ETL_using_Airflow.git

2. **Navigate to the proect directory:**

   ```bash
   cd Transfermarkt_ETL_using_Airflow


3. **Start the Docker containers:**

   ```bash
   docker-compose up -d

4. **Start to install the dependencies:**

   ```bash
   pip install -r requirements.txt


This will launch Airflow, and other necessary services.

5. **Open your web browser and go to http://localhost:8080 to access the Airflow web interface.**

6. **Use Airflow to trigger and monitor your ETL pipeline..**


## Features

- **Scraping**: Utilizes web scraping techniques to gather transfer data from Transfermarkt.
- **Transformation**: Applies data transformations to enhance and structure the collected data.
- **CSV Export**: Saves the transformed data into a CSV file for easy analysis.
- **MongoDB Integration**: Stores the transformed data into MongoDB for further querying and exploration.

## Project Structure

- `dags/`: Contains the Apache Airflow DAG (Directed Acyclic Graph) definition file.
- `player.py`: Includes functions for data retrieval (`get_trans`), transformation (`transform`), and MongoDB storage (`save_to_mongodb`).
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Project documentation providing instructions and details.


## Contributors
- [JAOUAD OUCHBAR](https://github.com/jawadoch/)
