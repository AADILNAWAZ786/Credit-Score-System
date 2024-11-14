# Credit-Score-System
# Quiz Application

This is a simple quiz application built using Django. The app fetches questions from an API endpoint, displays them to the user, and calculates a credit score based on the user's answers. The result is shown in a modal popup using Bootstrap.

## Features

- **Fetch Questions**: Questions are fetched dynamically from an API endpoint.
- **Session Management**: The quiz progress is managed using Django session.
- **Credit Score Calculation**: Based on user responses, a credit score is calculated and displayed.
- **Responsive UI**: Built with Bootstrap for a responsive and modern user interface.
- **Modal Popup for Result**: Displays the result in a Bootstrap modal popup.

## Installation

### Prerequisites

- Python 3.x
- Django
- Bootstrap (via CDN)
- XAMPP

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>

2. Set up a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   source venv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. XAMPP setting :
   - Open XAMPP Control Panel
   - Start Apache and MySql   

5. Apply Migrations:
   ```bash
   python manage.py migrate

6. Run the Development Server:
   ```bash
   python manage.py runserver

7. Access the Application: Open your browser and go to http://127.0.0.1:8000/.

## Technologies Used
- Django: A Python web framework for building the backend.
- Bootstrap: Frontend framework used to style the application and create modals.
- Python: The primary language for backend logic and calculations.
- SQLite: Database for storing session data (default for Django).

## Usage
- Upon starting the app, users will see the quiz page with questions fetched from the API.
- The user selects answers, and upon submission, a credit score is calculated based on the responses.
- The score is displayed in a Bootstrap modal, and the user can either close the modal or navigate back to the homepage.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Bootstrap for the UI components.
- Django for the powerful web framework.
```bash

### Key Sections:

- **Project Overview**: Brief explanation of what the app does.
- **Features**: A list of key features.
- **Installation**: Instructions to get the app running locally.
- **Project Structure**: An outline of the project's directory structure.
- **Technologies Used**: A list of frameworks and tools used in the project.
- **Usage**: Instructions on how the app works from a user's perspective.
- **License**: Mention of the project's licensing.
- **Acknowledgements**: Credits for technologies used.

This format provides clarity on how to install, use, and contribute to the project.

   

