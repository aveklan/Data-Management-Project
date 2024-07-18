import pandas as pd
import numpy as np
import os
import re

relative_csv_path = os.path.join('ETL', 'raw_data','salaries','data_scientists_salaries_from_reddit.csv')
df = pd.read_csv(relative_csv_path)

def get_salary_helper():
  salaries = df.iloc[:, 3]
  new_salaries = []
  for salary in salaries:
    if pd.isna(salary):
      salary = np.nan
      new_salaries.append(salary)
    else:
      salary = salary.replace(',', '')
      salary = salary.replace('.', '')
      salary = salary.replace('$', '')
      if '*' in salary:
        salary = salary.split('*')[0].strip()
      if '(' in salary:
        salary = salary.split('(')[0]
      if '/' in salary:
        salary = salary.split('/')[0]
      if '+' in salary:
        parts = salary.split('+')
        sal = 0
        for part in parts:
          if part.isdigit():
            sal += int(part)
        if sal == 0:
          salary = parts[0].strip()
        else:
          salary = str(sal)
      if salary.endswith('k'):
        salary = salary.replace('k', '000', 1)
      elif salary.endswith('K'):
        salary = salary = salary.replace('K', '000', 1)
      elif not salary.endswith('0'):
        for i in range(len(salary)):
          if salary[i].isdigit() and salary[i+1] == 'k' or salary[i].isdigit() and salary[i+1] == 'K':
            salary = salary.replace(salary[i+1], '000', 1)
      if 'base' in salary.lower():
        temp = salary.lower().split('base')
        if temp[0].strip().isdigit():
          salary = temp[0].strip()
        elif temp[1].strip().isdigit():
          salary = temp[1].strip()
      if '¬' in salary:
        salary = salary.split('¬')[0].strip() + ' EUR'
      if salary == '0':
          salary = np.nan
          new_salaries.append(salary)
          continue
      if '800-900' in salary:
        salary =  '10800'
      if '-' in salary:
        if 'cad' in salary:
          salary = '85000 cad'
        elif '150000' in salary:
          salary = '150000'
        else:
          salary = np.nan
          new_salaries.append(salary)
          continue
      if 'per ' in salary:
        if 'month' in salary:
          salary = str(int(salary.split('per')[0].strip()) * 12)
        else:
          salary = salary.split('per')[0].strip()
      if '  ' in salary:
        salary = salary.split('  ')[0].strip()
      if 'lt;' in salary:
        salary = np.nan
        new_salaries.append(salary)
        continue
      if ' pa ' in salary:
        salary = np.nan
        new_salaries.append(salary)
        continue
      if 'started' in salary.lower() or 'renegotiate' in salary.lower() or 'also teach' in salary.lower():
          salary = salary[:6].strip()
      if '14% bonus' in salary.lower():
        salary = '114000'
      if 'usd' in salary.lower():
        temp = salary.lower().split('usd')
        if temp[0].strip().isdigit():
          salary = temp[0].strip() + ' USD'
        elif temp[1].strip().isdigit():
          salary = temp[1].strip() + ' USD'
      elif 'dollars' in salary.lower():
        salary = salary.lower().split('dollars')[0].strip() + ' USD'
      elif 'eur' in salary.lower():
        temp = salary.lower().split('eur')
        if temp[0].strip().isdigit():
          salary = temp[0].strip() + ' EUR'
        elif temp[1].strip().isdigit():
          salary = temp[1].strip() + ' EUR'
      elif 'cad' in salary.lower():
        salary = salary.lower().split('cad')[0].strip().replace(' ','') + ' CAD'
      elif 'dkk' in salary.lower():
        salary = salary.lower().split('dkk')[0].strip() + ' DKK'
      elif 'aud' in salary.lower():
        temp = salary.lower().split('aud')
        if temp[0].strip().isdigit():
          salary = temp[0].strip() + ' AUD'
        elif temp[1].strip().isdigit():
          salary = temp[1].strip() + ' AUD'
      elif 'lpa' in salary.lower() or 'lak' in salary.lower():
        if 'lpa' in salary.lower():
          temp = salary.lower().split('lpa')[0].strip()
          salary = ''.join(c for c in temp if c.isdigit())
        elif 'lak' in salary.lower():
          temp = salary.lower().split('lak')[0].strip()
          salary = ''.join(c for c in temp if c.isdigit())
        salary = str(int(salary) * 100000) + ' INR'
      elif 'chf' in salary.lower():
        salary = salary.lower().split('chf')[1].strip() + ' CHF'
      elif 'TC' in salary:
        salary = salary.split('TC')[1].strip()

      if salary.endswith('0') and not salary.isdigit():
        i = len(salary) - 1
        res = ''
        while salary[i].isdigit():
          res += salary[i]
          i -= 1
        salary = res[::-1]

      salary = salary.strip()
      if salary.isdigit():
        salary += ' USD'

      new_salaries.append(salary)

  return new_salaries
 

