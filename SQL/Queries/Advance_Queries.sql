--Fetch the employees whose salary is greater than average salary of all the employees
    --IF average salary column is present
    SELECT e.name,e.salary 
    FROM Employee as e
    WHERE e.salary > e.avg_salary; 

    --IF average salary column is not present
    SELECT e.name,e.salary
    FROM Employee as e
    WHERE e.salary > (SELECT CAST(AVG(salary) AS INT) FROM Employees) 


--Find stores whos sales were better than average sales across all the stores

SELECT * 
FROM(
    SELECT s.store_name,s.cost AS total_store_sale 
    FROM Sales as s
    GROUP BY s.store_name;  
    ) AS Total_sales
    JOIN 
    (SELECT CAST(AVG(total_store_sale) AS INT) AS avg_sales
    FROM( 
    SELECT s.store_name,s.cost AS total_store_sale 
    FROM Sales as s
    GROUP BY s.store_name;  
    )) AS Average_sales
    ON Total_sales.total_store_sale > Average_sales.avg_sales


WITH Total_sales(store_id, total_sales_per_store) AS 
      (SELECT store_id, SUM(cost) as total_sales_per_store
       FROM Sales s
       Group By s.store_id),
     Avg_sales (avg_sales_for_all_stores) AS 
      (SELECT CAST(AVG(total_sales_per_store) AS INT) AS average_sales_for_all_stores
       FROM Total_Sales)
SELECT 
WITH Total_sales ts JOIN Avg_sales av
ON ts.total_sales_per_store > av.avg_sales_for_all_stores


    )
------------------------------------------------------------------------------

SELECT * 
FROM (
      SELECT e1.job AS Job_Title , SUM(e1.sal) AS Total_Salary 
      FROM emp e1
      GROUP BY job
	 ) t1
     JOIN
     (
	  SELECT AVG(Total_Salary) AS Average_Salary
      FROM (SELECT e2.job AS Job_Title , SUM(e2.sal) AS Total_Salary 
            FROM emp e2
            GROUP BY job)
     ) t2 ON t1.Total_Salary > t2.Average_Salary
