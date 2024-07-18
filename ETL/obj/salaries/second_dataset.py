import pandas as pd
import numpy as np
import os
import re

relative_csv_path = os.path.join('ETL', 'raw_data','salaries','salaries.csv')
df_second_dataset = pd.read_csv(relative_csv_path)

def get_title():
 job_titles = df_second_dataset.iloc[:, 3]
 new_job_titles = []
 for jt in job_titles:
  if pd.isna(jt):
    jt = 'Null'
    print(jt)
  else:
    if 'data' in jt.lower():
        if 'scientist' in jt.lower():
            jt = 'Data Scientist'
        elif 'analy' in jt.lower():
            jt = 'Data Analyst'
        elif 'manager' in jt.lower():
            jt = 'Data Manager'
        elif 'engineer' in jt.lower() or 'architect':
            jt = 'Data Engineer'
        elif 'science' in jt.lower():
            jt = 'Data Scientist'
    elif 'machine learning' in jt.lower() or 'ml' in jt.lower():
        jt = 'ML Engineer'
    elif 'research' in jt.lower():
        jt = 'Research Engineer'
    elif 'ai' in jt.lower():
        jt = 'AI Engineer'
    elif 'business' in jt.lower() or 'bi ' in jt.lower():
      if 'engineer' in jt.lower():
        jt = 'BI Engineer'
      elif 'analyst' in jt.lower():
        jt = 'BI Analyst'
      elif 'manager' in jt.lower():
        jt = 'BI Manager'
      elif 'developer' in jt.lower():
        jt = 'BI Developer'
      else:
        jt = 'BI Analyst'
  new_job_titles.append(jt)
 return new_job_titles

def get_location():
 employee_residence = df_second_dataset['company_location']
 return employee_residence

def get_salary():
 salaries = df_second_dataset['salary']   
 for s in salaries:
  if pd.isna(s):
    print(s)
  elif not str(s).isdigit:
    print(s)
 return salaries

def get_company_industry():
 reference_years = df_second_dataset['work_year']
 return reference_years

def get_experince_level():
 experience_level = df_second_dataset['experience_level']
 new_priorExperience = []
 for jt in experience_level:
    if pd.isna(jt):
      jt='Null'
    else:
      if 'EN' in jt:
          jt='Junior'
      elif 'MI' in jt:
          jt='Mid'
      elif 'SE' in jt:
          jt='Senior'
      elif 'EX' in jt:
          jt='Executive'

    new_priorExperience.append(jt)
 return new_priorExperience

def get_salary_currency():
 salary_currencies = df_second_dataset['salary_currency']
 return salary_currencies

def get_conversion_ratio():
 salary_currencies = get_salary_currency()
 conv_ratios = []
 for currency in salary_currencies:
  if currency == 'Null':
    cr = 'Null'
  else:
    if currency == 'USD':
      cr = 1
    elif currency == 'EUR':
      cr = 1.0882787
    elif currency == 'GBP':
      cr = 1.2951632
    elif currency == 'CAD':
      cr = 0.73006557
    elif currency == 'INR':
      cr = 0.011962834
    elif currency == 'AUD':
      cr = 0.67236147
    elif currency == 'CHF':
      cr = 1.1143726
    elif currency == 'DKK':
      cr = 0.14585547
    elif currency == 'SGD':
      cr = 0.74328847
    elif currency == 'BRL':
      cr = 0.18421977
    elif currency == 'PLN':
      cr = 0.25486645
    elif currency == 'JPY':
      cr = 0.0063014631
    elif currency == 'TRY':
      cr = 0.030213532
    elif currency == 'HUF':
      cr = 0.0027768293
    elif currency == 'ILS':
      cr = 0.27555599
    elif currency == 'NOK':
      cr = 0.09228212
    elif currency == 'THB':
      cr = 0.02764467
    elif currency == 'NZD':
      cr = 0.60512592
    elif currency == 'PHP':
      cr = 0.017113229
    elif currency == 'ZAR':
      cr = 0.05514742
    elif currency == 'HKD':
      cr = 0.1281279
    elif currency == 'MXN':
      cr = 0.056389299
    elif currency == 'CLP':
      cr = 0.0010997046

  conv_ratios.append(cr)
 return conv_ratios

def get_reference_year():
  reference_years = df_second_dataset['work_year']
  return reference_years
  
