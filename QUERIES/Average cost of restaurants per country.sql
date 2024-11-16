-- Average cost of restaurants per country
SELECT p.productdescription, pc.productcategory, c.country, ROUND(AVG(p.cost)::NUMERIC, 2) AS average_cost
FROM Product p 
	JOIN productcategory pc ON p.keyproductcategory = pc.keyproductcategory
	JOIN city c ON p.keycity = c.keycity
WHERE pc.productcategory = 'food' AND p.productdescription LIKE 'Meal for 2 People%'
GROUP BY p.productdescription, pc.productcategory, c.country
ORDER BY average_cost DESC
LIMIT 20