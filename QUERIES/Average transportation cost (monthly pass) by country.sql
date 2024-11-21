-- Average transportation cost (monthly pass) by country 
SELECT c.country, pc.productcategory, psc.productsubcategory, sog.servicesubscriptiontype, ROUND(AVG(p.cost)::NUMERIC, 2) as average_cost
FROM product p
	JOIN productcategory pc ON pc.keyproductcategory = p.keyproductcategory
	JOIN city c ON c.keycity = p.keycity
	JOIN productsubcategory psc ON psc.keyproductsubcategory = pc.keyproductsubcategory
	JOIN serviceorgood sog ON sog.keyserviceorgood = psc.keyserviceorgood
WHERE pc.productcategory = 'transportation' 
	AND psc.productsubcategory = 'Public Transportation'
	AND sog.servicesubscriptiontype = 'Monthly'
GROUP BY c.country, pc.productcategory, psc.productsubcategory, sog.servicesubscriptiontype
ORDER BY average_cost ASC