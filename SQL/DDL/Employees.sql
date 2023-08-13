Create Table Employees
(
EmployeeID Int Not Null Primary key,	
LastName Varchar(255),	
FirstName Varchar(255),	
BirthDate Varchar(255), 	
Photo Varchar(255),	
Notes Varchar(255)

)


Insert Into Employees(EmployeeID,LastName,FirstName,BirthDate,Photo,Notes)
Values
(1,'Davolio','Nancy','1968-12-08','EmpID1.pic','Education includes a BA in psychology from Colorado State University.'),
(2,'Fuller','Andrew','1952-02-19','EmpID2.pic','Andrew received his BTS commercial  He is fluent in French and Italian and reads German'),
(3,'Leverling','Janet','1963-08-30','EmpID3.pic','Janet has a BS degree in chemistry from Boston College. '),
(4,'Peacock','Margaret','1958-09-19','EmpID4.pic','Margaret holds a BA in English literature from Concordia College '),
(5,'Buchanan','Steven','1955-03-04','EmpID5.pic','Steven Buchanan graduated from St. Andrews University, Scotland,'),
(6,'Suyama','Michael','1963-07-02','EmpID6.pic','Michael is a graduate of Sussex University MA, economics and the University of California '),
(7,'King','Robert','1960-05-29','EmpID7.pic','Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan'),
(8,'Callahan','Laura','1958-01-09','EmpID8.pic','Laura received a BA in psychology from the University of Washington. She has also completed a course in business French. She reads and writes French.'),
(9,'Dodsworth','Anne','1969-07-02','EmpID9.pic','Anne has a BA degree in English from St. Lawrence College. She is fluent in French and German.'),
(10,'West','Adam','1928-09-19','EmpID10.pic','An old chum.');
