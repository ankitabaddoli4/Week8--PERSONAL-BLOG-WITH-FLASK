# Week8--PERSONAL-BLOG-WITH-FLASK
A full-featured personal blog web application built with Flask, featuring user authentication, blog post management, commenting system, and responsive design.

##  Project Overview
This project is a full-featured **Personal Blog Web Application** developed using the Flask framework in Python. It allows users to register, log in securely, create and manage blog posts, and interact through comments.

The application demonstrates complete **full-stack web development**, including backend logic, database integration, authentication, and responsive frontend design.

---

## Objectives
- Build a dynamic blog website using Flask  
- Implement secure user authentication system  
- Perform CRUD operations on blog posts  
- Enable user interaction through comments  
- Design a responsive and user-friendly interface  

---

##  Features
- User Registration and Login  
- Secure Authentication (Password Hashing)  
- Create, Read, Update, Delete (CRUD) Blog Posts  
- Comment System  
- Search Functionality  
- Pagination for posts  
- Responsive design using Bootstrap  
- Image upload support  
- Contact form  

---

##  Technologies Used

### Backend
- Python  
- Flask  

### Frontend
- HTML  
- CSS  
- Bootstrap  

### Database
- SQLite  
- SQLAlchemy ORM  

### Libraries
- Flask-SQLAlchemy  
- Flask-WTF  
- Flask-Login  
- Flask-Migrate  
- Werkzeug  

---

##  Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/flask-blog.git
cd flask-blog
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Initialize Database
flask db init
flask db migrate
flask db upgrade
Step 4: Run the Application
python run.py
Step 5: Open in Browser
http://localhost:5000

Project Structure
flask-blog/
│── app/
│   ├── __init__.py
│   ├── models.py
│   ├── extensions.py
│   │
│   ├── auth/
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── main/
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── templates/
│   ├── static/
│
│── migrations/
│── config.py
│── run.py
│── requirements.txt

## Technical Details
Architecture
Follows MVC (Model-View-Controller) pattern
Uses Flask Blueprints for modular structure
Database Design
User table → stores user details
Post table → stores blog posts
Comment table → stores comments
Core Functionalities
Password hashing using Werkzeug
Form validation using Flask-WTF
Session management using Flask-Login
Search using database queries
Pagination using Flask-SQLAlchemy
Security Features
Password encryption
CSRF protection
Secure session handling

## Screenshots
Home Page
Login Page
Registration Page
Create Post Page
Blog View
Comment Section
Search Results

## Testing
Test Cases
Login with valid credentials → Success
Login with invalid credentials → Error
Create post → Success
Edit post → Updated successfully
Delete post → Removed successfully
Add comment → Displayed correctly
Search → Relevant results shown
Validation
Form validation implemented
Error handling included
Secure data handling ensured

## Learning Outcomes
Flask web development
Database integration using SQLAlchemy
User authentication and security
Responsive UI design using Bootstrap
Structuring scalable web applications

## Future Enhancements
User profile page
Like and share functionality
Dark mode UI
REST API integration
Deployment on cloud platforms
