import pandas as pd
import numpy as np
import os
import re

relative_csv_path = os.path.join('ETL', 'raw_data','salaries','data_scientists_salaries_from_reddit.csv')
df = pd.read_csv(relative_csv_path)

def get_title():
    job_titles = df.iloc[:, 1]
    return job_titles

def get_location():
    return True

def get_salary():
    return True

def get_company_industry():
    return True

def get_experince_level():
    return True

