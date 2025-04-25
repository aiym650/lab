import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="250675", 
    host="localhost",
    port="5432"
)

def search_phonebook(pattern):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
        return cur.fetchall()

def insert_or_update_user(first_name, phone):
    with conn.cursor() as cur:
        cur.execute("CALL insert_or_update_user(%s, %s)", (first_name, phone))
        conn.commit()

def insert_multiple_users(user_list):
    with conn.cursor() as cur:
        cur.execute("CALL insert_multiple_users(%s)", (user_list,))
        conn.commit()

def get_phonebook_page(limit, offset):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
        return cur.fetchall()

def delete_user(input_text):
    with conn.cursor() as cur:
        cur.execute("CALL delete_user(%s)", (input_text,))
        conn.commit()

# Негізгі функция
def main():
    while True:
        print("\nМеню:")
        print("1. Жаңа пайдаланушы қосу немесе телефонды жаңарту")
        print("2. Көптеген пайдаланушыларды қосу")
        print("3. Деректерді үлгі бойынша іздеу")
        print("4. Беттеу арқылы деректерді сұрау")
        print("5. Деректерді жою")
        print("6. Шығу")
        choice = input("Сіз қай опцияны таңдайсыз? ")

        if choice == '1':
            first_name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update_user(first_name, phone)
        elif choice == '2':
            user_list = input("Пайдаланушылар тізімін енгізіңіз (мысалы: Айжан,87011234567): ").split(';')
            insert_multiple_users(user_list)
        elif choice == '3':
            pattern = input("Үлгі бойынша іздеу (атауы немесе телефон нөмірі): ")
            results = search_phonebook(pattern)
            for row in results:
                print(row)
        elif choice == '4':
            limit = int(input("Шектеу саны (limit): "))
            offset = int(input("Бастапқы орын (offset): "))
            results = get_phonebook_page(limit, offset)
            for row in results:
                print(row)
        elif choice == '5':
            input_text = input("Пайдаланушы аты немесе телефон нөмірі бойынша деректерді жою: ")
            delete_user(input_text)
        elif choice == '6':
            break
        else:
            print("Неверный ввод!")

    conn.close()

if __name__ == "__main__":
    main()
