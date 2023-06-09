# Django API Data Saving Project

This Django project demonstrates how to fetch data from an API and save it into a database using Django models.

## Prerequisites

- Python (version 3.6 or higher)
- Django (version 4.x or higher)
- Requests library (to make API requests)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/sbstnzcr/chileregistros-challenge.git
   ```

2. Navigate to the project directory:

   ```
   cd chileregistros-challenge
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

   - On Windows:

     ```
     venv\Scripts\activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run the migrations:

   ```
   python manage.py migrate
   ```

7. Create a superuser:

   ```
   python manage.py createsuperuser
   ```

   Follow the prompts to enter a username, email (optional), and password for the superuser.


## Configuration

1. Open the `config/settings.py` file and set your own database connection variables.

## Usage

1. Run the python scripts:

   ```
   python scipt_bikerio.py
   python script_snifa.py
   ```

2. Start the Django development server:

   ```
   python manage.py runserver
   ```

3. Open your web browser and navigate to `http://localhost:8000/admin` to access the django web admin interface.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
