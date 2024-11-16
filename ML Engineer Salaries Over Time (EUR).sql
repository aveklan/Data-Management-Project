-- ML Engineer Salaries Over Time (EUR)
SELECT y.year, j.job_title, cu.currency, ROUND(AVG(s.amount)::NUMERIC, 2) AS average_salary
FROM salary s 
    JOIN year y ON s.key_ry = y.key_ry
    JOIN job j ON s.key_jt = j.key_jt
    JOIN currency cu ON s.key_cu = cu.key_cu
WHERE j.job_title = 'ML Engineer' AND cu.currency = 'EUR'
GROUP BY y.year, j.job_title, cu.currency
ORDER BY y.year;
