# Self_Repo
This README file provides instructions on how to build and run the Python Django project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Virtual environment tool such as `venv` or `virtualenv`

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/MohanNagaSaiGopi/Self_Repo.git
    cd Self_Repo
    ```

2. **Create and activate a virtual environment (recommended)**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations (Optional)**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access)**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the application**
    - Open your browser and go to: http://127.0.0.1:8000/ and access the application.


