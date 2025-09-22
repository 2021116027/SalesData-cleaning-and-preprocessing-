# SalesData-cleaning-and-preprocessing-
Data cleaning using python pandas 
# Retail Store Sales Data Cleaning

## Overview
This project involves cleaning and preprocessing a retail store sales dataset to make it ready for analysis. The dataset contains transaction details including items, quantities, prices, discounts, payment methods, and store locations. The cleaning process handles missing values, duplicates, inconsistent text formatting, and invalid data.

---

## Dataset
- **File name:** `retail_store_sales.csv`
- **Columns:**
  - `Transaction_Date` – Date of transaction
  - `Category` – Item category
  - `Item` – Name of the item sold
  - `Price_Per_Unit` – Price of one unit of the item
  - `Quantity` – Number of units sold
  - `Total_Spent` – Total amount spent
  - `Payment_Method` – Method of payment (Cash, Card, etc.)
  - `Discount_Applied` – Whether discount was applied (True/False)
  - `Location` – Store location

---

## Features of Data Cleaning

1. **Column Standardization**
   - Converted all column names to title case and replaced spaces with underscores.

2. **Handling Missing Values**
   - Numeric columns (`Price_Per_Unit`, `Quantity`, `Total_Spent`) filled with mean values.
   - Categorical columns (`Item`, `Payment_Method`) filled with `'Unknown'`.
   - `Discount_Applied` filled with `False` if missing.

3. **Date Conversion**
   - Converted `Transaction_Date` to datetime format.
   - Removed rows with invalid dates.

4. **Duplicate Removal**
   - All duplicate rows removed.

5. **Text Standardization**
   - Converted text columns to proper case (title case) and removed extra spaces.

6. **Boolean Conversion**
   - `Discount_Applied` converted to boolean type.

7. **Index Reset**
   - Reset index after all cleaning steps.

---

