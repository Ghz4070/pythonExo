def init(connection):
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matiere (
        id          INTEGER AUTOINCREMENT PRIMARY KEY NOT NULL,
        name   TEXT    NOT NULL
    ) 
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cursus (
        id          INTEGER AUTOINCREMENT PRIMARY KEY NOT NULL,
        name   TEXT    NOT NULL
    ) 
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS etudiant (
        id          INTEGER AUTOINCREMENT PRIMARY KEY NOT NULL,
        firstname   TEXT    NOT NULL,
        lastname TEXT NOT NULL,
        age INTEGER NOT NULL
    ) 
    ''')
