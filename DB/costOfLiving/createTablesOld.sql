CREATE TABLE
IF NOT EXISTS Transportation
(
    KeyTransportation SERIAL PRIMARY KEY, 
    "Transportation cost" NUMERIC,        
    "Cost at km" NUMERIC,                 
    "Transportation Type" TEXT,   
    "Service Description" TEXT            
);

CREATE TABLE
IF NOT EXISTS Food
(
    KeyFood SERIAL PRIMARY KEY, 
    "Food cost" NUMERIC,        
    "Food Type" TEXT,                
    "Food quantity" TEXT,   
    "Food Name" TEXT           
);

CREATE TABLE
IF NOT EXISTS Education
(
    KeyEducation SERIAL PRIMARY KEY, 
    "Education cost" NUMERIC,        
    "Period of time" TEXT,                
    "Level" TEXT,   
    "School type" TEXT            
);

CREATE TABLE
IF NOT EXISTS RealEstate
(
    KeyRealEstate SERIAL PRIMARY KEY, 
    "RealEstate cost" NUMERIC,       
    "Car model" TEXT,                
    "House type" TEXT,   
    "City area" TEXT,            
	"Rooms" NUMERIC,  
	"Interest Rate" NUMERIC
);
CREATE TABLE
IF NOT EXISTS Dressing
(

    KeyDressing SERIAL PRIMARY KEY, 
    "Dressing cost" NUMERIC,       
    "Dressing type" TEXT,                
    "Target Usage" TEXT
);

CREATE TABLE
IF NOT EXISTS Dressing
(
    KeyDressing SERIAL PRIMARY KEY, 
    "Dressing cost" NUMERIC,       
    "Dressing type" TEXT,                
    "Target Usage" TEXT
);

CREATE TABLE
IF NOT EXISTS Hobby
(
    KeyHobby SERIAL PRIMARY KEY, 
    "Hobby cost" NUMERIC,       
    "Hobby type" TEXT,                
    "Subscription type" TEXT
);

CREATE TABLE
IF NOT EXISTS Bills
(
    KeyBills SERIAL PRIMARY KEY, 
    "Bills cost" NUMERIC,       
    "Bills type" TEXT,                
    "Characterization" TEXT
);

CREATE TABLE
IF NOT EXISTS City
(
    KeyCity SERIAL PRIMARY KEY,   
    "City" TEXT,                
    "Country" TEXT
);

CREATE TABLE
IF NOT EXISTS CostOfLiving
(
    KeyCostOfLiving SERIAL PRIMARY KEY,   
	KeyTransportation INT REFERENCES Transportation
(KeyTransportation),  
    KeyFood INT REFERENCES Food
(KeyFood),  
	KeyEducation INT REFERENCES Education
(KeyEducation),  
	KeyRealEstate INT REFERENCES RealEstate
(KeyRealEstate), 
	KeyDressing INT REFERENCES Dressing
(KeyDressing), 
	KeyHobby INT REFERENCES Hobby
(KeyHobby), 
	KeyBills INT REFERENCES Bills
(KeyBills),
	KeyCity INT REFERENCES City
(KeyCity),
	"Transportation cost index" NUMERIC,  
	"Food cost index" NUMERIC,  
	"Education cost index" NUMERIC,
	"Realestate cost index" NUMERIC,
	"Dressing cost index" NUMERIC,	
	"Hobby cost index" NUMERIC,	
	"Bills cost index" NUMERIC,	
	"Country cost index" NUMERIC	
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





Dressing
INSERT INTO Dressing
    ("Dressing cost", "Dressing type", "Target Usage")
SELECT
    CAST("x45" AS NUMERIC),
    'Summer Dress',
    'Casual'
FROM allItemsTable

Target
usage is either Casual or Elegant