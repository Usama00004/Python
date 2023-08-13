SELECT TRIM('     SQL Tutorial!     ') AS Trimmed_String; --Remove characters and spaces from a string:
SELECT LTRIM ('     SQL Tutorial!')  AS Left_Trimmed_String;
SELECT RTRIM ('SQL Tutorial!     ')  AS Right_Trimmed_String;
SELECT UPPER(CustomerName) AS UppercaseCustomerName FROM Customers;
SELECT SUBSTRING('SQL Tutorial', 1, 3) AS ExtractString;
SELECT CAST(25.65 AS int);