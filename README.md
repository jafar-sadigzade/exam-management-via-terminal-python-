# Exam Management System

This project is an exam management system that processes student exam results, reads from input files, and stores the results in a SQLite database. It handles specific requirements such as custom character replacements and processes student answers against correct answers stored in a file.

## Project Structure
### in the core directory:

- `test.py`: Main script to run the exam processing and store results in the database.
- `db.py`: Script to manage database operations (creating tables, adding columns, inserting data).
- `csvtodict.py`: Script to read exam form configurations from a CSV file and convert them to dictionaries.
- `cavablar_dirnaq_list.py`: Script to read correct answers from a file and provide functionality to retrieve correct answers.

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
