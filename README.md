# DRF Simple API

This is a simple Django Rest Framework (DRF) project that exposes a single endpoint returning an email, the current datetime, and a GitHub repository URL.

## Prerequisites

Ensure you have Python installed on your machine. This project requires Python 3.x.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Clemcy9/hng-week0-api.git
   cd your-repo
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Server

1. Apply migrations:
   ```sh
   python manage.py migrate
   ```

2. Start the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoint

### GET `https://memorys.pythonanywhere.com/api/user-details/`

#### Response Format:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Dependencies

The project uses the following dependencies as listed in `requirements.txt`:

```
asgiref==3.8.1
Django==5.1.5
django-rest-framework==0.1.0
djangorestframework==3.15.2
sqlparse==0.5.3
typing_extensions==4.12.2
```

## License

This project is licensed under the MIT License.

## Author

[clement Idemudo](https://github.com/Clemcy9)


## HNG

[hng_python](https://hng.tech/hire/python-developers)


