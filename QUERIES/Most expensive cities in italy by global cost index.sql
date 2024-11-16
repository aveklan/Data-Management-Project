-- Most expensive cities in italy by global cost index
SELECT ci.city, ci.country, AVG(ci.categorycostindex) as global_cost_index
FROM city c 
	JOIN categorycostindexnewkey ci ON c.city = ci.city AND ci.country = c.country
	JOIN productcategory pc ON pc.productcategory = ci.productcategory
WHERE c.country = 'Italy'
GROUP BY ci.city, ci.country
ORDER BY global_cost_index DESC
LIMIT 100