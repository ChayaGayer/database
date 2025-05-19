-- =============================
-- View 1: dishes_with_orders
CREATE VIEW dishes_with_orders AS 
SELECT 
    d.dishid,
    d.dishname,
    d.category,
    o.orderid,
    o.orderdate,
    o.totalamount
FROM 
    public.dishes d
 NATURAL JOIN
    public.orders o 

-- Query 1: High value orders per dish
SELECT *
FROM dishes_with_orders
WHERE totalamount > 200;

-- Query 2: Count of orders per dish
SELECT dishid, dishname, COUNT(orderid) AS order_count
FROM dishes_with_orders
GROUP BY dishid, dishname

SELECT * FROM dishes_with_orders LIMIT 5;




-- =============================
-- View 2: workers_by_status
-- Source: Delivery Department
-- =============================
CREATE VIEW workers_by_status AS
SELECT 
    w.wid,
    w.wfirstname,
    w.wstatus,
    COUNT(o.orderid) AS orders_count,
    AVG(o.totalamount) AS avg_order_value
FROM 
    public.worker w
LEFT JOIN 
    public.orders o ON w.wid = o.deliveryid
GROUP BY 
    w.wid, w.wfirstname, w.wstatus;

-- Query 1: Active workers with more than 3 deliveries
SELECT *
FROM workers_by_status
WHERE wstatus = 'Active' AND orders_count > 3;

-- Query 2: Average order value by worker status
SELECT wstatus, AVG(avg_order_value) AS avg_value_per_status
FROM workers_by_status
GROUP BY wstatus;


CREATE VIEW worker_morning_shifts AS
SELECT 
    w.wid,
    w.wfirstname || ' ' || w.wlastname AS full_name,
    w.salary,
    w.wstatus,
    s.shid,
    s.starttime,
    s.endtime
FROM 
    public.worker w
CROSS JOIN 
    public.shift s
WHERE 
    s.starttime < '12:00';


SELECT full_name, COUNT(shid) AS morning_shift_count
FROM worker_morning_shifts
GROUP BY full_name
ORDER BY morning_shift_count DESC;

SELECT full_name, starttime, endtime
FROM worker_morning_shifts
WHERE endtime < '13:00'
ORDER BY endtime;


