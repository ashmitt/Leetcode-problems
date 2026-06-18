# Write your MySQL query statement below
SELECT D.NAME as Department, E.NAME AS Employee, E.SALARY as Salary 
FROM EMPLOYEE E join DEPARTMENT D 
on E.departmentid=D.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
      AND e2.salary > e.salary
) < 3;

