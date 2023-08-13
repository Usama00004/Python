--Create DB
CREATE DATABASE my_db;

--Drop DB
DROP DATABASE my_db;

--Backing up DataBase 
BACKUP DATABASE my_db 
TO DISK = 'filepath'
WITH DIFFERENTIAL;


--Create Table
CREATE TABLE my_table
(
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
 
); 
--Create Table From Existing Table 
CREATE TABLE new_table AS 
 SELECT col_1,col_2
 FROM existing_table
 Where condition 

--Drop table
 DROP TABLE table_name

 --ALter table add column
ALTER TABLE my_table
ADD PhoneNumber varchar(255);

 --ALter table drop column
 ALTER TABLE my_table
 DROP COLUMN City

 --To Change the datatype of existing column
ALTER TABLE table_name
MODIFY COLUMN Column_name datatype;

--To ADD Constraint to existing column
ALTER TABLE table_name
MODIFY COLUMN Column_name datate CONSTRAINT;

--Adding Constrainst while table Creation
CREATE TABLE my_table
(
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    CONSTRAINT constraint_name constraint_type (Col1,col2) 
 
); 

--ALTERING tabe and adding Constraint 
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE(ID,LastName);

--ALTERING tabe and adding Constraint 
ALTER TABLE Persons
DROP CONSTRAINT UC_Person;

CONSTRAINT PK_PERSON PRIMARY KEY(ID,LastName)

ADD CONSTRAINT FK_PersonOrder
FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);


ADD CONSTRAINT Fk_PersonOrder Foreign Key (PersonID) REFERENCES Persons(PersonID)

ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';



CREATE INDEX index_name
ON table_name (column1, column2, ...);


CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);


CREATE TABLE Persons (
    Personid int IDENTITY(1,1) PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

IDENTITY(1,1)
IDENTITY(10,2)

