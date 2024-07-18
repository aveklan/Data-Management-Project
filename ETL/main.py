import obj.salaries.first_dataset as firstDataset
import pandas as pd

first_dataset_table = pd.DataFrame()

first_dataset_table['Job title'] = firstDataset.get_title()
first_dataset_table['Location']  = firstDataset.get_location()
first_dataset_table['Salary'] = firstDataset.get_salary()
first_dataset_table['Company Industru'] = firstDataset.get_company_industry()
first_dataset_table['Experience Level'] = firstDataset.get_experince_level()

print (first_dataset_table)