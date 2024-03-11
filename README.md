# Transfermarkt ETL using Airflow

## Overview

This project implements an Extract, Transform, Load (ETL) pipeline to scrape football transfer data from Transfermarkt using Apache Airflow. The pipeline includes tasks for data retrieval, transformation, and storage in both CSV and MongoDB formats.

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

## Getting Started

### Prerequisites

- [Apache Airflow](https://airflow.apache.org/) installed.
- Python dependencies installed using:

```bash
pip install -r requirements.txt
