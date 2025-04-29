
select * from emp;
select * from dept;
select empno,ename,job,hiredate,sal,dname,loc from emp Join dept on emp.deptno=dept.deptno;

select empno,ename,job,hiredate,sal,
(select dname from dept where deptno=emp.deptno) as dname,
(select loc from dept where deptno=emp.deptno) as loc
from emp;

use mydb;
select * from dept
where ename like '%A%';

select * from emp
where ename like '%'||'A'||'%';

select * from emp
where ename like concat('%','A','%');