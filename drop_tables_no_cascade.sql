-- מחיקת טבלאות קישור (כי יש בהן מפתחות זרים)
DROP TABLE IF EXISTS OrderDish;
DROP TABLE IF EXISTS Reviews;

-- מחיקת ישויות תלויות
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Delivers;

-- מחיקת ישויות עצמאיות
DROP TABLE IF EXISTS Dishes;
DROP TABLE IF EXISTS customers;

