-- Fetch name of workers who earn higest salary 
Select first_name,last_name,salary
From Employees
Where Salary = (Select Max(salary) From Employees);

-- Fetch departments along with the total salaries paid for each of them

Select department_name, Sum(salary) As total_salary
From Employees 
Group By department_name;

-- Fetch nth max salaries from a table.

Select Distinct Salary 
From Employees As E1
Where n >= (Select Count(Distinct(salary)) from Employees As E2 Where E1.Salary <= E2.salary) Order by E1.salary Desc;
 

-- Fetch three max salaries from a table

Select Distinct Salary 
From Employees As E1
Where 3 >= (Select Count(Distinct(Salary) From Employees As E2 Where E1.Salary <= E2.Salary)) Order by E1.Salary Desc;

-- Fetch name of Employees having highest salary in each department. 

Select department.department_name, Max(employee.Salary)
From department join employee
On  employees.department_id = departments.department_id
Group by department.department_id