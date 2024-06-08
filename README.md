# Exam Management System

This project is an exam management system that processes student exam results, reads from input files, and stores the results in a SQLite database. It handles specific requirements such as custom character replacements and processes student answers against correct answers stored in a file.

## Project Structure
- `core/`: Contains the core logic of the application.
  - `cavablar_dirnaq_list.py`: Script to read correct answers from a file.
  - `csvtodict.py`: Script to read exam form configurations from a CSV file.
  - `db.py`: Script to manage database operations (creating tables, adding columns, inserting data).
  - `server.py`: Flask server script to fetch data from the database and render HTML templates.
  - `test.py`: Main script to run the exam processing and store results in the database.
- `templates/`: Contains HTML templates used by Flask to render web pages.
  - `index.html`: Displays the list of tables in the database.
  - `table.html`: Displays the content of a selected table.
  - `report.html`: (Currently empty) Placeholder for future report generation.
- `txt/`: Contains text files or input data files.
  - `answer.txt`: File containing correct answers.
  - `result.txt`: File containing student results.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: This file, providing an overview of the project.
- `exam.sqlite3`: SQLite database file containing exam data.
- `examform.csv`: CSV file containing exam form data.
- `requirements.txt`: Lists Python packages required for the project.
- `venv/`: Directory containing the Python virtual environment.

## Installation

### Prerequisites

- Python 3.x
- Virtual environment (recommended)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jafar-sadigzade/exam-management-via-terminal-python-.git
    cd exam-management-via-terminal-python-
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt  # If you have a requirements.txt file with dependencies
    ```

## Usage

### Step-by-Step Guide

1. **Prepare Input Files**:
    - Ensure you have the student results file (e.g., `result.txt`).
    - Ensure you have the correct answers file (e.g., `answer.txt`).
    - Ensure you have the exam forms configuration CSV file (e.g., `examform.csv`).

2. **Run the `test.py` script**:
    ```bash
    python core/test.py
    ```

3. **Follow the prompts**:
    - Enter the name of the correct answers file.
    - Enter the name of the student results file.
    - Select the exam form configuration by entering its name.
    - Enter the name for the database table to store the results.


3. **Follow the prompts**:
    - Enter the name of the correct answers file.
    - Enter the name of the student results file.
    - Select the exam form configuration by entering its name.
    - Enter the name for the database table to store the results.


4. **Run the Flask server**:
    ```bash
    python core/server.py
    ```

5. **Access the web interface**:
    - Open your web browser and go to `http://127.0.0.1:5000/`.

6. **Navigate the interface**:
    - The homepage lists all tables in the database.
    - Click on a table name to see options to view the table or generate a report.
    - Use the buttons to toggle columns in the table view.



## HTML Templates

- `index.html`: Lists all tables in the database and provides options to view each table or generate a report.
- `table.html`: Displays the contents of a selected table, with show/hide functionality for specific columns.
- `report.html`: Placeholder for future report generation functionality.


### Example Usage

1. **Run the script**:
    ```bash
    python test.py
    ```

2. **Input Prompts**:
    ```
    Cavablar olan faylın adını yazın: cavab1.txt
    şagird nəticələri olan txt faylın adını yazın: 8-5.txt
    sinaq1
    sinaq2
    sinaq3
    sinaq4
    sinaq5
    sinaq6
    sinaq7
    Sınaq formasını daxil edin: sinaq7
    Cədvəl adını daxil edin: test
    ```

3. **Results**:
    - The results will be processed and stored in the specified SQLite database table.

## Scripts Description

### `test.py`

- **Description**: Main script to process student results and store them in the database.
- **Functionality**:
    - Reads input files.
    - Replaces specific characters.
    - Initializes variables and configurations.
    - Processes student answers and calculates scores.
    - Stores results in the SQLite database.

### `db.py`

- **Description**: Manages database operations.
- **Functions**:
    - `db_first()`: Creates the main table for storing results.
    - `db_second(x)`: Adds necessary columns to the table.
    - `db_third(...)`: Inserts processed student results into the table.

### `csvtodict.py`

- **Description**: Reads exam form configurations from a CSV file.
- **Functionality**: Converts CSV data to a list of dictionaries for easy access.

### `cavablar_dirnaq_list.py`

- **Description**: Reads correct answers from a file.
- **Functionality**: Provides a function to retrieve correct answers based on coordinates.
