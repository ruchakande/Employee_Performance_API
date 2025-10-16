# Employee_Performance_API
A RESTful API for managing employee data and analyzing performance metrics. This project allows you to store, retrieve, and analyze employee information such as performance scores, work hours, and department-wise productivity. Analytics endpoints use Pandas for aggregating and summarizing data in real-time.


# Employee Performance Analytics API

**Tech Stack:** Python, Flask, MySQL, REST API, Pandas  

A **RESTful API** for managing employee data and analyzing performance metrics. This project allows you to store, retrieve, and analyze employee information such as performance scores, work hours, and department-wise productivity. Analytics endpoints use **Pandas** for aggregating and summarizing data in real-time.  

---

## Features
- Add, list, and manage employee records via **REST API endpoints**.  
- Department-wise **performance summary** with average performance scores and total hours worked.  
- Optimized **MySQL queries and indexing** for faster data retrieval.  
- Analytics handled using **Pandas** to provide real-time insights.  

---

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/employees` | POST | Add a new employee |
| `/employees` | GET | List all employees |
| `/analytics/performance` | GET | Get department-wise performance summary |

---

## Setup Instructions

1. **Clone or download** the repository.  
2. **Create and activate a virtual environment**:  
   ```bash
   python -m venv venv
   venv\Scripts\activate         # Windows

3. Install dependencies:
   `pip install -r requirements.txt`

4. Set up the MySQL database:
   ```bash
   CREATE DATABASE employee_db;

   USE employee_db;

   CREATE TABLE employees (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      department VARCHAR(50),
      role VARCHAR(50),
      performance_score INT,
      hours_worked INT,
      date_joined DATE
   );

   CREATE INDEX idx_department ON employees(department);
   CREATE INDEX idx_performance_score ON employees(performance_score);
5. Update db.py with your MySQL credentials.
6. Run the API: `flask run`
7. Test endpoints using Postman, curl, or any API testing tool.

Project Structure:
Employee_Performance_API/
├── app.py           # Flask API entry point
├── db.py            # MySQL connection setup
├── analytics.py     # Pandas-based analytics functions
├── requirements.txt # Python dependencies
