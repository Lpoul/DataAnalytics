USE northwind;
-- Write a query to identify the products where the unit price is $7.50 or less
		SELECT ProductID, ProductName, UnitPrice
        FROM products
			WHERE UnitPrice <= 7.50;


 -- What are the products that we carry where we have no units on hand, but 1 or more
 -- units are on backorder?
							
		SELECT ProductName,UnitsInStock,UnitsOnOrder
        FROM products					
			WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;
        
-- Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.
		
		SELECT ProductName, CategoryName
        FROM products 
			JOIN categories 
				ON products.CategoryID = categories.CategoryID
					WHERE CategoryName = 'Seafood';

-- Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier.

	SELECT SupplierID,ProductID, ProductName 
    FROM products
		JOIN suppliers
			ON SupplierID
				WHERE CompanyName = 'Tokyo Traders';

-- How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question.

SELECT count(*) as EmployeeCount
	FROM employees;

SELECT EmployeeID, FirstName, LastName, Title
	FROM employees
		WHERE Title LIKE '%manager%';

        
