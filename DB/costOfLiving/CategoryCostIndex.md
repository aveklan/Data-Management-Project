INSERT INTO CategoryCostIndex (City, ProductCategory, CategoryCostIndex)
SELECT
city, -- City from allItemsTable
'food' AS ProductCategory, -- Set ProductCategory to 'food' for all rows
CAST(food_cost_index AS DECIMAL) -- Convert food_cost_index to DECIMAL
FROM
allItemsTable
WHERE
food_cost_index IS NOT NULL; -- Only insert rows where food_cost_index is not null
