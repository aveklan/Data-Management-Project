-- Average cost of groceries per country ASC
SELECT pc.productcategory, c.country, psc.productsubcategory, ROUND(AVG(p.cost)::NUMERIC, 2) AS average_cost
FROM Product p 
	JOIN productcategory pc ON p.keyproductcategory = pc.keyproductcategory
	JOIN city c ON p.keycity = c.keycity
	JOIN productsubcategory psc ON pc.keyproductsubcategory = psc.keyproductsubcategory
WHERE pc.productcategory = 'food'
	AND psc.productsubcategory = 'Groceries'
GROUP BY pc.productcategory, c.country, psc.productsubcategory
ORDER BY average_cost ASC