-- Salary comparison by experience level in France 
SELECT c.country, cu.currency, jt.job_title, jt.experience_level, ROUND(AVG(s.amount)::NUMERIC, 2) AS average_salary 
FROM salary s 
	JOIN country c ON s.key_c = c.key_c 
	JOIN currency cu ON s.key_cu = cu.key_cu
	JOIN job jt ON s.key_jt = jt.key_jt
	
WHERE cu.currency = 'EUR' 
	AND c.country = 'FR' 
	AND jt.experience_level != 'null' 
	AND jt.job_title ='Data Scientist'
GROUP BY
     jt.job_title, jt.experience_level, c.country, cu.currency
ORDER BY
    jt.experience_level, average_salary DESC
