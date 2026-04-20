USE northwind;
-- Write a query to identify the products where the unit price is $7.50 or less
		SELECT ProductID, ProductName, UnitPrice FROM products
		WHERE UnitPrice <= 7.50;


 -- What are the products that we carry where we have no units on hand, but 1 or more
 -- units are on backorder?
							
		SELECT ProductName,UnitsInStock,UnitsOnOrder FROM products					
        WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;
        
-- Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.
		
		SELECT CategoryID FROM products;
        SELECT CategoryName FROM categories;
        
