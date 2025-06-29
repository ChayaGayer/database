
# Project: Catering Database

## Phase 1: Design and Build the Database

### Introduction
The **Catering Database** is designed to efficiently manage information related to customers, orders, dishes, deliveries, and payments. The system ensures smooth tracking of operations, data organization, and customer feedback.

### Purpose
The purpose of the Catering database is to:
- Manage customer and order information
- Track deliveries and payment methods
- Store details of dishes, quantities, and pricing
- Collect and analyze customer reviews

### ERD (Entity Relationship Diagram)
![image](https://github.com/user-attachments/assets/faf7104d-55e3-42c1-9c1a-75708acb41e3)


### DSD (Data Structure Diagram)
![image](https://github.com/user-attachments/assets/13f1b4e1-6cca-4117-9198-02d69b9f4398)


### SQL Scripts
The following scripts are provided for interacting with the database:
- 📜 [create_tables.sql](phase1/files/create_tables_user.sql) – Create database tables
- 📜 [insert_tables.sql](phase1/files/insert_tables_fixed.sql) – Insert sample data
- 📜 [drop_tables.sql](phase1/files/drop_tables_no_cascade.sql) – Drop all tables
- 📜 [selectAll_tables.sql](phase1/files/selectAll_tables_structured.sql) – Select data from all tables

### Data
using Python to generate CSV files with faker package to
automate the generation of 400 rows per table
![image](https://github.com/user-attachments/assets/92eaa40d-a7e2-4994-a243-fbe6f3b993d4) 

using Mockaroo
Mockaroo was used to generate realistic CSV data files:

📜 customers.csv – 400 customers with valid names, emails, phones, and addresses
![image](https://github.com/user-attachments/assets/99f47257-ee1d-49e9-9c63-9f4f7b7e77b9)

results for the command SELECT COUNT(*) FROM :
![image](https://github.com/user-attachments/assets/a0e4b05f-03c2-43a0-8aed-daa52cbd0ee0)

 using generatedata. to create csv file
 
![image](https://github.com/user-attachments/assets/976791df-b243-4f89-98a5-cf6a3f9ec4d8)


### Backup
[View the backup directory](phase1/files/backup3)

## Phase 2

**This phase includes a series of SQL queries and data manipulations to analyze and update the database. Each query is followed by an explanation and screenshots showing the results or effects.**
### **Queries**
1. Orders with Customer InfoShows each order with the customer name, delivery status, payment method, date, and total amount.

![cc991428-d541-4b66-a3a5-5cafbfad7ad8](https://github.com/user-attachments/assets/a8149817-e58c-4df6-a88c-e0af084b872e)
2. Orders Summary by CustomerDisplays how many orders each customer made and how much they spent in total.

![b0f364bf-0a55-40f9-bc20-1091afd87a3b](https://github.com/user-attachments/assets/cbd65d25-e3e2-4cc4-b0af-d60eb19537e1)
3. Average Review RatingsShows the average rating and number of reviews per customer.

![618f6a8c-80c0-48a5-937b-d2712715b509](https://github.com/user-attachments/assets/45e33d78-6e0f-4077-9139-21178e22b031)
4. Top 3 Most Ordered DishesDisplays the 3 most frequently ordered dishes.

![ed5e8821-61d7-443b-afcc-7b9c7299cb2c](https://github.com/user-attachments/assets/44775be2-75ee-41cc-8cf0-82491adcce0c)
5. Recent Orders (Last 30 Days)Shows all orders placed within the last 30 days.

![0fa94115-37eb-4e57-a2ae-58a338fef5b2](https://github.com/user-attachments/assets/ce7eba20-a819-4ce2-b3cf-65cd50f62bf2)
6. Monthly Orders & Revenue SummarySummarizes the number of orders and total revenue by month and year.

![1fff6818-43bd-4614-b72c-931a94e85d1a](https://github.com/user-attachments/assets/3daec6b2-320d-4175-b041-20917430098b)
7. Dishes with Avg Quantity > 2Finds dishes ordered with an average quantity above 2.

![14e1c756-39ba-4799-b148-58499201bef8](https://github.com/user-attachments/assets/3633b91a-3f3d-4ca8-b482-f8268a4af1dd)
8. Customers with No OrdersIdentifies customers who have never made an order.

![216aacba-9b3c-4727-b4d6-bddf59c8d75c](https://github.com/user-attachments/assets/b7aa50f3-12b6-4435-a4b7-7a030c80a975)
9.9. Delete Old ReviewsDeletes reviews older than one year.
Before Deletion

![787846ab-6b50-49a7-9ef2-2df06cb46430](https://github.com/user-attachments/assets/ef9ba10c-9824-47b6-9e23-30bb35468754)
This query deletes all reviews that were written more than one year ago.
After Deletion
![929e458e-1dfe-4c57-9b67-01e1fcc3c923](https://github.com/user-attachments/assets/9ef9e4b3-72ce-4517-a277-cba3ff9090ad)

![image](https://github.com/user-attachments/assets/fba827e4-9a34-477e-b639-30550e68abd9)
10. Delete Orders with Total = 0Removes orders where the total amount is 0.
Before Deletion

![image](https://github.com/user-attachments/assets/301f70d2-2fe7-4742-8fc6-97699c15e71e)
After Deletion

![image](https://github.com/user-attachments/assets/7aff2ba9-8744-4456-8168-3459fccb15f9)
11. Delete Inactive CustomersDeletes customers with no orders and no reviews.

![image](https://github.com/user-attachments/assets/af820d1e-8891-4926-b955-9147ac867aa3)
After Deletion

![image](https://github.com/user-attachments/assets/08a1d389-7f12-4377-9485-7c7343309f68)

![image](https://github.com/user-attachments/assets/00437c22-1fbf-4547-8412-5a487a8efabf)
12.This query updates the delivery status to 'Completed' for all deliveries with a past date.
Before

![image](https://github.com/user-attachments/assets/7178c342-8a45-41af-a8fb-9618dbf59582)
After

![image](https://github.com/user-attachments/assets/df0a53d1-39cc-4579-b306-c72cb470a4cd)

![image](https://github.com/user-attachments/assets/0e9c6e6f-f3fd-4874-be84-c4367befdf9a)
13. Increase Price for Premium DishesRaises price by 10% for all dishes in the 'Premium' category.

![image](https://github.com/user-attachments/assets/71853a22-d795-4c98-83ba-1ec4cb9f85ab)
After

![image](https://github.com/user-attachments/assets/c2ef7756-0e93-4ae7-b587-5f7f65ead20d)

![image](https://github.com/user-attachments/assets/0718655e-9ff6-4922-b80f-c4f903be0794)
14. Update Low-Rated ReviewsChanges comment of reviews rated 1 to 'Needs follow-up'.

![image](https://github.com/user-attachments/assets/4f9c2158-a8c0-4ec0-8718-913acc0cf27c)
After

![image](https://github.com/user-attachments/assets/a4d03278-dc97-4758-8fe6-efc3bcabcc5c)

![image](https://github.com/user-attachments/assets/f1feb764-5e24-4743-9728-c2118430d8d4)

### Constraints

Constraint 1: NOT NULL on Reviews.ReviewCommentEnforces that every review must have a comment.

![image](https://github.com/user-attachments/assets/a9581a6f-7350-4bde-b3f0-786efee34576)
After

![image](https://github.com/user-attachments/assets/34b0897f-60f3-41eb-84df-fd4b2f056338)

Constraint 2: CHECK on Orders.TotalAmountEnsures the total amount in orders is greater than 0.

Before

![image](https://github.com/user-attachments/assets/d8fd6017-e826-4bd4-8517-ce0c2fb01c9c)
After

![image](https://github.com/user-attachments/assets/9fcba756-244f-404b-969f-ed29e1710b94)
Constraint 3: DEFAULT on Delivers.DeliveryStatusAdds default value 'status1' to DeliveryStatus if not provided..

Before

![image](https://github.com/user-attachments/assets/15a9315a-6b2e-4558-9909-0c41919388c6)
After


![image](https://github.com/user-attachments/assets/3d91fb83-56fa-4f0a-ae5e-b46173e80b5e)
![image](https://github.com/user-attachments/assets/2b2d5b8a-0059-4167-a6f6-4890aa270560)


# Phase 3

## 1. Diagrams

### DSD – New Department
![image](https://github.com/ChayaGayer/database/blob/master/Phase3/DSD.png)

### ERD – New Department
![image](https://github.com/ChayaGayer/database/blob/master/Phase3/ERD.png)

###  ERD – Combined System
![image](https://github.com/ChayaGayer/database/blob/master/Phase3/DSDnew.png)

### DSD – After Integration
![image](https://github.com/ChayaGayer/database/blob/master/Phase3/ERDnew.png)

---

###  Integration Decisions
Initial Step: Load Both Backups into a Unified Database

Step 1: Remove Foreign Key Constraint-To allow updates to the deliveryid column in both orders and delivers tables without violating referential integrity.

ALTER TABLE public.orders
DROP CONSTRAINT orders_deliveryid_fkey;

Step 2: Update deliveryid Values to Avoid Conflicts-To avoid duplicate primary/foreign key values between existing data and newly imported data. The offset (+605) ensures unique deliveryid values.

UPDATE public.orders
SET deliveryid = deliveryid + 605
WHERE deliveryid IS NOT NULL;

UPDATE public.delivers
SET deliveryid = deliveryid + 605;

 Step 3: Re-add the Foreign Key Constraint-To restore referential integrity after aligning the IDs.

ALTER TABLE public.orders
ADD CONSTRAINT orders_deliveryid_fkey
FOREIGN KEY (deliveryid)
REFERENCES public.delivers (deliveryid);

Step 4: Insert Workers from delivers – Default Values Version-
INSERT INTO public.worker (
    wfirstname, wlastname, wid, salary, havebonus, wseniority, wstatus
)
SELECT 
    couriername, '', deliveryid, 0, 0, 0, deliverystatus
FROM public.delivers
WHERE deliveryid NOT IN (SELECT wid FROM public.worker);

Step 5: Merge meal Data into dishes-To import meal data into the dishes table, while avoiding duplicates.
UPDATE public.dishes 
SET 
    mname = m.mname,
    mprice = m.mprice,
    dishname = m.mname,
    price = m.mprice::numeric(10,2)
FROM public.meal m
WHERE dishes.dishid = m.mid;
Step 6: Cleanup (Remove Temporary Columns)

ALTER TABLE public.dishes
DROP COLUMN mname,
DROP COLUMN mprice;

📜 [Integrate.sql](https://github.com/ChayaGayer/database/blob/master/Phase3/Integrate.sql)

### Views
View 1: dishes_with_orders
Description:
This view combines the dishes and orders tables using a NATURAL JOIN to show which dishes were ordered, their categories, and order-related data like date and total amount.
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
 ![image](https://github.com/user-attachments/assets/09ef4b5e-d026-479f-bdbe-fa5edceb38c7)

Query 1: High-value dish orders
SELECT *
FROM dishes_with_orders
WHERE totalamount > 200;
![image](https://github.com/user-attachments/assets/441629d7-543d-4557-9203-3c4842ff4c53)

Query 2: Number of orders per dish
SELECT dishid, dishname, COUNT(orderid) AS order_count
FROM dishes_with_orders
GROUP BY dishid, dishname;
![image](https://github.com/user-attachments/assets/8657d37e-d8e7-4677-bb2d-cf2680b71296)

View 2: worker_morning_shifts
Description:
This view uses a CROSS JOIN to match every worker with every shift, then filters to include only shifts starting before 12:00.
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

 ![image](https://github.com/user-attachments/assets/8dc95128-5801-4e41-bee4-8bec64325fdf)

Query 1: Morning shift count per worker
Counts how many shifts each worker is scheduled for that start before 12:00.
SELECT full_name, COUNT(shid) AS morning_shift_count
FROM worker_morning_shifts
GROUP BY full_name
ORDER BY morning_shift_count DESC;
![image](https://github.com/user-attachments/assets/3db38465-0e11-4ef9-9b60-b49b0903aad3)

Query 2: Workers who finish before 13:00
Returns names and shift times of workers whose shifts end before 13:00.
SELECT full_name, starttime, endtime
FROM worker_morning_shifts
WHERE endtime < '13:00'
ORDER BY endtime;
![image](https://github.com/user-attachments/assets/5f73de45-fee3-45c9-8912-b4731aaed84c)

📜 [Views.sql](https://github.com/ChayaGayer/database/blob/master/Phase3/Integrate.sql)



### Backup
[backup200525](https://github.com/ChayaGayer/database/blob/master/Phase3/backup200525)

# Phase D
### Functions
-total_salary_by_status
Description:
Calculates the total salary of workers with a specific status (e.g., 'Active').

Code:
CREATE OR REPLACE FUNCTION total_salary_by_status(p_status TEXT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC := 0;
BEGIN
    SELECT SUM(salary) INTO total
    FROM worker
    WHERE wstatus = p_status;
    RETURN total;
END;
$$ LANGUAGE plpgsql;

-count_worker_shifts
Description:
Returns the number of shifts a worker is scheduled for, based on their ID.

Code:
CREATE OR REPLACE FUNCTION count_worker_shifts(p_worker_id INT)
RETURNS INT AS $$
DECLARE
    shift_count INT;
BEGIN
    SELECT COUNT(*) INTO shift_count
    FROM scheduled
    WHERE wid = p_worker_id;
    RETURN shift_count;
END;
$$ LANGUAGE plpgsql;
### Procedures 
update_bonus_for_senior_workers
Description:
Updates the havebonus field to 1 for workers with seniority greater than 5.

Code:
CREATE OR REPLACE PROCEDURE update_bonus_for_senior_workers()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE worker
    SET havebonus = 1
    WHERE wseniority > 5;
END;
$$;


![image](https://github.com/user-attachments/assets/94474b62-4cee-4f04-b614-86ed444ba248)


-assign_worker_to_shift
Description:
Inserts a row into the scheduled table, assigning a worker to a shift on the current date.

Code:
CREATE OR REPLACE PROCEDURE assign_worker_to_shift(
    p_worker_id INT,
    p_shift_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO scheduled (sdate, wid, shid)
    VALUES (CURRENT_DATE, p_worker_id, p_shift_id);
END;
$$;



![image](https://github.com/user-attachments/assets/1f5b3148-713b-432f-9a3d-4dacb587d879)

### Triggers 
-log_salary_change
Description:
Logs any salary update into the worker_salary_log table.

Code:
CREATE OR REPLACE FUNCTION log_salary_change()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salary <> OLD.salary THEN
        INSERT INTO worker_salary_log(wid, old_salary, new_salary, change_date)
        VALUES (OLD.wid, OLD.salary, NEW.salary, CURRENT_DATE);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_salary_change
AFTER UPDATE ON worker
FOR EACH ROW
EXECUTE FUNCTION log_salary_change();


![image](https://github.com/user-attachments/assets/02a00842-810c-4b1f-8593-c301d905ee10)
![image](https://github.com/user-attachments/assets/8b6d7507-493a-425a-b97e-8b9a192417ab)




-validate_shift_times
Description:
Ensures that a shift’s endtime is after starttime.

Code:
CREATE OR REPLACE FUNCTION validate_shift_times()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.endtime <= NEW.starttime THEN
        RAISE EXCEPTION 'End time must be after start time';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_shift_time_check
BEFORE INSERT OR UPDATE ON shift
FOR EACH ROW
EXECUTE FUNCTION validate_shift_times();



![image](https://github.com/user-attachments/assets/00e23383-5fe8-4c44-89b3-a96dc5d203db)





### Main Program 
Description:
Calls the procedure to update bonuses and the function to sum salaries by status.

Code:

DO $$
DECLARE
    total NUMERIC;
BEGIN
    CALL update_bonus_for_senior_workers();
    total := total_salary_by_status('Active');
    RAISE NOTICE 'Total salary of active workers: %', total;
END;
$$;




![image](https://github.com/user-attachments/assets/eb2150ab-cee8-4b30-8e8f-3065ff72d790)



-2
Description:
Assigns a worker to a shift and prints the number of shifts they're scheduled for.

Code:
DO $$
DECLARE
    shift_num INT;
BEGIN
    CALL assign_worker_to_shift(1, 5000);
    shift_num := count_worker_shifts(1);
    RAISE NOTICE 'Worker 1 has % shifts', shift_num;
END;
$$;




![image](https://github.com/user-attachments/assets/8b898a4d-5566-4891-add7-6c1a0ae6bf4c)




### Backup
[90620252](https://github.com/Ch# Catering Management System 🍽️ 

## 🟢 Application Overview
This is a graphical database application for managing a **catering service**. It allows users to manage workers, customers, shift scheduling, and run queries and procedures using a user-friendly interface built with Python and Tkinter.

---

## 📁 Project Structure
This repository contains:

1. **gui_code/** – the full implementation of the graphical user interface.
2. **instructions.txt** – a step-by-step guide for installing and running the system.
3. **screenshots/** – screenshots of the system in action.
4. **README.md** – this project report and documentation.

---

## 🧭 How to Run the Application
### Requirements:
- Python 3.x installed
- PostgreSQL running with a database named `ITINEWDB`
- Python packages:
  - `psycopg2`
  - `Pillow` (for image support)

### Run:
From the `gui_code/` directory, run:
```bash
python main.py
ayaGayer/database/blob/master/phae4/90620252)




# Phase E















