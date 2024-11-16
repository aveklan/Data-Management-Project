-- Average cost of Apartment Rent per country DESC
SELECT c.country, pc.productcategory, ROUND(AVG(p.cost)::NUMERIC, 2) AS average_cost
FROM Product p 
	JOIN productcategory pc ON p.keyproductcategory = pc.keyproductcategory
	JOIN city c ON p.keycity = c.keycity
WHERE pc.productcategory = 'realestate'
GROUP BY c.country, pc.productcategory
ORDER BY average_cost DESC