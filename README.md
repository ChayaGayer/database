
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

## Phase 2: Integration
(To be completed in the next development phase)
**Queries**
1.This query shows each order with the customer name, delivery status, payment method, date, and total amount.
![cc991428-d541-4b66-a3a5-5cafbfad7ad8](https://github.com/user-attachments/assets/a8149817-e58c-4df6-a88c-e0af084b872e)
2.This query shows how many orders each customer made and how much they spent in total.
![b0f364bf-0a55-40f9-bc20-1091afd87a3b](https://github.com/user-attachments/assets/cbd65d25-e3e2-4cc4-b0af-d60eb19537e1)
3.This query shows the average review rating and number of reviews for each customer.
![618f6a8c-80c0-48a5-937b-d2712715b509](https://github.com/user-attachments/assets/45e33d78-6e0f-4077-9139-21178e22b031)
4.This query shows the 3 most frequently ordered dishes, based on the total amount ordered
![ed5e8821-61d7-443b-afcc-7b9c7299cb2c](https://github.com/user-attachments/assets/44775be2-75ee-41cc-8cf0-82491adcce0c)
5.This query shows all orders made in the last 30 days, including customer name, order date, and total amount.
![0fa94115-37eb-4e57-a2ae-58a338fef5b2](https://github.com/user-attachments/assets/ce7eba20-a819-4ce2-b3cf-65cd50f62bf2)
6.This query summarizes the number of orders and total revenue for each month, grouped by year and month.
![1fff6818-43bd-4614-b72c-931a94e85d1a](https://github.com/user-attachments/assets/3daec6b2-320d-4175-b041-20917430098b)
7.This query finds all dishes that were ordered with an average quantity greater than 2 units per order.
![14e1c756-39ba-4799-b148-58499201bef8](https://github.com/user-attachments/assets/3633b91a-3f3d-4ca8-b482-f8268a4af1dd)
8.This query finds customers who have never made an order (i.e., not connected to any order in the Orders table)
![216aacba-9b3c-4727-b4d6-bddf59c8d75c](https://github.com/user-attachments/assets/b7aa50f3-12b6-4435-a4b7-7a030c80a975)









