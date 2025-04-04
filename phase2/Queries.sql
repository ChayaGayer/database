
-- 1. SELECT: Get all orders with customer name, delivery status, and payment method
SELECT o.OrderID, c.CustomerName, o.OrderDate, d.DeliveryStatus, p.PaymentMethod, o.TotalAmount
FROM Orders o
JOIN customers c ON o.CustomerID = c.CustomerID
JOIN Delivers d ON o.DeliveryID = d.DeliveryID
JOIN Payment p ON o.PaymentID = p.PaymentID;

-- 2. SELECT: Total amount of orders per customer (with customer info)
SELECT c.CustomerName, COUNT(o.OrderID) AS OrderCount, SUM(o.TotalAmount) AS TotalSpent
FROM customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName
ORDER BY TotalSpent DESC;

-- 3. SELECT: Average rating per customer and number of reviews
SELECT c.CustomerName, AVG(r.Rating) AS AvgRating, COUNT(r.ReviewID) AS NumReviews
FROM customers c
JOIN Reviews r ON c.CustomerID = r.CustomerID
GROUP BY c.CustomerName;

-- 4. SELECT: Top 3 most ordered dishes
SELECT d.DishName, SUM(od.Amount) AS TotalOrdered
FROM Dishes d
JOIN OrderDish od ON d.DishID = od.DishID
GROUP BY d.DishName
ORDER BY TotalOrdered DESC
LIMIT 3;

-- 5. SELECT: Orders placed in the last 30 days
SELECT o.OrderID, c.CustomerName, o.OrderDate, o.TotalAmount
FROM Orders o
JOIN customers c ON o.CustomerID = c.CustomerID
WHERE o.OrderDate >= CURRENT_DATE - INTERVAL '30 days';

-- 6. SELECT: Orders grouped by month and year
SELECT EXTRACT(YEAR FROM OrderDate) AS OrderYear,
       EXTRACT(MONTH FROM OrderDate) AS OrderMonth,
       COUNT(*) AS NumOrders,
       SUM(TotalAmount) AS TotalRevenue
FROM Orders
GROUP BY OrderYear, OrderMonth
ORDER BY OrderYear DESC, OrderMonth DESC;

-- 7. SELECT: Dishes with average amount ordered greater than 2
SELECT d.DishName, AVG(od.Amount) AS AvgAmount
FROM Dishes d
JOIN OrderDish od ON d.DishID = od.DishID
GROUP BY d.DishName
HAVING AVG(od.Amount) > 2;

-- 8. SELECT: Customers who never placed an order
SELECT c.CustomerID, c.CustomerName
FROM customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

-- 9. DELETE: Remove reviews older than 1 year
DELETE FROM Reviews
WHERE ReviewDate < CURRENT_DATE - INTERVAL '1 year';

-- 10. DELETE: Delete orders with total amount = 0
DELETE FROM Orders
WHERE TotalAmount = 0;

-- 11. DELETE: Delete customers with no orders or reviews
DELETE FROM customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders)
  AND CustomerID NOT IN (SELECT CustomerID FROM Reviews);

-- 12. UPDATE: Set delivery status to 'Completed' for past deliveries
UPDATE Delivers
SET DeliveryStatus = 'Completed'
WHERE DeliveryDate < CURRENT_DATE;

-- 13. UPDATE: Increase price of dishes in category 'Premium' by 10%
UPDATE Dishes
SET Price = Price * 1.10
WHERE Category = 'Premium';

-- 14. UPDATE: Mark reviews with rating 1 as 'Needs follow-up' in comment
UPDATE Reviews
SET ReviewComment = 'Needs follow-up'
WHERE Rating = 1;
