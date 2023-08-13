--General Structure of Trigger

/*CREATE TRIGGER trigger_name ON table_name 
{BEFORE|AFTER|INSTEAD OF} {INSERT|UPDATE|DELETE}
AS BEGIN 
 DECLARE @va1 varchar(20);
 DECLARE @va2 varchar(20);
 SELECT @var1 = name_1 FROM INSERTED|UPDATED|DELETED
 IF @var1 = 'Usama'
  THROW 51000, 'The record does not exist.', 1; 
 ELSE ---  
 */



-- Trigger ON INSERT
CREATE TRIGGER t_country_insert ON country INSTEAD OF INSERT
AS BEGIN
    DECLARE @country_name CHAR(128);
    DECLARE @country_name_eng CHAR(128);
    DECLARE @country_code  CHAR(8);
    SELECT @country_name = country_name, @country_name_eng = country_name_eng, @country_code = country_code FROM INSERTED;
    IF @country_name IS NULL SET @country_name = @country_name_eng;
    IF @country_name_eng IS NULL SET @country_name_eng = @country_name;
    INSERT INTO country (country_name, country_name_eng, country_code) VALUES (@country_name, @country_name_eng, @country_code);
END;

-- Trigger ON DELETE
DROP TRIGGER IF EXISTS t_country_delete;
GO
CREATE TRIGGER t_country_delete ON country INSTEAD OF DELETE
AS BEGIN
    DECLARE @id INT;
    DECLARE @count INT;
    SELECT @id = id FROM DELETED;
    SELECT @count = COUNT(*) FROM city WHERE country_id = @id;
    IF @count = 0
        DELETE FROM country WHERE id = @id;
    ELSE
        THROW 51000, 'can not delete - country is referenced in other tables', 1;
END;