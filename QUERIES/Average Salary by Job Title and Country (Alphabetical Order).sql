-- Average salary by job title and contry in alphabetic order 
SELECT j.job_title, c.country, cu.currency, AVG (s.amount) AS average_salary 
FROM salary s 
	JOIN job j ON s.key_jt = j.key_jt
	JOIN country c ON s.key_c = c.key_c 
	JOIN currency cu ON s.key_cu = cu.key_cu
WHERE cu.currency = 'USD'
GROUP BY
    j.job_title, c.country, cu.currency
ORDER BY
    country ASC;