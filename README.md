# E-Learning School Project - Courses and Classes Management API (Completed)

## Introduction

The "E-Learning School" project was an API designed for the management of courses and classes in an e-learning school. The application followed the Entity Relationship Diagram (ERD) provided as a guideline.

![Entity Relationship Diagram (ERD)](https://imgur.com/blEuWtp.png)

## General Rules

- The language used was Python, along with the Django framework and Django Rest Framework.
- PostgreSQL was used as the database for developing the API.
- Documentation was available in Swagger.
- Deployment was completed, and all routes were functional in the production environment, which was done using services like Render.
- Generic Views and Model Serializer from DRF were used throughout the application. No routes were left with APIView or basic DRF Serializer.
- Authentication was implemented using Json Web Token (JWT).
- The relationship between "Account" and "Course" entities was 1:N, with the "instructor" attribute in "Course" and the "courses" attribute in "Account" configured with the related_name "courses."
- The relationship between "Course" and "Content" entities was 1:N, with the "course" attribute in "Content" and the related_name "contents."
- The relationship between "Account" and "Course" entities was N:N, using a custom pivot table.
- The location to configure the N:N relationship was at the developer's discretion, but it was possible to access the "students" key in "Course" and the "my_courses" key in "Account."
- The foreign key referring to "Account" in the pivot table was named "student," with the related_name "students_courses."
- The foreign key referring to "Course" in the pivot table was named "course," with the related_name "students_courses."

## Routes

### Account

- POST `/api/accounts/`: Created new user accounts.
- GET `/api/accounts/`: Listed all user accounts.
- GET `/api/accounts/<int:account_id>/`: Searched for user accounts by ID.
- PATCH `/api/accounts/<int:account_id>/`: Updated user account information.
- DELETE `/api/accounts/<int:account_id>/`: Deleted user accounts by ID.

### Course

- POST `/api/courses/`: Created new courses.
- GET `/api/courses/`: Listed all courses.
- GET `/api/courses/<int:course_id>/`: Searched for courses by ID.
- PATCH `/api/courses/<int:course_id>/`: Updated course information.
- DELETE `/api/courses/<int:course_id>/`: Deleted courses by ID.

### Content

- POST `/api/contents/`: Created new content for courses.
- GET `/api/contents/`: Listed all content.
- GET `/api/contents/<int:content_id>/`: Searched for content by ID.
- PATCH `/api/contents/<int:content_id>/`: Updated content information.
- DELETE `/api/contents/<int:content_id>/`: Deleted content by ID.

### Students-Courses Relationship

- POST `/api/students-courses/`: Created new student-course relationships.
- GET `/api/students-courses/`: Listed all student-course relationships.
- DELETE `/api/students-courses/<int:relation_id>/`: Deleted student-course relationships by ID.

## Project Configuration

The "E-Learning School" project followed best development practices with Django and Django Rest Framework. Configuration details were available in the source code.
