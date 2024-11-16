-- Average cost of Apartment Rent per country DESC full join
SELECT c.country, psc.productsubcategory, ROUND(AVG(p.cost)::NUMERIC, 2) AS average_cost
FROM Product p 
	JOIN productcategory pc ON p.keyproductcategory = pc.keyproductcategory
	JOIN city c ON p.keycity = c.keycity
	JOIN productsubcategory psc ON pc.keyproductsubcategory = psc.keyproductsubcategory
	JOIN serviceorgood sg ON psc.keyserviceorgood = sg.keyserviceorgood
WHERE pc.productcategory = 'realestate'
	AND psc.consumptionLocation = 'Home'
	AND sg.servicedescription = 'Apartment Rent'
GROUP BY c.country, psc.productsubcategory
ORDER BY average_cost DESC