BEGIN TRANSACTION;

/* Create a table called NAMES */
CREATE TABLE quills(Id text, Name text, COM text);

/* Create few records in this table */
INSERT INTO quills VALUES('A','1','Tom');
INSERT INTO quills VALUES('B','2','Lucy');
INSERT INTO quills VALUES('C','3','Frank');
INSERT INTO quills VALUES('D','4','Jane');
INSERT INTO quills VALUES('E','5','Robert');
COMMIT;

/* Display all the records from the table */
--SELECT sql FROM sqlite_master WHERE type='table'
--SELECT * FROM quills;
select 1,sql FROM sqlite_master WHERE type=char(116) || char(97) || char(98) || char(108) || char(101) union select 1,url from quills limit 100 offset 0
select flag from flagtable union select url from quills limit 100 offset 0