def get_title():
    job_titles = df.iloc[:, 1]
    new_job_titles = []

    for jt in job_titles:
        if pd.isna(jt):
            jt = np.nan
        else:
            if 'ds' in jt.lower():
                jt = 'Data Scientist'
            elif 'data' in jt.lower():
                if 'scientist' in jt.lower():
                    jt = 'Data Scientist'
                elif 'analy' in jt.lower():
                    jt = 'Data Analyst'
            elif 'machine learning' in jt.lower() or 'ml' in jt.lower():
                jt = 'ML Engineer'
            elif 'analytics' in jt.lower():
                jt = 'Analytics Manager'
            elif 'analyst' in jt.lower():
                if 'business' in jt.lower() or 'bi' in jt.lower() or 'intelligence' in jt.lower():
                    jt = 'BI Analyst'
                else:
                    jt = 'Product Analyst'
            elif 'directo' in jt.lower():
                jt = 'Director'
            elif '/' in jt.lower() and 'sr' in jt.lower():
                temp = jt.split('/')[0]
                jt = temp.split('Sr. ')[1]
            elif '/' in jt.lower():
                jt = jt.split('/')[0]
            elif ',' in jt.lower():
                jt = jt.split(',')[0]
            elif '(' in jt.lower():
                jt = jt.split('(')[0]
            elif 'sr' in jt.lower():
                jt = jt.split('Sr. ')[1]
            elif 'senior' in jt.lower():
                jt = jt.split('Senior ')[1]
            elif '.' in jt.lower():
                jt = jt.split('.')[0]
        new_job_titles.append(jt)
    return new_job_titles

def get_location():
  locations = df.iloc[:, 2]

  return True

def get_salary():
  new_salaries = get_salary_helper()
  new_salaries_amount= []
  
  for salary in new_salaries:
    if pd.isna(salary):
      new_salaries_amount.append(np.nan)
      
    else:
      new_salaries_amount.append(int(salary.split(' ')[0].strip()))
  return new_salaries_amount

