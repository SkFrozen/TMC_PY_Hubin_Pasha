-- SQLite
-- CREATE TABLE Employees (
-- Name varchar(50),
-- Position varchar(50),
-- Department varchar(50),
-- Salary decimal(10, 2)
-- );

-- INSERT INTO Employees VALUES ("Luchi", "worker", "repair", 1000),
--                              ("Pippo", "worker", "repair", 1000),
--                              ("Lerdo", "foreman", "repair", 1600),
--                              ("Municci", "foreman", "repair", 1600),
--                              ("Pablo", "engineer", "repair", 1800.99),
--                              ("Lula", "bookkeeper", "bookkeeping", 1500.45),
--                              ("Mikki", "manager", "management", 1250.55),
--                              ("Petra", "manager", "management", 1250.55),
--                              ("Paul", "director", "management", 5500);

-- UPDATE Employees SET Position="foreman" WHERE Name="Pippo";

-- ALTER TABLE Employees ADD COLUMN HireDate date;

-- UPDATE Employees SET HireDate="2018-09-03" WHERE Name="Luchi";
-- UPDATE Employees SET HireDate="2020-03-25" WHERE Name="Petra";
-- UPDATE Employees SET HireDate="2019-06-14" WHERE Name="Mikki";
-- UPDATE Employees SET HireDate="2019-12-09" WHERE Name="Pippo";
-- UPDATE Employees SET HireDate="2018-01-29" WHERE Name="Pablo";
-- UPDATE Employees SET HireDate="2018-11-23" WHERE Name="Lula";
-- UPDATE Employees SET HireDate="2019-09-11" WHERE Name="Municci";
-- UPDATE Employees SET HireDate="2017-11-05" WHERE Name="Paul";
-- UPDATE Employees SET HireDate="2021-08-16" WHERE Name="Lerdo";

-- SELECT * FROM Employees WHERE Position="manager";

-- SELECT * FROM Employees WHERE Salary > 5000;

-- SELECT * FROM Employees WHERE Department="repair";

-- SELECT AVG(Salary) FROM Employees;

-- DROP TABLE Employees;