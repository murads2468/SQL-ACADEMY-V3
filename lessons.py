TOPICS = [{'id': 0, 'title': 'Introduction to SQL', 'level': 'Beginner'}, {'id': 1, 'title': 'Database Basics', 'level': 'Beginner'}, {'id': 2, 'title': 'CREATE DATABASE and CREATE TABLE', 'level': 'Beginner'}, {'id': 3, 'title': 'INSERT', 'level': 'Beginner'}, {'id': 4, 'title': 'SELECT', 'level': 'Beginner'}, {'id': 5, 'title': 'WHERE', 'level': 'Beginner'}, {'id': 6, 'title': 'AND, OR, NOT', 'level': 'Beginner'}, {'id': 7, 'title': 'ORDER BY', 'level': 'Beginner'}, {'id': 8, 'title': 'DISTINCT', 'level': 'Beginner'}, {'id': 9, 'title': 'LIMIT', 'level': 'Beginner'}, {'id': 10, 'title': 'UPDATE', 'level': 'Beginner'}, {'id': 11, 'title': 'DELETE', 'level': 'Beginner'}, {'id': 12, 'title': 'Aggregate Functions', 'level': 'Beginner'}, {'id': 13, 'title': 'GROUP BY', 'level': 'Intermediate'}, {'id': 14, 'title': 'HAVING', 'level': 'Intermediate'}, {'id': 15, 'title': 'SQL Joins', 'level': 'Intermediate'}, {'id': 16, 'title': 'INNER JOIN', 'level': 'Intermediate'}, {'id': 17, 'title': 'LEFT JOIN', 'level': 'Intermediate'}, {'id': 18, 'title': 'RIGHT JOIN concepts', 'level': 'Intermediate'}, {'id': 19, 'title': 'FULL OUTER JOIN concepts', 'level': 'Intermediate'}, {'id': 20, 'title': 'UNION and UNION ALL', 'level': 'Intermediate'}, {'id': 21, 'title': 'Subqueries', 'level': 'Intermediate'}, {'id': 22, 'title': 'Nested Queries', 'level': 'Intermediate'}, {'id': 23, 'title': 'CASE WHEN', 'level': 'Intermediate'}, {'id': 24, 'title': 'Constraints', 'level': 'Intermediate'}, {'id': 25, 'title': 'Primary Key and Foreign Key', 'level': 'Intermediate'}, {'id': 26, 'title': 'Indexes', 'level': 'Intermediate'}, {'id': 27, 'title': 'Views', 'level': 'Intermediate'}, {'id': 28, 'title': 'SQL Functions', 'level': 'Intermediate'}, {'id': 29, 'title': 'Date and Time Functions', 'level': 'Intermediate'}, {'id': 30, 'title': 'String Functions', 'level': 'Intermediate'}, {'id': 31, 'title': 'CTEs', 'level': 'Advanced'}, {'id': 32, 'title': 'Window Functions', 'level': 'Advanced'}, {'id': 33, 'title': 'ROW_NUMBER', 'level': 'Advanced'}, {'id': 34, 'title': 'RANK and DENSE_RANK', 'level': 'Advanced'}, {'id': 35, 'title': 'Stored Procedures concepts', 'level': 'Advanced'}, {'id': 36, 'title': 'Transactions', 'level': 'Advanced'}, {'id': 37, 'title': 'Normalization', 'level': 'Advanced'}, {'id': 38, 'title': 'Database Design', 'level': 'Advanced'}, {'id': 39, 'title': 'SQL Interview Questions', 'level': 'Advanced'}, {'id': 40, 'title': 'Real-world SQL Projects', 'level': 'Advanced'}]

BASE = [
("All employees","SELECT id, name, salary FROM employees;"),
("Karachi employees","SELECT name FROM employees WHERE city = 'Karachi';"),
("Salary descending","SELECT name, salary FROM employees ORDER BY salary DESC;"),
("Department counts","SELECT department_id, COUNT(*) AS total FROM employees GROUP BY department_id;"),
("Average salary","SELECT AVG(salary) AS average_salary FROM employees;"),
("Join department names","SELECT e.name, d.name AS department FROM employees e JOIN departments d ON e.department_id=d.id;"),
("Employees above average","SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"),
("Salary bands","SELECT name, CASE WHEN salary >= 90000 THEN 'High' ELSE 'Standard' END AS band FROM employees;"),
("Customer orders","SELECT c.name, o.amount FROM customers c JOIN orders o ON c.id=o.customer_id;"),
("Top two salaries","SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2;")
]
EXAMPLES=[]
for topic in TOPICS:
    title=topic["title"]
    items=[]
    for n,(name,query) in enumerate(BASE,1):
        # safe SQL editor execution is only enabled for read-only queries; other lesson topics remain syntax demonstrations.
        explanation=f"{title} ko practical dataset par apply karne ka example. Query ko samajh kar values aur columns change karein."
        items.append({"title":f"{n}. {name}","sql":query,"roman":explanation,"english":f"Example {n} demonstrates {title.lower()} using the academy sample tables.","runnable":query.lstrip().upper().startswith("SELECT")})
    EXAMPLES.append(items)
