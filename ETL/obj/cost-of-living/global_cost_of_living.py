import pandas as pd
import numpy as np
import os


relative_csv_path = os.path.join(
    "ETL", "raw_data", "cost_of_living", "global-cost-of-living.csv"
)
raw_data = pd.read_csv(relative_csv_path)

output_path = os.path.join("global_cost_of_living_with_Indexes.xlsx")


def calculate_mean(column):
    current_column = raw_data.iloc[:, column]
    sum = 0
    valueCounter = 0

    for value in current_column:
        if not (pd.isna(value)):
            sum = sum + value
            valueCounter += 1

    return round((sum / valueCounter), 2)


def insert_mean_value(column, mean_value):
    current_column = raw_data.iloc[:, column]
    raw_data.iloc[:, column] = current_column.fillna(mean_value)


def calculate_cost_index(first_item, last_item):
    index_columns = raw_data.iloc[:, first_item:last_item]

    log_values = np.log(index_columns.where(index_columns > 0))
    log_sums = log_values.sum(axis=1, skipna=True).to_numpy()

    mean_value = np.mean(log_sums)
    closest_to_mean = log_sums[np.abs(log_sums - mean_value).argmin()]
    percentages = 100 + (log_sums - closest_to_mean) / closest_to_mean * 100

    return percentages


def main():
    for column in range(2, 58):
        current_mean_value = calculate_mean(column)
        insert_mean_value(column, current_mean_value)

    food_cost_index = calculate_cost_index(2, 28)
    raw_data["food_cost_index"] = food_cost_index

    transportation_cost_index = calculate_cost_index(29, 37)
    raw_data["transportation_cost_index"] = transportation_cost_index

    bills_cost_index = calculate_cost_index(37, 40)
    raw_data["bills_cost_index"] = bills_cost_index

    hobby_cost_index = calculate_cost_index(40, 43)
    raw_data["hobby_cost_index"] = hobby_cost_index

    education_cost_index = calculate_cost_index(43, 45)
    raw_data["education_cost_index"] = education_cost_index

    dressing_cost_index = calculate_cost_index(45, 49)
    raw_data["dressing_cost_index"] = dressing_cost_index

    realestate_cost_index = calculate_cost_index(49, 55)
    raw_data["realestate_cost_index"] = realestate_cost_index

    raw_data.to_excel(output_path, index=False)


if __name__ == "__main__":
    main()
