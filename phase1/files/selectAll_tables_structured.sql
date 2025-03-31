-- שליפת כל הנתונים מכל הטבלאות
SELECT * FROM OrderDish;
SELECT * FROM Reviews;
SELECT * FROM Orders;
SELECT * FROM Payment;
SELECT * FROM Delivers;
SELECT * FROM Dishes;
SELECT * FROM customers;

-- ספירת כמות הרשומות בכל טבלה
SELECT 'OrderDish' AS table_name, COUNT(*) FROM OrderDish;
SELECT 'Reviews' AS table_name, COUNT(*) FROM Reviews;
SELECT 'Orders' AS table_name, COUNT(*) FROM Orders;
SELECT 'Payment' AS table_name, COUNT(*) FROM Payment;
SELECT 'Delivers' AS table_name, COUNT(*) FROM Delivers;
SELECT 'Dishes' AS table_name, COUNT(*) FROM Dishes;
SELECT 'customers' AS table_name, COUNT(*) FROM customers;
