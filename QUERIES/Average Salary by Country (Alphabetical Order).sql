-- Average Salary by Country (Alphabetical Order)
SELECT c.country, cu.currency, ROUND(AVG(s.amount)::NUMERIC, 2) AS average_salary 
FROM salary s 
	JOIN country c ON s.key_c = c.key_c 
	JOIN currency cu ON s.key_cu = cu.key_cu
WHERE cu.currency = 'EUR'
GROUP BY
     c.country, cu.currency
ORDER BY
    country ASC
LIMIT 20;