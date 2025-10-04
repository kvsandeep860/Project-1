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

# 2. Data Validation

Lets say we have trained the pipeline with 1000 data points and 3 features f1, f2, f3 now during inference we should not send the features in f2, f3, f1 in this order if in case that happens we should rise an error, in order to perrform these kind of tasks data validation moudle is being implemented.

# 3. Data Transformation

All the Data preprocessing steps like dealing with null values data noramlization are done in this step