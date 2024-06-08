from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('exam.sqlite3')
    cursor = conn.cursor()

    # Get the list of table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]

    # Close the database connection
    conn.close()

    # Pass the list of table names to the template
    return render_template('index.html', tables=table_names)


@app.route('/table/<table_name>')
def display_table(table_name):
    # Redirect to a new HTML page to display the contents of the selected table
    return redirect(url_for('show_table', table_name=table_name))


@app.route('/report/<table_name>')
def display_report(table_name):
    # Logic to display the report goes here
    return render_template('report.html', table_name=table_name)


@app.route('/show_table/<table_name>')
def show_table(table_name):
    # Connect to the database
    conn = sqlite3.connect('exam.sqlite3')
    cursor = conn.cursor()

    # Fetch data from the selected table
    cursor.execute(f'SELECT * FROM {table_name}')
    data = cursor.fetchall()

    # number of subject
    number_of_subject = int((len(data[0]) - 7) / 6)

    # Close the database connection
    conn.close()

    # Function to determine if an index should be excluded
    def should_exclude(index):
        if index in [2, 4]:
            return True
        if index >= 10:
            return (index - 10) % 6 == 0 or (index - 11) % 6 == 0 or (index - 12) % 6 == 0
        return False

    # Exclude specific elements from each row
    modified_data = []
    for row in data:
        modified_row = [element for index, element in enumerate(row) if not should_exclude(index)]
        modified_data.append(modified_row)

    # Include subject name
    subject_names = []
    for i in range(number_of_subject):
        subject_names.append(data[0][12+i*6])

    # Pass the fetched data to the HTML template for rendering
    return render_template('table.html', table_name=table_name, data=modified_data, number_of_subject=number_of_subject, subject_names=subject_names)


if __name__ == '__main__':
    app.run(debug=True)
