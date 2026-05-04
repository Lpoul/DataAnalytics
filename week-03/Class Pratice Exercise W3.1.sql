USE northwind;
-- Q1
select categories.CategoryID, categories.CategoryName, categories.Description
from categories;

-- Q2
select products.ProductID, products.ProductName, products.QuantityPerUnit
from products
where products.QuantityPerUnit LIKE ('%box%');

select products.ProductID, products.ProductName, products.Discontinued
from products
where Discontinued = 1;

select employees.EmployeeID, concat(FirstName , ' ' ,LastName) AS FullName, employees.Title
from employees;

select CustomerID, CompanyName, Country
from customers
