# Anime Recommendation Project

This project is an MLOps-oriented anime recommendation system. The main idea is to use anime-related data to build a machine learning pipeline that can suggest titles a user may like based on patterns in the dataset.

The goal of the project is not only to train a recommendation model, but also to organize the work in a production-style structure. That means keeping the code modular, handling errors cleanly, logging project activity, and preparing the project so it can grow into a full ML pipeline.

## Project Idea

When there are thousands of anime titles available, it becomes difficult for users to decide what to watch next. A recommendation system helps solve this problem by learning from data and returning anime suggestions that are more relevant to user interests.

This project aims to:

- understand anime data and user preference patterns
- build a recommendation workflow using Python and machine learning tools
- organize the project with an MLOps mindset
- prepare the codebase for future stages such as training, evaluation, experiment tracking, and deployment

## Why This Project

This repository is useful for learning how a machine learning project can be structured from the beginning. Instead of keeping everything inside a notebook, the project starts separating reusable code into modules so it becomes easier to maintain, test, and extend later.

In simple terms:

- Machine Learning gives the recommendation logic
- MLOps gives the project structure and scalability

## Current Status

At the moment, the repository is in the foundation stage. The project already includes:

- Python package setup with `setup.py`
- dependency management with `requirements.txt`
- a custom logging utility in `src/logger.py`
- a custom exception class in `src/custom_exception.py`
- folders prepared for pipelines, utilities, configuration, notebooks, and artifacts

This means the project structure is ready, while the full recommendation pipeline can be added step by step.

## Tech Stack

The current project dependencies show that the system is designed around the following tools:

- `pandas` and `numpy` for data handling
- `scikit-learn` for machine learning
- `matplotlib` and `seaborn` for data visualization
- `mlflow` for experiment tracking
- `pyyaml` for configuration management
- `google-cloud-storage` for cloud storage integration

## Project Structure

```text
Anime_Recomendation_Project/
|-- README.md
|-- requirements.txt
|-- setup.py
|-- src/
|   |-- logger.py
|   |-- custom_exception.py
|-- pipeline/
|-- utils/
|-- config/
|-- notebooks/
|-- articats/
|-- Materials/
```

### Folder Explanation

- `src/`: shared core modules such as logging and exception handling
- `pipeline/`: intended for training, prediction, and end-to-end ML workflows
- `utils/`: helper functions that can be reused across the project
- `config/`: configuration files and project settings
- `notebooks/`: experiments, exploration, and model development work
- `articats/`: likely intended to store generated outputs or model artifacts
- `Materials/`: supporting project materials

## How the Project Will Work

The expected recommendation workflow is:

1. collect or load anime dataset
2. clean and preprocess the data
3. engineer useful features
4. train a recommendation model
5. evaluate recommendation quality
6. track experiments and results
7. prepare the model for deployment or reuse

Depending on the final design, the recommender can be:

- content-based
- collaborative filtering based
- hybrid

## Installation

Clone the repository and install the dependencies:

```bash
git clone <your-repository-url>
cd Anime_Recomendation_Project
pip install -r requirements.txt
```

You can also install the project as a package:

```bash
pip install -e .
```

## Logging and Error Handling

This project already includes two useful engineering components:

- `src/logger.py` creates log files inside a `logs/` directory
- `src/custom_exception.py` provides more detailed error messages with file name and line number

These are helpful when the project becomes larger and debugging gets harder.

## Future Improvements

Some natural next steps for this repository are:

- add the dataset and data ingestion pipeline
- implement preprocessing and feature engineering
- build the recommendation model
- add model evaluation metrics
- create configuration files for reproducible runs
- track experiments with MLflow
- save trained models and artifacts
- expose predictions through an API or app

## Who This Project Is For

This project is a good fit for:

- beginners learning recommendation systems
- students practicing MLOps project structure
- developers who want to turn notebook work into a cleaner ML codebase

## Author

**EL Aouan Mohamed**

## Summary

This repository is the starting point of an anime recommendation system built with an MLOps mindset. Its purpose is to combine recommendation logic with good project organization, so the system can grow from experimentation into a more complete and production-ready ML application.
