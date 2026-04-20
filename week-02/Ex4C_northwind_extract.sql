-- The name of the table that holds the items Northwind sells is called products.
-- The name of the table that holds the categories of the items Northwind sells is called Categories.
use northwind;
select * from employees;

-- The Northwind employee whose name makes it look like she is a bird is Peacock Margaret.
select * from products;

-- 77 records is what gets returned from retrieving the products table.
-- There are two ways to limit your query to only retrueve 10 rows, you can have it set the limit paramiter as listed below or you can go to the dropdown menu and set it to limit to 10 rows.
-- select * from products limit 10; I did not use a source to find this answer, I have prior SQL knowledge.

select * from categories;

-- The category id of seafood is 8. 
select * from categories order by CategoryID desc limit 1;

select OrderID, OrderDate, ShipName, ShipCountry from orders order by OrderDate ASC limit 50;
