WITH AverageSalary AS (
    SELECT c.country, ROUND(AVG(s.amount)::NUMERIC, 2) AS average_salary
	FROM salary s 
		JOIN country c ON s.key_c = c.key_c
		JOIN currency cu ON s.key_cu = cu.key_cu
	WHERE cu.currency = 'EUR'
	GROUP BY c.country 
),
CostOfLiving AS (
    SELECT ci.country, AVG(ci.categorycostindex) as global_cost_index
	FROM city c 
		JOIN categorycostindexnewkey ci ON c.city = ci.city AND ci.country = c.country
		JOIN productcategory pc ON pc.productcategory = ci.productcategory
	GROUP BY ci.country
)
SELECT
    s.country,
    s.average_salary,
    c.global_cost_index,
    ROUND(s.average_salary / c.global_cost_index, 2) AS salary_to_cost_ratio
FROM
    AverageSalary s
JOIN
    CostOfLiving c ON s.country = c.country
ORDER BY
    salary_to_cost_ratio DESC
LIMIT 10;