import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="250675", 
    host="localhost",
    port="5432"
)

def create_table():
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                phone VARCHAR(15) NOT NULL UNIQUE
            );
        """)
        conn.commit()

def insert_from_console():
    with conn.cursor() as cur:
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        try:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
            print("Данные добавлены!")
        except Exception as e:
            conn.rollback()
            print(f"Ошибка: {e}")

def insert_from_csv(filename):
    with conn.cursor() as cur:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
                except Exception as e:
                    print(f"Ошибка при добавлении {row}: {e}")
                    conn.rollback()
        conn.commit()
        print("Данные из CSV загружены!")

def update_data():
    with conn.cursor() as cur:
        field = input("Что изменить? (имя/телефон): ").lower()
        if field == 'имя':
            old = input("Старое имя: ")
            new = input("Новое имя: ")
            cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new, old))
        elif field == 'телефон':
            old = input("Старый номер: ")
            new = input("Новый номер: ")
            cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new, old))
        conn.commit()
        print("Обновление выполнено!")

def query_data():
    with conn.cursor() as cur:
        filter_type = input("Фильтр по (имя/телефон): ").lower()
        if filter_type == 'имя':
            name = input("Введите имя: ")
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
        else:
            phone = input("Введите телефон: ")
            cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))
        rows = cur.fetchall()
        for row in rows:
            print(row)

def delete_record():
    with conn.cursor() as cur:
        by = input("Удалить по (имя/телефон): ").lower()
        if by == 'имя':
            name = input("Введите имя: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        else:
            phone = input("Введите телефон: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        print("Удаление выполнено!")

def main():
    create_table()
    while True:
        print("\nМеню:")
        print("1. Добавить из консоли")
        print("2. Загрузить из CSV")
        print("3. Обновить данные")
        print("4. Найти данные")
        print("5. Удалить запись")
        print("6. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            insert_from_csv("data.csv")
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print("Неверный ввод!")

    conn.close()

if __name__ == '__main__':
    main()
