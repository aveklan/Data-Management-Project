import pandas as pd
import os

import pandas as pd
import os

# Load the first CSV file
relative_csv_path_first = os.path.join(
    "ETL", "raw_data", "cost_of_living", "global-cost-of-living.csv"
)
raw_data = pd.read_csv(relative_csv_path_first)

# Load the second CSV file
relative_csv_path_second = os.path.join(
    "ETL", "raw_data", "cost_of_living", "cost-of-living.csv"
)
raw_data_second_dataset = pd.read_csv(relative_csv_path_second)

# Extract unique "city" and "country" combinations from both datasets
first_dataset_cities = raw_data[["city", "country"]].drop_duplicates()
second_dataset_cities = []

for col in raw_data_second_dataset.columns[
    2:
]:  # Start from the third column if first two are actual data
    # Split by commas and take the first and last part
    parts = col.split(",")
    city = parts[0]  # First part before the first comma
    country = parts[-1]  # Last part after the last comma
    # Append to the list
    second_dataset_cities.append([city.strip(), country.strip()])

first_dataset_cities_set = set(first_dataset_cities.apply(tuple, axis=1))

# Initialize a list to hold city-country pairs from the second dataset that are not in the first dataset
missing_city_country_pairs = []

# Iterate over the city-country pairs from the second dataset
for city, country in second_dataset_cities:
    # Check if the city-country pair is not in the first dataset
    if (city, country) not in first_dataset_cities_set:
        missing_city_country_pairs.append([city, country])

# Print the result (or process further)
print("City-Country pairs missing in the first dataset:")
for pair in missing_city_country_pairs:
    print(pair)
