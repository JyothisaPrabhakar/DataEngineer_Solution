from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datatime, timedelta
import pandas as pd
import os

#IO paths
input_directory = "path/input
output_file = "path/output/solution.csv"

#transform json data to tabular format
def transform_data_to_csv():
  
  
