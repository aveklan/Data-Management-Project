CREATE TABLE ServiceOrGood
(
    KeyServiceOrGood SERIAL PRIMARY KEY,
    ServiceOrGood TEXT NOT NULL,
    ServiceDescription TEXT,
    ServiceSubscriptionType TEXT
);

CREATE TABLE ProductSubCategory
(
    KeyProductSubCategory SERIAL PRIMARY KEY,
    ProductSubCategory TEXT NOT NULL,
    KeyServiceOrGood INT REFERENCES ServiceOrGood(KeyServiceOrGood),
    PriceType TEXT,
    BrandType TEXT,
    IsLuxuryItem BOOLEAN,
    BrandNameOrModel TEXT,
    ConsumptionLocation TEXT
);

CREATE TABLE CategoryCostIndex
(
    KeyCategoryCostIndex SERIAL PRIMARY KEY,
    City TEXT NOT NULL,
    ProductCategory TEXT NOT NULL,
    CategoryCostIndex DECIMAL
);

CREATE TABLE ProductCategory
(
    KeyProductCategory SERIAL PRIMARY KEY,
    ProductCategory TEXT NOT NULL,
    ProductName TEXT NOT NULL,
    KeyCategoryCostIndex INT REFERENCES CategoryCostIndex(KeyCategoryCostIndex)
);

CREATE TABLE City
(
    KeyCity SERIAL PRIMARY KEY,
    City TEXT NOT NULL,
    Country TEXT NOT NULL,
    KeyCategoryCostIndex INT REFERENCES CategoryCostIndex(KeyCategoryCostIndex)
);

CREATE TABLE Product
(
    KeyCity INT REFERENCES City(KeyCity),
    KeyProductCategory INT REFERENCES ProductCategory(KeyProductCategory),
    Cost DECIMAL NOT NULL,
    Quantity DECIMAL,
    ProductDescription TEXT,
    DataQuality INT,
    PRIMARY KEY (KeyCity, KeyProductCategory)
);

CREATE TABLE allItemsTable
(
    cityIndex SERIAL PRIMARY KEY,
    "city" TEXT,
    "country" TEXT,
    "x1" TEXT,
    "x2" TEXT,
    "x3" TEXT,
    "x4" TEXT,
    "x5" TEXT,
    "x6" TEXT,
    "x7" TEXT,
    "x8" TEXT,
    "x9" TEXT,
    "x10" TEXT,
    "x11" TEXT,
    "x12" TEXT,
    "x13" TEXT,
    "x14" TEXT,
    "x15" TEXT,
    "x16" TEXT,
    "x17" TEXT,
    "x18" TEXT,
    "x19" TEXT,
    "x20" TEXT,
    "x21" TEXT,
    "x22" TEXT,
    "x23" TEXT,
    "x24" TEXT,
    "x25" TEXT,
    "x26" TEXT,
    "x27" TEXT,
    "x28" TEXT,
    "x29" TEXT,
    "x30" TEXT,
    "x31" TEXT,
    "x32" TEXT,
    "x33" TEXT,
    "x34" TEXT,
    "x35" TEXT,
    "x36" TEXT,
    "x37" TEXT,
    "x38" TEXT,
    "x39" TEXT,
    "x40" TEXT,
    "x41" TEXT,
    "x42" TEXT,
    "x43" TEXT,
    "x44" TEXT,
    "x45" TEXT,
    "x46" TEXT,
    "x47" TEXT,
    "x48" TEXT,
    "x49" TEXT,
    "x50" TEXT,
    "x51" TEXT,
    "x52" TEXT,
    "x53" TEXT,
    "x54" TEXT,
    "x55" TEXT,
    "data_quality" TEXT,
    "food_cost_index" TEXT,
    "transportation_cost_index" TEXT,
    "bills_cost_index" TEXT,
    "hobby_cost_index" TEXT,
    "education_cost_index" TEXT,
    "dressing_cost_index" TEXT,
    "realestate_cost_index" TEXT
);

COPY allItemsTable("city", "country", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", 
"x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21", 
"x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31", "x32", "x33", 
"x34", "x35", "x36", "x37", "x38", "x39", "x40", "x41", "x42", "x43", "x44", "x45", "x46", 
"x47", "x48", "x49", "x50", "x51", "x52", "x53", "x54", "x55", "data_quality", "food_cost_index", 
"transportation_cost_index", "bills_cost_index", "hobby_cost_index", "education_cost_index", 
"dressing_cost_index", "realestate_cost_index") 
FROM 'C:\Users\Aveklan\Documents\Uni\La Sapienza\Data Management\Project\Data-Management-Project\global_cost_of_living_with_Indexes.csv' 
DELIMITER ',' 
CSV HEADER;
