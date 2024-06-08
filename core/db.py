import sqlite3


def db_first():
    try:
        global cursor, conn, tbname
        dbname = 'istedad_sinaq.db'  # SQLite database file
        tbname = input('Cədvəl adını daxil edin: ')
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {tbname}")
        sql = f'''CREATE TABLE {tbname}(
            ad TEXT,
            soyad TEXT,
            is_no TEXT,
            ata_adi TEXT,
            cins TEXT,
            sinif TEXT,
            cem REAL
        )'''
        cursor.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def db_second(x):
    try:
        required_columns = [
            f"fenn_{x}_duz",
            f"fenn_{x}_sehv",
            f"fenn{x}_bal",
            f"fenn{x}",
            f"dzgn_cvb_f{x}",
            f"fennad{x}"
        ]

        cursor.execute(f"PRAGMA table_info({tbname})")
        existing_columns = [column[1] for column in cursor.fetchall()]

        for column in required_columns:
            if column not in existing_columns:
                if column.endswith('_bal'):
                    cursor.execute(f"ALTER TABLE {tbname} ADD COLUMN {column} REAL")
                else:
                    cursor.execute(f"ALTER TABLE {tbname} ADD COLUMN {column} TEXT")

        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def db_third(ad, soyad, is_no, ata_adi, cins, sinif, cem, fennduzdeyisenler, fennsehvdeyisenler, fenncembaldeyisenler, fenncavabdeyisenler, duzguncavabdeyisenler, fennaddeyisenler):
    try:
        columns = ['ad', 'soyad', 'is_no', 'ata_adi', 'cins', 'sinif', 'cem']
        placeholders = ['?', '?', '?', '?', '?', '?', '?']
        values = [ad, soyad, is_no, ata_adi, cins, sinif, cem]

        for data in [fennduzdeyisenler, fennsehvdeyisenler, fenncembaldeyisenler, fenncavabdeyisenler, duzguncavabdeyisenler, fennaddeyisenler]:
            columns.extend(data.keys())
            placeholders.extend(['?'] * len(data))
            values.extend(data.values())

        columns_str = ', '.join(columns)
        placeholders_str = ', '.join(placeholders)

        insert_data = f"INSERT INTO {tbname} ({columns_str}) VALUES ({placeholders_str})"
        cursor.execute(insert_data, values)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
