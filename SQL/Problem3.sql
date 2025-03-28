WITH RankedEmployees AS (
    SELECT 
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS ranking,
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary
    FROM 
        Employee e INNER JOIN
        Department d 
    ON 
        e.departmentId = d.id
)
SELECT 
    Department,
    Employee,
    Salary
FROM 
    RankedEmployees
WHERE
    ranking <= 3