
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
[90620252](https://github.com/ChayaGayer/database/blob/master/phae4/90620252)




# Phase E
## 🟢 Application Overview
#Catering Management System 🍽️
This is a graphical database application for managing a **catering service**. It allows users to manage workers, customers, shift scheduling, and run queries and procedures using a user-friendly interface built with Python and Tkinter.

Application Deployment Instructions
1. Application Setup
Requirements:

Python 3.x installed

PostgreSQL installed, with a database named: ITINEWDB

Required Python packages:

psycopg2

Pillow (for image support)

2. Running the Application
To run the graphical application:

Navigate to the gui_code/ directory in the terminal.

Execute the following command:

bash
Copy
Edit
python main.py
Ensure that the database server is running and that the relevant tables, procedures, and functions exist in the ITINEWDB database.

🧩 Tools and Technologies
The following tools and technologies were used in the development of this application:

Python 3.x – core programming language

Tkinter – Python's standard GUI library

PostgreSQL – the database system used

pgAdmin – database management interface

psycopg2 – PostgreSQL adapter for Python

Pillow – for loading and displaying images in the GUI

Visual Studio Code – primary development environment

Application Screenshots
Main Menu – Welcome Screen
This is the main entry screen of the catering management system. It features a clean, user-friendly interface with a welcoming message and five primary navigation buttons:

Manage Workers – Opens the interface for managing worker records.

Manage Customers – Opens the interface for managing customer data.

Assign Worker to Shift – Opens the interface for linking workers to scheduled shifts.

Queries and Procedures – Opens the screen for executing predefined SQL queries and stored procedures.

Exit – Closes the application.

This screen provides easy access to all core features of the system.

![image](https://github.com/user-attachments/assets/13625c93-de28-4eef-80e4-649dbc2cb3ce)

Worker Management Screen
This screen provides a comprehensive interface for managing worker records in the catering system. Users can:

View all workers in a structured table showing ID, name, salary, seniority, status, and bonus.

Add a new worker by entering their details in the text fields above and clicking "הוסף עובד" ("Add Worker").

Update an existing worker by selecting a row, editing the details, and clicking "עדכן עובד" ("Update Worker").

Delete a worker using the "מחק עובד" ("Delete Worker") button.

Refresh the table to reflect the latest changes using the "רענן" ("Refresh") button.

The screen is designed with a clean, pink background and user-friendly layout, allowing efficient management of employee data.


![image](https://github.com/user-attachments/assets/2924c6b7-5a91-43b1-9457-0782a98ae5e6)

Worker Update Confirmation
This screenshot demonstrates the update functionality in the Worker Management screen. After selecting an existing worker, editing their details, and clicking the "עדכן עובד" ("Update Worker") button:

A confirmation dialog appears with the message "Worker updated successfully."

This ensures users receive immediate feedback about the success of the operation.

The success dialog improves user experience by validating the action, confirming the backend database was updated accordingly.


![image](https://github.com/user-attachments/assets/397be2e9-b6ef-43a7-9a22-2dde5a7a30d1)


Worker Addition Confirmation
This screenshot illustrates the successful addition of a new worker in the Worker Management screen. After filling in all required fields (ID, first name, last name, salary, seniority, status, and bonus) and clicking the "הוסף עובד" ("Add Worker") button:

A confirmation message appears: "Worker added successfully."

This ensures the new worker’s data has been saved to the database and the user receives immediate positive feedback.

The interface supports real-time validation and updates to the table view upon worker addition.

![image](https://github.com/user-attachments/assets/c167dee4-7dee-4de4-9478-ce209e7cb850)

Worker Deletion Confirmation
This screenshot demonstrates the process of deleting a worker from the Worker Management screen. After selecting an existing worker's ID and clicking the "מחק עובד" ("Delete Worker") button:

A confirmation message appears: "Worker deleted successfully."

This indicates that the worker’s record has been permanently removed from the system database.

The data table refreshes to reflect the change, ensuring real-time feedback and data accuracy for the user.

![image](https://github.com/user-attachments/assets/947768ab-ecc8-4ea6-ad7c-4f0d6cf31c9b)


Customer Management Screen
This screen allows users to manage customer information within the catering management system. It is accessed via the main entry screen by clicking the "ניהול לקוחות" ("Manage Customers") button.

Key functionalities include:

View: Displays a table of all customers, including their ID, name, phone number, email address, and physical address.

Add Customer: Using the "הוסף לקוח" ("Add Customer") button, users can register new customers by filling in the fields at the top.

Update Customer: Select an existing customer, edit their details in the input fields, and click "עדכן לקוח" ("Update Customer") to apply the changes.

Delete Customer: Removes a customer from the system via the "מחק לקוח" ("Delete Customer") button.

Refresh: Updates the table to reflect the most current data from the database.

This module ensures that client information is easily accessible, editable, and consistently synchronized with the underlying PostgreSQL database.

![image](https://github.com/user-attachments/assets/23da7539-d7a5-4d25-a6f7-615d8563b983)

Customer Added Confirmation

This screenshot demonstrates the successful addition of a new customer to the catering management system.

Key features shown:

A new customer (ID: 455) has been added with full details including name, phone number, email, and address.

Upon clicking the "הוסף לקוח" ("Add Customer") button, a confirmation popup is displayed:
"✔ Customer added successfully."

The newly added customer immediately appears in the customer list below, indicating real-time synchronization with the PostgreSQL database.

This feedback mechanism ensures users receive immediate confirmation of successful actions, enhancing the system’s usability and reliability.

![image](https://github.com/user-attachments/assets/35bfe171-66d5-47b4-a365-5615f9cf62b7)

Customer Update Confirmation

This screenshot captures the process of updating an existing customer's details within the customer management screen.

Highlights:

The customer with ID 455 is being updated, with changes reflected in fields such as phone number, email, or address.

Once the "עדכן לקוח" ("Update Customer") button is clicked, a confirmation message appears:
"✔ Customer updated successfully."

The confirmation dialog ensures the user receives immediate feedback about the success of the operation, improving transparency and user confidence.

The updated information is instantly visible in the data table, confirming that the system is functioning correctly and connected to the live database.
![image](https://github.com/user-attachments/assets/e5c8e5c0-33fc-499a-8456-b65f6cfceb9c)

Customer Deletion Confirmation

This screenshot displays the successful deletion of a customer record from the customer management screen.

Details:

The record of Customer455, previously visible in the form fields and table, has been removed.

A confirmation dialog appears stating:
"🗑 Customer deleted successfully."

This ensures the user receives immediate visual feedback that the deletion was processed by the system.

The deletion is also reflected in the table view, which refreshes automatically to show the updated list of customers. This reinforces data integrity and ease of use.

![image](https://github.com/user-attachments/assets/3d70ee8f-575c-4441-a32f-27ed4baba047)

Shift Count Query Screen

This screen allows users to check how many shifts a specific worker is assigned to.

Features:

The screen is accessed from the main interface using the button labeled "📊 שאילתות ופרוצדורות".

Users enter a worker_id in the input field.

By clicking the "בדוק כמות משמרות" button, the system retrieves the number of scheduled shifts for the given worker, using a pre-defined SQL function.

The interface is styled with a light pink background and bold, centered headers for clarity and visual consistency with the rest of the system.

![image](https://github.com/user-attachments/assets/d12b7dba-b4ac-4132-9d52-b308a0571dff)

Shift Count Check – Result Display

This screenshot shows the result of querying the number of shifts assigned to a specific worker.

The user entered worker_id = 111.

Upon clicking the "Check Shifts" button, a confirmation dialog appears.

The dialog message displays:
"Worker number 111 has 2 shifts."

This functionality is part of the system's procedures screen and reflects real-time data retrieved from the database using a backend SQL function.

![image](https://github.com/user-attachments/assets/48bb94bf-447d-4736-a6ed-aa4d8f5fead2)

Queries & Functions Screen
This window is accessed via the "Queries and Procedures" button on the main menu screen.
It allows the user to execute predefined SQL queries and stored procedures in the catering management system.

Functionalities included:

Total Orders per Customer: Displays the total number of orders placed by each customer.

Total Salary by Status: After entering a worker status (e.g., "Active", "Inactive"), this query returns the total salary of all workers matching that status.

Assign Worker to Shift: By entering a valid worker ID and shift ID, this function assigns the selected worker to the specified shift using a stored procedure.

This interface provides a direct way to interact with complex backend logic (queries and procedures), in a user-friendly form.

![image](https://github.com/user-attachments/assets/1dc73403-f7ab-467b-8b95-8100b0156a08)


Total Orders per Customer – Result Window

Upon clicking the "Total Orders per Customer" button, the system executes a predefined SQL query that aggregates the number of orders and total spending for each customer.

The result is displayed in a message window in the following format:
Customer<ID> | Orders: <count> | Total: <sum>

Customer41 | Orders: 5 | Total: 953.77
Customer306 | Orders: 4 | Total: 898.53
...
This functionality is useful for summarizing customer engagement and identifying top-spending clients in the system.

![image](https://github.com/user-attachments/assets/773da017-d25c-46a0-bb51-50294ae08e4a)


Count Workers by Status – Result Window
Upon clicking the "Count Workers by Status" button, the system executes an SQL query that groups all employees in the database by their wstatus field and counts the number of employees in each status category.

The result is displayed in a message window in the following format:

php-template
Copy
Edit
Status: <StatusName> | Count: <NumberOfWorkers>
For example:

yaml
Copy
Edit
Status: Active | Count: 460  
Status: Not Active | Count: 351  
Status: Completed | Count: 294  
Status: temp | Count: 144  
Status: Vacation | Count: 44  
Status: Status3 | Count: 40  
Status: Status2 | Count: 38  
Status: Status1 | Count: 28
This functionality is useful for HR and management to quickly assess the distribution of employee statuses across the organization, enabling better workforce planning and status-based analysis.


![image](https://github.com/user-attachments/assets/a233fc8f-b4e4-4e36-bf0b-0fc0d215f8aa)


Total Salary by Status – Result Window
Upon clicking the "Total Salary by Status" button (after entering a valid status, e.g. "Active"), the system calculates the sum of all salaries for workers with that specific status.

The result is shown in a message box in the following format:

lua
Copy
Edit
Total salary for status '<Status>': <TotalSum>
For example:

Total salary for status 'Active': 4823794.09
This feature provides a quick financial overview of salary expenses filtered by worker status (e.g. Active, Inactive, etc.).
![image](https://github.com/user-attachments/assets/f4786caf-75d9-44d4-b9aa-49a5989b3694)


 Assign Worker to Shift
This feature allows administrators to assign a worker to a specific shift using a stored procedure.

How it works:

The user inputs:

Worker ID — an existing worker's ID from the database.

Shift ID — an existing shift ID from the shift table.

Upon clicking Assign Worker to Shift, the system executes the stored procedure assign_worker_to_shift(worker_id, shift_id).

Behavior:

✅ On success, a confirmation message is displayed (e.g., "Worker 111 assigned to shift 5000.").

❌ If the shift ID does not exist in the shift table, an error message is shown due to the foreign key constraint in the scheduled table.

Purpose:
This function streamlines the scheduling process by programmatically linking workers to shifts based on business logic defined in the database.

![image](https://github.com/user-attachments/assets/1aeca3b5-34dc-42d8-992e-a36300a75281)

### Exit the System

At the bottom of the interface, the **"יציאה מהמערכת" (Exit the System)** button is displayed.

#### Behavior:
🡆 Clicking this button immediately closes the current window and exits the application.

#### Purpose:
This feature allows users to safely and quickly log out or exit the system once they have completed their tasks.



![image](https://github.com/user-attachments/assets/7be59d32-7d3d-44e4-8139-46742f44b279)