def get_company_industry():
  company_industry = df.iloc[:, 4]
  new_company_industry = []
  
  for jt in company_industry:
    if pd.isna(jt):
      jt=np.nan
    else:
      if 'consulting' in jt.lower() or 'big 4' in jt.lower() or 'consultancy' in jt.lower() or 'agency' in jt.lower():
          jt ='Consulting'
      elif 'health' in jt.lower() or 'pharma' in jt.lower() or 'medical' in jt.lower() or 'danhar' in jt.lower() or 'clinical' in jt.lower():
          jt ='Healthcare'
      elif 'warehous' in jt.lower() or 'logistics' in jt.lower() or 'supply' in jt.lower():
          jt ='Warehousing and Logistic'
      elif 'travel' in jt.lower() or 'entert' in jt.lower():
          jt ='Travelling and Enterteinment'
      elif 'security' in jt.lower() or 'defense' in jt.lower():
          jt ='Ciber Security'
      elif 'education' in jt.lower() or 'research' in jt.lower() or 'academia' in jt.lower() or 'university' in jt.lower() or 'higher ed' in jt.lower() or 'sensory science' in jt.lower():
          jt ='Education, Research ad University'
      elif 'faang' in jt.lower() or 'public company' in jt.lower() or 'large corporate' in jt.lower() or 'large cable' in jt.lower() or 'maang' in jt.lower() or 'fortune' in jt.lower() or 'large international' in jt.lower() or 'fanng' in jt.lower() or 'fb' in jt.lower() or 'google' in jt.lower() or 'youtube' in jt.lower() or 'amazon' in jt.lower() or 'aaa game' in jt.lower() or 'big n' in jt.lower():
          jt ='Big Tech'
      elif 'small' in jt.lower():
          if 'tech' in jt.lower():
            jt ='Small Tech'
      elif 'tech' in jt.lower() or 'saas' in jt.lower() or 'sas' in jt.lower() or 'game' in jt.lower() or 'gaming' in jt.lower() or 'software' in jt.lower() or 'digital' in jt.lower():
          jt ='Tech Company'
      elif 'finance' in jt.lower() or 'real estate' in jt.lower() or 'm / g' in jt.lower() or 'tmd' in jt.lower() or 'forecast' in jt.lower() or 'pe/vc' in jt.lower() or'statistics' in jt.lower() or 'portofolio' in jt.lower() or 'capital' in jt.lower()  or 'credit' in jt.lower() or 'portfolio' in jt.lower() or 'trading' in jt.lower() or 'crypto' in jt.lower() or 'financial' in jt.lower() or 'bank' in jt.lower() or 'financing' in jt.lower() or 'insurance' in jt.lower():
          jt ='Finance'
      elif 'fintech' in jt.lower():
          jt ='FinTech'
      elif 'startup' in jt.lower() or 'self driving' in jt.lower() or 'self-driving' in jt.lower():
          jt ='StartUp'
      elif 'ecommerce' in jt.lower() or 'e-commerce' in jt.lower():
          jt ='Ecommerce'
      elif 'govern' in jt.lower() or 'federal' in jt.lower():
          jt ='Public Sector and Gonverment'
      elif 'manufactor' in jt.lower() or 'electronics' in jt.lower() or 'automaker'  in jt.lower() or 'steel' in jt.lower() or 'hardware' in jt.lower() or 'manufactur' in jt.lower() or 'components' in jt.lower() or 'semiconductors' in jt.lower() or 'caterpillar' in jt.lower():
          jt ='Manufactoring'
      elif 'energy' in jt.lower() or 'oil' in jt.lower() or 'gas' in jt.lower() or 'utilit' in jt.lower():
          jt ='Energy, oil and gas'
      elif 'marketing' in jt.lower() or 'advertising' in jt.lower() or 'media' in jt.lower():
          jt ='Marketing, Media and Advertising'
      elif 'retail' in jt.lower() or 'fmcg' in jt.lower() or 'consumer' in jt.lower() or 'goods' in jt.lower() or 'cpg' in jt.lower() or 'food' in jt.lower() or 'brewery' in jt.lower():
          jt ='Retail'
      else:
          jt ='Others'
    new_company_industry.append(jt)
  
  return new_company_industry

def get_experince_level():
  prior_experience = df.iloc[:, 6]
  new_priorExperience = []
  
  pattern = r'(\d+(\.\d+)?)\s*year'
  pattern1 = r'(\d+(\.\d+)?)\s*yrs'
  pattern2 = r'(\d+(\.\d+)?)\s*Year'
  pattern3 = r'(\d+(\.\d+)?)\s*YOE'
  pattern4 = r'(\d+(\.\d+)?)\s*yoe'
  
  for jt in prior_experience:
    if pd.isna(jt):
      jt = np.nan
    else:
      matches = re.findall(pattern, jt)
      matches1 = re.findall(pattern1, jt)
      matches2 = re.findall(pattern2, jt)
      matches3 = re.findall(pattern3, jt)
      matches4 = re.findall(pattern4, jt)

      total_experience = sum(float(match[0]) for match in matches)
      total_experience += sum(float(match[0]) for match in matches1)
      total_experience += sum(float(match[0]) for match in matches2) 
      total_experience += sum(float(match[0]) for match in matches3)
      total_experience += sum(float(match[0]) for match in matches4)

      if(total_experience==0):
        if 'internship' in jt.lower():
          jt = 'Intership'
        elif '1y' in jt.lower():
          jt = 'Junior'
        else:
          jt = 'Not specified'
      else:
        if (total_experience < 3):
          jt = 'Junior'
        elif (total_experience >= 3 and total_experience < 5):
          jt = 'Mid'
        elif (total_experience >= 5):
          jt = 'Senior'

    new_priorExperience.append(jt)
    
  return new_priorExperience

def get_salary_currency():
  new_salaries = get_salary_helper()
  new_salaries_currency = []
  
  for salary in new_salaries:
    if pd.isna(salary):
      new_salaries_currency.append(np.nan)
      
    else:
      new_salaries_currency.append(salary.split(' ')[1].strip())
      
  return new_salaries_currency

def get_conversion_ratio():
  salaries_currency = get_salary_currency()
  conv_ratios = []
  for currency in salaries_currency:
    if pd.isna(currency):
      cr = np.nan
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

    conv_ratios.append(cr)
    
  return conv_ratios

def get_reference_year():
  reference_years = df.iloc[:, 13]
  return reference_years