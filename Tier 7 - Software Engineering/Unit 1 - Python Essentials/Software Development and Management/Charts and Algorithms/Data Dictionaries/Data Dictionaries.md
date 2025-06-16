# **Data Dictionaries**

Databases are used to store structured data in computer systems. Relational Databases are the most common type for structured data storage.

A database organises data in tables with rows (records) and columns (attributes).

## **Data Dictionary**
A data dictionary provides a comprehensive description of each variable stored or referred to in a system. This commonly includes variable name, data type, format, size in bytes, number of characters to display the item including number of decimal places (if applicable), the purpose of each variable and a relevant example. Any validation rules applicable to the data item can also be included.

**Data Dictionary from Course Specifications**

![Data Dictionary](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Data%20Dictionaries/Images/datadictexample.avif)

**⚠️ The above data dictionary is in the <u> expected format and is examinable. </u>**

## **Database Schema**
To create a Relational Database, a data schema is required. A data schema is a blueprint or framework that outlines how data is organised in a database.

It defines the structure of the database in terms of the tables, columns, relationships, and constraints that make up the database. It acts as a guide for how data is stored, accessed, and managed within the database system.

### **Components**
- **Tables:** Represent entities (like customers, products, orders) in the database. Each table is a collection of related data entries.
- **Columns:** Define the attributes or properties of the entity. For instance, a 'Customer' table might include columns like CustomerID, Name, Address, etc.
- **Data Types:** Each column in a table is associated with a specific data type (like integer, text, date), which defines the nature of the data that can be stored in the column.
- **Primary Keys:** Unique identifiers for each record in a table. They help to ensure that each record can be uniquely identified.
- **Foreign Keys:** Establish relationships between tables, linking each record in one table to one or more records in another.
- **Constraints:** Rules applied to table columns to enforce data integrity, such as NOT NULL, UNIQUE, CHECK, etc.

**Data Schema for a Relational Database**

![Data Schema](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Data%20Dictionaries/Images/dataschemaexample.avif
)

## **Example of Database Tables**
The following is an example of database tables. 

- Each **ROW** is a **RECORD**
- Each **COLUMN** represents a **FIELD.** 
    - Data Dictionaries provide a description of each field, including data types and validation.
- A **RECORD (ROW)** is made up of many **FIELDS (COLUMNS).**

**Database Tables**

![Example](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Data%20Dictionaries/Images/databaseetableexample.avif)

**Database Schema**

![Schema](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Software%20Development%20and%20Management/Charts%20and%20Algorithms/Data%20Dictionaries/Images/schemaexample2.avif)