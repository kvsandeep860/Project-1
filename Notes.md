# Project Setup Guide

## 1. Creating a Virtual Environment

The first step in any data science project is to **create a virtual environment**.  
This ensures that all dependencies for your project are isolated and do not interfere with other projects on your system.

### Why use a separate environment?
- Prevents version conflicts between libraries.
- Keeps your global Python installation clean.
- Makes your project reproducible across different machines.

### Creating a virtual environment using Conda

```bash
# Create a new virtual environment with Python 3.10
conda create -p venv python==3.10 -y

```bash
# To activate the created conda environment
conda activate venv/
```
# 1. Data Ingestion.
    - The primary aim of data ingestion is data is sitting some where may be in S3, MangoDb
    we have to extract the data from there
 
### why do we use data class?
    Through data class we can store the paths and can retrive when ever we want, lets say "HelloWorld" is a data class and name_path is one of the attribute there we can exract it when ever we want and also, can make it immutable and also we can update it. 
