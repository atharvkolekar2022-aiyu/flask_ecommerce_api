# Flask eCommerce API

A RESTful API built with Flask for managing an eCommerce platform. This project provides endpoints for product management, shopping cart operations, and order processing with an integrated frontend.

## Features

- **Product Management** - Get, create, update, and delete products
- **Shopping Cart** - Add/remove items from cart
- **Order Processing** - Place and manage orders
- **API Documentation** - Interactive Swagger UI with Flasgger
- **CORS Support** - Cross-origin requests enabled
- **SQLite Database** - Lightweight data persistence

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **API Documentation**: Flasgger (Swagger UI)
- **Frontend**: HTML/JavaScript (templates)

## Project Structure

```
ecommerce_api/
├── app.py              # Application entry point and factory
├── db.py               # Database initialization and models
├── routes.py           # API route definitions
├── service.py          # Business logic and service layer
├── requirements.txt    # Python dependencies
├── ecommerce.db        # SQLite database file
└── templates/
    └── index.html      # Frontend HTML
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/atharvkolekar2022-aiyu/flask_ecommerce_api.git
   cd flask_ecommerce_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### API Documentation

View the interactive Swagger UI at: `http://localhost:5000/apidocs`

## API Endpoints

### Products
- `GET /api/products` - Get all products
- `POST /api/products` - Create a new product
- `PUT /api/products/<id>` - Update a product
- `DELETE /api/products/<id>` - Delete a product

### Frontend
- `GET /` - Serve the main frontend page

## Configuration

The application runs in debug mode by default. Modify `app.py` to change:
- Debug mode (`debug=True/False`)
- Port (default: 5000)
- Host (default: localhost)

## CORS Support

The API includes CORS headers allowing requests from any origin. Headers include:
- `Access-Control-Allow-Origin: *`
- `Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS`
- `Access-Control-Allow-Headers: Content-Type, Authorization`

## Database

SQLite database is automatically initialized on first run. The database file (`ecommerce.db`) stores all application data.

## License

MIT License

## Author

Atharv Kolekar
