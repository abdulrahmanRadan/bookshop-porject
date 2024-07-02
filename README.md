# Bookshop Project

## Introduction
This project is a bookshop management application developed using the Django framework. It provides an interface to add, edit, and delete books, as well as manage the details of the available books in the library.

## About Django
Django is a high-level web framework for Python that encourages rapid development and clean, pragmatic design. Known for its "don't repeat yourself" (DRY) principle, Django includes numerous built-in features like user management, forms, database administration, and a templating system, which help developers build web applications quickly and efficiently.

## Requirements
To download and run this project, you need to have the following requirements installed:
- Python 3.7 or higher
- Django 3.2 or higher
- pip for package installation
- SQLite database (included with Django)

## How to Download the Project
1. Clone this repository to your local machine:
    ```bash
    git clone https://git@github.com:abdalrahmanRadan/bookshop-porject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd bookshop-project
    ```

## How to Run the Project
1. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    ```
2. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```
3. git code:
   - Show branch:
       ```bash
       git branch -r
       ```
   - Create a local branch that tracks master from the remote:
       ```bash
       git checkout -b master origin/master
       ```
   - Or if the master branch already exists locally, you can simply navigate to it:
       ```bash
       git checkout master
       ```
   - Update 'master' branch:
       ```bash
       git pull origin master
       ```

4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
5. Migrate the database:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```
7. Open your web browser and navigate to the following address to access the application:
    ```
    http://127.0.0.1:8000/
    ```

## About Me
My name is Abdalrahman Radan. I am a passionate software developer specializing in web application development using Django. I have extensive experience in designing and developing software solutions that meet clients' needs and exceed their expectations.

---

If you have any questions or need further assistance, feel free to reach out to me.
