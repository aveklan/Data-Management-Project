INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x1::DECIMAL, '1 meal', 'Meal, Inexpensive Restaurant', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Meal, Inexpensive Restaurant'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x2::DECIMAL, 'three-course', 'Meal for 2 People, Mid-range Restaurant, Three-course', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Meal for 2 People, Mid-range Restaurant, Three-course'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x3::DECIMAL, 'combo', 'McMeal at McDonalds or Equivalent Combo Meal', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'McMeal at McDonalds or Equivalent Combo Meal'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x4::DECIMAL, '0.5 liter', 'Domestic Beer, draught', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Domestic Beer, draught'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x5::DECIMAL, '0.33 liter', 'Imported Beer, bottle', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Imported Beer, bottle'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x6::DECIMAL, '1 cup', 'Cappuccino, regular', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Cappuccino, regular'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x7::DECIMAL, '0.33 liter', 'Coke/Pepsi, bottle', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Coke/Pepsi, bottle'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x8::DECIMAL, '0.33 liter', 'Water, bottle', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Water, bottle'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x9::DECIMAL, '1 liter', 'Milk, regular', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Milk, regular'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x10::DECIMAL, '500g', 'Loaf of Fresh White Bread', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Loaf of Fresh White Bread'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x11::DECIMAL, '1kg', 'Rice, white', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'food' AND pc.ProductName = 'Rice, white'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x28::DECIMAL, 'one-way', 'One-way Ticket, Local Transport', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'One-way Ticket, Local Transport'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x29::DECIMAL, 'monthly', 'Monthly Pass, Regular Price', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Monthly Pass, Regular Price'
ON CONFLICT (KeyCity, KeyProductCategory) DO NOTHING;

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x30::DECIMAL, 'start', 'Taxi Start, Normal Tariff', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Taxi Start, Normal Tariff';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x31::DECIMAL, '1 km', 'Taxi 1km, Normal Tariff', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Taxi 1km, Normal Tariff';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x32::DECIMAL, '1 hour', 'Taxi 1hour Waiting, Normal Tariff', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Taxi 1hour Waiting, Normal Tariff';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x33::DECIMAL, '1 liter', 'Gasoline, per liter', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Gasoline, per liter';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x34::DECIMAL, '1 car', 'Volkswagen Golf or Equivalent New Car', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Volkswagen Golf or Equivalent New Car';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x35::DECIMAL, '1 car', 'Toyota Corolla Sedan or Equivalent New Car', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'transportation' AND pc.ProductName = 'Toyota Corolla Sedan or Equivalent New Car';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x36::DECIMAL, '1 apartment', 'Basic Utilities for 85m2 Apartment', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'bills' AND pc.ProductName = 'Basic Utilities for 85m2 Apartment';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x37::DECIMAL, '1 min', 'Prepaid Mobile Tariff Local, per min', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'bills' AND pc.ProductName = 'Prepaid Mobile Tariff Local, per min';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x38::DECIMAL, '1 subscription', 'Internet, 60 Mbps or More, Unlimited Data', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'bills' AND pc.ProductName = 'Internet, 60 Mbps or More, Unlimited Data';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x39::DECIMAL, '1 month', 'Fitness Club, Monthly Fee', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'hobby' AND pc.ProductName = 'Fitness Club, Monthly Fee';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x40::DECIMAL, '1 hour', 'Tennis Court Rent, Hour on Weekend', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'hobby' AND pc.ProductName = 'Tennis Court Rent, Hour on Weekend';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x41::DECIMAL, '1 ticket', 'Cinema, International Release, per Seat', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'hobby' AND pc.ProductName = 'Cinema, International Release, per Seat';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x42::DECIMAL, '1 month', 'Preschool or Kindergarten, Full Day, Private, Monthly', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'education' AND pc.ProductName = 'Preschool or Kindergarten, Full Day, Private, Monthly';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x43::DECIMAL, '1 year', 'International Primary School, Yearly for 1 Child', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'education' AND pc.ProductName = 'International Primary School, Yearly for 1 Child';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x44::DECIMAL, '1 pair', 'Pair of Jeans, Levis 501 or Similar', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'dressing' AND pc.ProductName = 'Pair of Jeans, Levis 501 or Similar';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x45::DECIMAL, '1 dress', 'Summer Dress in a Chain Store', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'dressing' AND pc.ProductName = 'Summer Dress in a Chain Store';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x46::DECIMAL, '1 pair', 'Pair of Nike Running Shoes, Mid-Range', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'dressing' AND pc.ProductName = 'Pair of Nike Running Shoes, Mid-Range';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x48::DECIMAL, '1 bedroom', 'Apartment, 1 bedroom, City Centre', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'realestate' AND pc.ProductName = 'Apartment, 1 bedroom, City Centre';

INSERT INTO Product (KeyCity, KeyProductCategory, Cost, Quantity, ProductDescription, DataQuality)
SELECT c.KeyCity, pc.KeyProductCategory, a.x54::DECIMAL, 'monthly salary', 'Average Monthly Net Salary After Tax', a.data_quality::INT
FROM allItemsTable AS a
JOIN City AS c ON a.city = c.City AND a.country = c.Country
JOIN ProductCategory AS pc ON pc.ProductCategory = 'realestate' AND pc.ProductName = 'Average Monthly Net Salary After Tax';
