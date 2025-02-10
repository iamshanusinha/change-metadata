# Change Metadata Flask Project

This is a Flask-based project for managing metadata, designed for deployment on Render.com. It allows you to modify and manage metadata entries via API endpoints and integrates a basic frontend to visualize the changes.

## Project Structure

The project structure is as follows:
changemetadata/
│
├── changemetadata/
│   ├── init.py
│   ├── metadata_views.py
│   └── templates/
│       ├── index.html
│       └── other_templates.html
│
├── config.py
├── run.py
└── requirements.txt
- `run.py`: Entry point for starting the Flask app.
- `config.py`: Configuration file for environment variables and settings.
- `changemetadata/`: Package that contains the business logic and views.
- `changemetadata/templates/`: Frontend HTML files.
- `requirements.txt`: List of dependencies for the project.

## Requirements

Before running the project locally or deploying it to Render, make sure you have the following installed:

- Python 3.8+ (Python 3.8 or later is recommended)
- Pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/changemetadata.git
   cd changemetadata
   python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
To run the app locally, use the following command:
python run.py
