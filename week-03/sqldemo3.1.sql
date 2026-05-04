-- Leon Poulson
-- April 20, 2026

SHOW databases;
USE northwind;
SHOW TABLES;
-- Example 1
SELECT ProductName, UnitPrice
FROM products;
-- Example 2
SELECT *
FROM products;
-- Example 3
SELECT ProductName AS 'Product', UnitPrice AS 'Price(USD)', UnitsInStock AS 'Stock'
FROM products;

-- Example 4
SELECT CompanyName, City, Country
FROM customers
	WHERE Country = 'Germany';

-- Example 5
SELECT ProductName, UnitPrice
FROM products
	WHERE UnitPrice > 50;

-- Example 6
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM orders
	WHERE ShipCountry = 'France';

-- Example 7
SELECT ProductName, UnitsInStock,ReorderLevel
FROM products
	WHERE ReorderLevel > UnitsInStock;
    
-- Example 8
SELECT OrderID, Freight
FROM orders
	WHERE Freight >= 100;

-- Example 10
SELECT ProductName, UnitPrice,UnitsInStock
FROM products
	WHERE UnitPrice > 20 AND UnitsInStock > 50;
    
-- Example 11
SELECT CompanyName, Country
FROM customers
	WHERE Country = 'UK' or 'Ireland';
    
-- Example 12

SELECT CategoryID, UnitPrice
FROM products
	WHERE (CategoryID = 1 OR 2) AND (UnitPrice < 20);

-- Example 13
SELECT CompanyName, Country
FROM customers
WHERE NOT Country = 'u.s.a' or'USA';

-- Example 14
SELECT ProductName
FROM products
WHERE NOT Discontinued;

-- Example 15
SELECT CompanyName,Country
FROM customers
WHERE Country IN ('Germany','France','Spain');

-- Example 16
SELECT ProductName,SupplierID
FROM products
WHERE SupplierID NOT IN ('1','2','3');

-- Example 17
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice BETWEEN 10 AND 20;

-- Example 19
SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS NULL;

-- Example 20
SELECT FirstName, LastName, Region
FROM employees
WHERE Region IS NOT NULL;

-- Example 2
SELECT OrderID, CompanyName, OrderDate
FROM Orders
JOIN Customers USING (CustomerID)
ORDER BY OrderDate
LIMIT 5;

-- Example 5
-- Customers with zero orders will show 0 in Order Count
SELECT c.CompanyName,
       COUNT(o.OrderID) AS 'Order Count'
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY `Order Count` ASC
LIMIT 5;




select count(orderID)
from orders;


SELECT sum(Freight) AS 'Total Freight', avg(Freight)
