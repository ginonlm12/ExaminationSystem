# Online Exam System

This is a fully functional Online Exam System built using **Python**, **Django**, **MySQL**, and **Bootstrap**. It allows students to register, take exams, and automatically calculate scores. Faculties can manage courses and questions, while admins can manage all aspects of the system.

## Features

### Admin Features
- **Login**: Admin users can log in to manage the system.
- **Dashboard**: Provides an overview of uploaded images and general system status.
- **Manage Courses**:
  - Add new courses.
  - List all courses.
  - Delete courses.
- **Manage Questions**:
  - Add new questions.
  - List all questions.
  - Delete questions.
- **Manage Teachers**:
  - List all teachers.
  - Validate new teacher accounts.
  - Update teacher details.
  - Delete teacher accounts.
  - List teacher salaries.
- **Manage Students**:
  - List all students.
  - Update student details.
  - Delete student accounts.
  - List student salaries.

### Faculty Features
- **Login and Registration**: Faculties can log in to manage courses and questions.
- **Dashboard**: Displays uploaded images and general data.
- **Manage Courses**:
  - Add new courses.
  - List all courses.
  - Delete courses.
- **Manage Questions**:
  - Add new questions.
  - List all questions.
  - Delete questions.
  
### Student Features
- **Login and Registration**: Students can register and log in to take exams.
- **Dashboard**: Displays uploaded images and basic information.
- **List Examination**: Students can view all available exams.
- **Take Exams**: Students can select one answer per question, review their answers, and submit.
- **View Exam Results**: Students can view their results after submitting the exam.

## Screenshots

Here are some screenshots of the Online Exam System interface:

### Admin Dashboard
![Admin Dashboard](static\app_interface\AdminDashboard.png)

### Homepage 
![Homepage ](static/app_interface/student_dashboard.png)

## Tech Stack

- **Python**
- **Django** - Web framework
- **SQLite3** - Database
- **HTML**, **CSS**, **JavaScript**, **jQuery**, **Ajax**
- **Pillow** - For image processing
- **asgiref** - For asynchronous support
- **Django-widget-tweaks** - For form customization
- **pytz** - For timezone management
- **FontAwesome** - For icons
- **Bootstrap** - For responsive design

## How to Run

### Prerequisites

Ensure you have the following installed on your system:
- **Python**: Download and install Python 3.x from the official website.
- **PIP**: Python package manager for installing dependencies.

### Setup/Installation

1. **Download the Source Code**:
   - Download or clone this repository to your local machine.

2. **Install Dependencies**:
   - Open a terminal (Command Prompt or shell) and navigate to the project directory where the source code is stored. Run the following command to install the necessary packages:
   
     ```bash
     pip install -r requirements.txt
     ```

3. **Run Migrations**:
   - Run the following command to apply all database migrations:

     ```bash
     python manage.py migrate
     ```

4. **Create a Superuser**:
   - To access the admin panel, create a superuser account with the following command:
   
     ```bash
     python manage.py createsuperuser
     ```

   - Follow the prompts to create an admin user.

5. **Run the Development Server**:
   - Start the development server with:

     ```bash
     python manage.py runserver
     ```

6. **Access the Application**:
   - Open a web browser and navigate to:
   
     ```
     http://127.0.0.1:8000/ or http://localhost:8000/
     ```

7. **Admin Panel Access**:
   - To access the Django admin panel, visit:

     ```
     http://127.0.0.1:8000/admin/
     ```

   - Log in with the admin credentials you created earlier.

## Troubleshooting

If you encounter any issues during setup, consider the following troubleshooting tips:

1. **Module Installation Errors**:
   - Ensure that `pip` is installed and using the correct version of Python.
   - If you encounter errors during the `pip install -r requirements.txt` step, try upgrading `pip` by running:
     ```bash
     pip install --upgrade pip
     ```

2. **Database Issues**:
   - If you encounter database-related issues, try running the migrations again with:
     ```bash
     python manage.py migrate
     ```

3. **Missing Static Files**:
   - If static files (images, CSS) are not loading properly, run the following command to collect them:
     ```bash
     python manage.py collectstatic
     ```

4. **Server Not Running**:
   - If the server is not running or you encounter a port issue, try running it on a different port:
     ```bash
     python manage.py runserver 8080
     ```

## License

This project is licensed under the MIT License.

## Acknowledgements

- **Django**: Used as the web framework for building this project.
- **Bootstrap**: For responsive UI design.
- **FontAwesome**: For icons used throughout the application.
- **Pillow**: For handling image uploads and processing.
- **jQuery** and **Ajax**: For dynamic and interactive user interface features.

---

Feel free to fork this repository, contribute, and help improve the project.
