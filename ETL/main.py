import obj.salaries.first_dataset as firstDataset
import pandas as pd

first_dataset_table = pd.DataFrame()

first_dataset_table['Job title'] = firstDataset.get_title()
first_dataset_table['Location']  = firstDataset.get_location()
first_dataset_table['Company Industry'] = firstDataset.get_company_industry()
first_dataset_table['Experience Level'] = firstDataset.get_experince_level()
first_dataset_table['Salary Amount'] = firstDataset.get_salary()
first_dataset_table['Salary Currency'] = firstDataset.get_salary_currency()
first_dataset_table['Conversion Ratio'] = firstDataset.get_conversion_ratio()
first_dataset_table['Reference Year'] = firstDataset.get_reference_year()

print (first_dataset_table)