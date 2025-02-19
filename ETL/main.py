import obj.salaries.first_dataset as firstDataset
import obj.salaries.second_dataset as secondDataset
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

#print (first_dataset_table)

second_dataset_table = pd.DataFrame()

second_dataset_table['Job title'] = secondDataset.get_title()
second_dataset_table['Location']  = secondDataset.get_location()
second_dataset_table['Company Industry'] = secondDataset.get_company_industry()
second_dataset_table['Experience Level'] = secondDataset.get_experince_level()
second_dataset_table['Salary Amount'] = secondDataset.get_salary()
second_dataset_table['Salary Currency'] = secondDataset.get_salary_currency()
second_dataset_table['Conversion Ratio'] = secondDataset.get_conversion_ratio()
second_dataset_table['Reference Year'] = secondDataset.get_reference_year()

#print (second_dataset_table)

final_table_salaries = pd.concat([first_dataset_table, second_dataset_table], ignore_index=True)
final_table_salaries.to_csv('final_table_salaries.csv', index=False)
print(final_table_salaries)