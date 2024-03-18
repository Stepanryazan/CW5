from classes.db_manager import DBManager
from utils import create_database, create_tables, insert_data_into_tables


def user_interaction():

    list_employers = [1942330, 49357, 78638, 2748, 3529, 9498112, 93787326, 2180, 1648566, 1942336]
    dbm = DBManager('db_name')
    create_database('db_name')
    create_tables('db_name')
    insert_data_into_tables(list_employers)

    print(" Привет!\n"
          " Выберите команду:\n"
          " 1 - Список всех компаний и количесво их вакансий\n 2 - Список всех вакансий с информацией по каждой\n 3 - "
          "Узнать среднюю зарплату \n 4 - Списсок вакансий, у которых зарплата выше средней\n 5 - Поискать по ключевому "
          "слову\n")

    while True:
        user_input = input()
        if user_input in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Попробуйте еще раз")

    if user_input == '1':
        print(dbm.get_companies_and_vacancies_count())
    elif user_input == '2':
        print(dbm.get_all_vacancies())
    elif user_input == '3':
        print(dbm.get_avg_salary())
    elif user_input == '4':
        print(dbm.get_vacancies_with_higher_salary())
    elif user_input == '5':
        keyword = str(input('Найти: '))
        print(dbm.get_vacancies_with_keyword(keyword))


if __name__ == '__main__':
    while True:
        user_interaction()
        user_choice = input("Продолжить? (да/нет): ")
        if user_choice.lower() != "да":
            break