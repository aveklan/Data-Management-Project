-- TOP 10 highest paying industries
SELECT ci.company_industry, cu.currency, ROUND(AVG(s.amount)::NUMERIC, 2) AS average_salary
FROM salary s 
	JOIN company ci ON s.key_ci = ci.key_ci
	JOIN currency cu ON s.key_cu = cu.key_cu
WHERE cu.currency = 'USD' AND company_industry != 'Null'
GROUP BY ci.company_industry, cu.currency
ORDER BY average_salary DESC
LIMIT 10;