use empManagementdb;

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000001", "5f4dcc3b5aa765d61d8327deb882cf99", "adm", "Merlyn", "Bannister", "100000", "SysAdmin", "2022-10-01", "1980-01-02", "14", "13", "14", "14", "123 Sesame Street", "6472290000", "merban@company.com", "merban@personal.com", "555550333123456789001", "111111001");

INSERT INTO employee (employeeID, password, empType,fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000002", "5f4dcc3b5aa765d61d8327deb882cf99", "adm", "Aruna", "Can", "100000", "SysAdmin", "2022-10-01", "1980-01-03", "14", "13", "14", "12", "124 Sesame Street", "6472290001", "arucan@company.com", "arucan@personal.com", "555550333123456789002", "111111002");

INSERT INTO employee (employeeID, password, empType,fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000003", "5f4dcc3b5aa765d61d8327deb882cf99", "mng", "Nevada", "Cam", "1000000", "Owner", "2022-10-01", "1980-01-04", "14", "12", "14", "14", "125 Sesame Street", "6472290002", "nevcam@company.com", "nevcam@personal.com", "555550333123456789003", "111111003");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000004", "5f4dcc3b5aa765d61d8327deb882cf99", "mng",  "Lucero", "Pavlovsky", "120000", "Manager", "2022-10-01", "1980-01-05", "14", "11", "14", "14", "126 Sesame Street", "6472290003", "lucpav@company.com", "lucpav@personal.com", "555550333123456789004", "111111004");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000005", "5f4dcc3b5aa765d61d8327deb882cf99", "mng", "Lungile", "Roscoe", "140000", "Manager", "2022-10-01", "1980-01-06", "14", "14", "14", "13", "127 Sesame Street", "6472290004", "lunros@company.com", "lunros@personal.com", "555550333123456789005", "111111005");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000006", "5f4dcc3b5aa765d61d8327deb882cf99", "reg", "Munashi", "Barrett", "80000", "SWE1", "2022-10-01", "1980-01-07", "14", "14", "14", "14", "128 Sesame Street", "6472290005", "munbar@company.com", "munbar@personal.com", "555550333123456789006", "111111006");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000007", "5f4dcc3b5aa765d61d8327deb882cf99", "reg", "Puck", "Goretti", "150000", "Tech Lead", "2022-10-01", "1980-01-08", "14", "11", "14", "13", "129 Sesame Street", "6472290006", "pucgor@company.com", "pucgor@personal.com", "555550333123456789007", "111111007");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000008", "5f4dcc3b5aa765d61d8327deb882cf99", "reg", "Dwi", "Monette", "90000", "SWE2", "2022-10-01", "1980-01-09", "14", "13", "14", "12", "130 Sesame Street", "6472290007", "dwimon@company.com", "dwimon@personal.com", "555550333123456789008", "111111008");

INSERT INTO employee (employeeID, password, empType, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("000009", "5f4dcc3b5aa765d61d8327deb882cf99", "reg", "Shannon", "Aarts", "7500000", "SWE1", "2022-10-01", "1980-01-10", "14", "14", "14", "7", "131 Sesame Street", "6472290008", "shaaar@company.com", "shaaar@personal.com", "555550333123456789009", "111111009");

-- Owner
INSERT INTO empManaged (managerID, employeeID) VALUES ("000003", "000004");
INSERT INTO empManaged (managerID, employeeID) VALUES ("000003", "000005");

-- Manager 1
INSERT INTO empManaged (managerID, employeeID) VALUES ("000004", "000001");
INSERT INTO empManaged (managerID, employeeID) VALUES ("000004", "000006");
INSERT INTO empManaged (managerID, employeeID) VALUES ("000004", "000007");

-- Manager 2
INSERT INTO empManaged (managerID, employeeID) VALUES ("000005", "000002");
INSERT INTO empManaged (managerID, employeeID) VALUES ("000005", "000008");
INSERT INTO empManaged (managerID, employeeID) VALUES ("000005", "000009");

INSERT INTO team (teamID, teamManagerID, teamName) VALUES ("1101", "000004", "Dragon");
INSERT INTO team (teamID, teamManagerID, teamName) VALUES ("1102", "000005", "Phoenix");
INSERT INTO team (teamID, teamName) VALUES ("1103", "Unassigned");

UPDATE employee SET teamID="1101", managerID="000004" WHERE employeeID="000001";
UPDATE employee SET teamID="1102", managerID="000005" WHERE employeeID="000002";
UPDATE employee SET teamID="1101", managerID="000003" WHERE employeeID="000004";
UPDATE employee SET teamID="1102", managerID="000003" WHERE employeeID="000005";
UPDATE employee SET teamID="1101", managerID="000004" WHERE employeeID="000006";
UPDATE employee SET teamID="1101", managerID="000004" WHERE employeeID="000007";
UPDATE employee SET teamID="1101", managerID="000002" WHERE employeeID="000008";
UPDATE employee SET teamID="1101", managerID="000004" WHERE employeeID="000006";

INSERT INTO teamManaged (managerID, teamID) VALUES ("000003", "1103");
INSERT INTO teamManaged (managerID, teamID) VALUES ("000004", "1101");
INSERT INTO teamManaged (managerID, teamID) VALUES ("000003", "1102");

INSERT INTO teamMembers (teamID, employeeID) VALUES ("1101", "000004");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1101", "000001");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1101", "000006");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1101", "000007");

INSERT INTO teamMembers (teamID, employeeID) VALUES ("1102", "000005");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1102", "000002");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1102", "000008");
INSERT INTO teamMembers (teamID, employeeID) VALUES ("1102", "000009");

INSERT INTO project (projectID, projectName, currentTeamID, projectStatus) VALUES ("22220001", "MoneyMaker", "1101", "In Development");
INSERT INTO project (projectID, projectName, currentTeamID, projectStatus) VALUES ("22220002", "StonksUp", "1102", "In Testing");
INSERT INTO project (projectID, projectName, projectStatus) VALUES ("22220003", "Unnamed", "Not Started");

UPDATE team SET projectID="22220001" WHERE teamID="1101";
UPDATE team SET projectID="22220002" WHERE teamID="1102";

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "S", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000001", "W", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "S", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "V", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000002", "V", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "S", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "S", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000003", "W", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "S", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "S", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "S", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000004", "W", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "V", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000005", "W", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000006", "W", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "S", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "S", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "S", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000007", "V", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "V", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000008", "S", "8",  "2022-10-30");

INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-3");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-4");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-5");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-6");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-7");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-10");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-11");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-12");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-13");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-14");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-17");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "V", "8",  "2022-10-18");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-19");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-20");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-21");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-24");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-25");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-26");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-27");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-28");
INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES ("000009", "W", "8",  "2022-10-30");

INSERT INTO teamHoursWorked (teamID, projectID, hourAmount) VALUES ("1101", "22220001", "672");
INSERT INTO teamHoursWorked (teamID, projectID, hourAmount) VALUES ("1102", "22220002", "672");
