from datetime import datetime
import json
import csv

class ManageNotes:
    def __init__(self):
        print("\nУправление заметками")
        print(' 1. Создание новой заметки.\n 2. Просмотр списка заметок.\n 3. Просмотр подробностей заметки.\n 4. Редактирование заметки.\n 5. Удаление заметки.\n 6. Импорт и экспорт заметок в формате CSV.')
        self.action = int(input('Выберите действие: '))
        if self.action == 1:
            self.create_note()
        elif self.action == 2:
            self.list_notes()
        elif self.action == 3:
            self.view_note()
        elif self.action == 4:
            self.edit_note()
        elif self.action == 5:
            self.delete_note()
        elif self.action == 6:
            self.import_export_notes()

    def create_note(self):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        self.id = len(notes) + 1
        self.title = input('Введите заголовок заметки: ')
        self.content = input('Введите содержимое заметки: ')
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_note = {'id': self.id, 'title': self.title, 'content': self.content, 'timestamp': self.timestamp}
        notes.append(new_note)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)
        print(f'Заметка {self.id} создана успешно!')

    def list_notes(self):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        for note in notes:
            print(f'{note["id"]}. {note["title"]} - {note["timestamp"]}')

    def view_note(self):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        self.note_id = int(input('Введите id заметки: '))
        note = next((note for note in notes if note['id'] == self.note_id), None)
        if note:
            print(f'Заметка {note["id"]}: {note["title"]}\n{note["content"]}\n{note["timestamp"]}')
        else:
            print('Заметка с таким id не найдена.')

    def edit_note(self):
        self.note_id = int(input('Введите id заметки: '))
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        note = next((note for note in notes if note['id'] == self.note_id), None)
        if note:
            note['title'] = input('Введите новый заголовок заметки: ')
            note['content'] = input('Введите новое содержимое заметки: ')
            with open('notes.json', 'w') as file:
                json.dump(notes, file, indent=4)
            print(f'Заметка {self.note_id} изменена успешно!')
        else:
            print('Заметка с таким id не найдена.')

    def delete_note(self):
        self.note_id = int(input('Введите id заметки: '))
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        note = next((note for note in notes if note['id'] == self.note_id), None)
        if note:
            notes.remove(note)
            with open('notes.json', 'w') as file:
                json.dump(notes, file, indent=4)
            print(f'Заметка {self.note_id} удалена успешно!')
        else:
            print('Заметка с таким id не найдена.')

    def import_export_notes(self):
        print('Импорт и экспорт заметок')
        print('1. Импорт заметок из CSV.\n2. Экспорт заметок в CSV.')
        self.import_export_action = int(input('Выберите действие: '))
        if self.import_export_action == 1:
            self.import_notes_from_csv()
        elif self.import_export_action == 2:
            self.export_notes_to_csv()

    def import_notes_from_csv(self):
        self.import_notes = []
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.import_id = row[0]
                self.import_title = row[1]
                self.import_content = row[2]
                self.import_timestamp = row[3]
                self.import_note = {'id': self.import_id, 'title': self.import_title, 'content': self.import_content, 'timestamp': self.import_timestamp}
                self.import_notes.append(self.import_note)
        with open('notes.json', 'w') as file:
            json.dump(self.import_notes, file, indent=4)
        print('Заметки импортированы из CSV успешно!')
                

    def export_notes_to_csv(self):
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for note in notes:
                writer.writerow([note['id'], note['title'], note['content'], note['timestamp']])
            print('Заметки экспортированы в CSV успешно!')

class ManageTasks:
    def __init__(self):
        print("\nУправление задачами")
        print('1. Создание новой задачи.\n2. Просмотр списка задач.\n3. Отметка задачи как выполненной.\n4. Редактирование задачи.\n5. Удаление задачи.\n6. Импорт и экспорт задач в формате CSV.')
        self.action = int(input('Выберите действие: '))
        if self.action == 1:
            self.create_task()
        elif self.action == 2:
            self.list_tasks()
        elif self.action == 3:
            self.status_task()
        elif self.action == 4:
            self.edit_task()
        elif self.action == 5:
            self.delete_task()
        elif self.action == 6:
            self.import_export_tasks()

    def create_task(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = [] #если файла нет, то создаем пустой список

        self.task_id = len(self.tasks) + 1
        self.task_title = input('Введите заголовок задачи: ')
        self.task_description = input('Введите описание задачи: ')
        self.task_status = (input('Введите статус задачи (1 - выполнено, 0 - не выполнено): '), False)
        if self.task_status == 1:
            self.task_status = True
        else:
            self.task_status = False
        self.priority = int(input('Введите приоритет задачи (1 - низкий, 2 - средний, 3 - высокий): '))
        if self.priority == 1:
            self.priority = 'Низкий'
        elif self.priority == 2:
            self.priority = 'Средний'
        else:
            self.priority = 'Высокий'

        self.due_date = int(input('Введите срок выполнения задачи (дней): '))
        self.due_date = datetime.now() + datetime.timedelta(int(self.due_date))
        self.due_date = self.due_date.strftime('%Y-%m-%d')

        self.task = {'id': self.task_id, 'title': self.task_title, 'description': self.task_description, 'status': self.task_status, 'priority': self.priority, 'due_date': self.due_date}
        self.tasks.append(self.task)
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)
        print(f'Задача {self.task_id} создана успешно!')
    
    def list_tasks(self):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)
        for task in self.tasks:
            if task['status'] == True:
                self.task_status = 'Выполнено'
            elif task['status'] == False:
                self.task_status = 'Не выполнено'
            print(f'{task["id"]}. {task["title"]} - Статус: {self.task_status} - Приоритет: {task["priority"]} - Срок выполнения: {task["due_date"]}')

    def status_task(self):
        self.task_id = int(input('Введите id задачи: '))
        with open('tasks.json', 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)
        self.task = next((task for task in self.tasks if task['id'] == self.task_id), None)
        if self.task:
            self.task['status'] = True
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f'Задача {self.task_id} отмечена как выполненная!')
        else:   
            print('Задача с таким id не найдена.')

    def edit_task(self):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)
        self.task_id = int(input('Введите id задачи: '))
        self.task = next((task for task in self.tasks if task['id'] == self.task_id), None)
        if self.task:
            self.task['title'] = input('Введите новый заголовок задачи: ')
            self.task['description'] = input('Введите новое описание задачи: ')
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f'Задача {self.task_id} изменена успешно!')
        else:
            print('Задача с таким id не найдена.')

    def delete_task(self):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            self.tasks = json.load(file)
        self.task_id = int(input('Введите id задачи: '))
        self.task = next((task for task in self.tasks if task['id'] == self.task_id), None)
        if self.task:
            self.tasks.remove(self.task)
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f'Задача {self.task_id} удалена успешно!')
        else:
            print('Задача с таким id не найдена.')

    def import_export_tasks(self):
        print('Импорт и экспорт задач')
        print('1. Импорт задач из CSV.\n2. Экспорт задач в CSV.')
        self.import_export_action = int(input('Выберите действие: '))
        if self.import_export_action == 1:
            self.import_tasks_from_csv()
        elif self.import_export_action == 2:
            self.export_tasks_to_csv()
    
    def import_tasks_from_csv(self):
        self.import_tasks = []
        try:
            with open('tasks.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.import_id = row[0]
                    self.import_title = row[1]
                    self.import_description = row[2]
                    self.import_status = row[3]
                    self.import_priority = row[4]
                    self.import_due_date = row[5]
                    self.import_task = {'id': self.import_id, 'title': self.import_title, 'description': self.import_description, 'status': self.import_status, 'priority': self.import_priority, 'due_date': self.import_due_date}
                    self.import_tasks.append(self.import_task)
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(self.import_tasks, file, indent=4, ensure_ascii=False)
            print('Заметки импортированы из CSV успешно!')
        except FileNotFoundError:
            print('Файл tasks.csv не найден.')
        except Exception as e:
            print(f'Произошла ошибка: {e}')

    def export_tasks_to_csv(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                self.tasks = json.load(file)
            with open('tasks.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for task in self.tasks:
                    writer.writerow([task['id'], task['title'], task['description'], task['status'], task['priority'], task['due_date']])
            print('Заметки экспортированы в CSV успешно!')
        except FileNotFoundError:
            print('Файл tasks.json не найден.')
        except Exception as e:
            print(f'Произошла ошибка: {e}')

class ManageContacts:
    def __init__(self):
        print('\nУправление контактами')
        print(' 1. Добавление нового контакта \n 2. Поиск контакта по имени или номеру телефона \n 3. Редактирование контакта')
        print(' 4. Удаление контакта \n 5. Импорт и экспорт контактов в формате CSV')
        self.action = int(input('Выберите действие: '))
        if self.action == 1:
            self.add_contact()
        elif self.action == 2:
            self.find_contact()
        elif self.action == 3:
            self.edit_contact()
        elif self.action == 4:
            self.delete_contact()
        elif self.action == 5:
            self.import_export_csv()
        else:
            print(f'Неизвестное действие: {self.action}')
    
    def add_contact(self):
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
            self.id = len(self.contacts) + 1
            self.name = input(f'Введите имя контакта: ')
            self.phone = input(f'Введите номер телефона: ')
            self.email = input(f'Введите email: ')
            self.new_contact = {'id': self.id, 'name': self.name, 'phone': self.phone, 'email': self.email}
            self.contacts.append(self.new_contact)
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(self.contacts, file, ensure_ascii=False, indent=4)
            print('Новый контакт успешно добавлен')  

        except FileNotFoundError:
            self.contacts = []
            self.id = len(self.contacts) + 1
            self.name = input(f'Введите имя контакта: ')
            self.phone = input(f'Введите номер телефона: ')
            self.email = input(f'Введите email: ')
            self.new_contact = {'id': self.id, 'name': self.name, 'phone': self.phone, 'email': self.email}
            self.contacts.append(self.new_contact)
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(self.contacts, file, ensure_ascii=False, indent=4)
            print('Новый контакт успешно добавлен')  

        except Exception as e:
            print(f'Произошла ошибка {e}')

    def find_contact(self):
        print('Поиск контакта \n 1. Поиск по имени \n 2. Поиск по номеру телефона')
        self.find_action = int(input('Выберите действие: '))
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
            if self.find_action == 1:
                self.find_name = input('Введите имя контакта: ')
                self.contact = next((contact for contact in self.contacts if contact['name'] == self.find_name), None)
                if self.contact:
                    print(f'Контакт найден: {self.contact}')
                else:
                    print('Контакт не найден')

            elif self.find_action == 2:
                self.find_phone = input('Введите номер телефона контакта: ')
                self.contact = next((contact for contact in self.contacts if contact['phone'] == self.find_phone), None)
                if self.contact:
                    print(f'Контакт найден: {self.contact}')
                else:
                    print('Контакт не найден')

            else:
                print(f'Неизвестное действие: {self.find_action}')
        except FileNotFoundError:
            print('Файл contacts.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def edit_contact(self):
        self.edit_id = int(input('Введите id контакта: '))
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
            self.contact = next((contact for contact in self.contacts if contact['id'] == self.edit_id), None)
            if self.contact:
                self.contact['name'] = input('Введите новое имя контакта: ')
                self.contact['phone'] = input('Введите новый номер телефона контакта: ')
                self.contact['email'] = input('Введите новый email контакта: ')
                with open('contacts.json', 'w', encoding='utf-8') as file:
                    json.dump(self.contacts, file, ensure_ascii=False, indent=4)
                print('Контакт успешно изменен')
            else:
                print('Контакт не найден')

        except FileNotFoundError:
            print('Файл contacts.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def delete_contact(self):
        self.edit_id = int(input('Введите id контакта: '))
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
            self.contact = next((contact for contact in self.contacts if contact['id'] == self.edit_id), None)
            if self.contact:
                self.contacts.remove(self.contact)
                with open('contacts.json', 'w', encoding='utf-8') as file:
                    json.dump(self.contacts, file, ensure_ascii=False, indent=4)
                print('Контакт успешно удален')
            else:
                print('Контакт не найден')

        except FileNotFoundError:
            print('Файл contacts.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def import_export_csv(self):
        print('Импорт/Экспорт CSV')
        print(' 1. Экспорт в CSV файл \n 2. Импорт из CSV файла')
        self.ie_action = int(input('Выберите действие: '))
        if self.ie_action == 1:
            self.export_to_csv()
        elif self.ie_action == 2:
            self.import_from_csv()

    def export_to_csv(self):
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
            with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for contact in self.contacts:
                    writer.writerow([contact['id'], contact['name'], contact['phone'], contact['email']])
            print('Данные успешно импортированы из json в csv')

        except FileNotFoundError:
            print('Файл contacts.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def import_from_csv(self):
        try:
            self.import_contacts = []
            with open('contacts.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for line in reader:
                    self.import_contact = {'id': line[0], 'name': line[1], 'phone': line[2], 'email': line[3]}
                    self.import_contacts.append(self.import_contact)
                
            with open('contacts.json', 'w', encoding='utf-8') as file:
                json.dump(self.import_contacts, file, ensure_ascii=False, indent=4)
            print('Данные успешно импортированы из contacts.csv')

        except FileNotFoundError:
            print('Файл contacts.csv не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

class FinanceRecords:
    def __init__(self):
        print('Модель финансовых записей')
        print(' 1. Добавление новой записи \n 2. Просмотр всех записей \n 3. Генерация отчета \n 4. Импорт и экспорт записей в формате CSV')
        self.action = int(input('Выберите действие: '))
        if self.action == 1:
            self.add_fr()
        elif self.action == 2:
            self.list_fr()
        elif self.action == 3:
            self.generate_report()
        elif self.action == 4:
            self.import_export_csv()

    def add_fr(self):
        try:
            with open('finance.json', 'r', encoding='utf-8') as file:
                self.finance_records = json.load(file)
            self.id = len(self.finance_records) + 1
            self.amount = float(input('Введите сумму: '))
            self.category = input('Введите категорию: ')
            self.date = datetime.now().strftime('%d-%m-%Y')
            self.description = input('Введите описание: ')
            self.new_fr = {'id': self.id, 'amount': self.amount, 'category': self.category, 'date': self.date, 'description': self.description}
            self.finance_records.append(self.new_fr)
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(self.finance_records, file, ensure_ascii=False, indent=4)
            print('Финансовая запись успешно добавлена')    
            
        except FileNotFoundError:
            self.finance_records = []
            self.id = len(self.finance_records) + 1
            self.amount = float(input('Введите сумму: '))
            self.category = input('Введите категорию: ')
            self.date = datetime.now().strftime('%d-%m-%Y')
            self.description = input('Введите описание: ')
            self.new_fr = {'id': self.id, 'amount': self.amount, 'category': self.category, 'date': self.date, 'description': self.description}
            self.finance_records.append(self.new_fr)
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(self.finance_records, file, ensure_ascii=False, indent=4)
            print('Финансовая запись успешно добавлена')

        except Exception as e:
            print(f'Произошла ошибка {e}')

    def list_fr(self):
        try:
            with open('finance.json', 'r', encoding='utf-8') as file:
                self.finance_records = json.load(file)
            print('Типы фильтрации.')
            print('1. По дате \n2. По категории')
            self.filter_action = int(input('Выберите действие: '))
            if self.filter_action == 1:
                self.filter_date = int(input('Введите промежуток в днях (число): '))
                self.filtered_records = [record for record in self.finance_records if (datetime.now() - datetime.strptime(record['date'], '%d-%m-%Y')).days <= self.filter_date]
                for record in self.filtered_records:
                    print(f'{record["id"]}. {record["amount"]} - {record["category"]} - {record["date"]} - {record["description"]}')

            elif self.filter_action == 2:
                self.filter_category = input('Введите категорию: ')
                self.filtered_records = [record for record in self.finance_records if record['category'] == self.filter_category]
                for record in self.filtered_records:
                    print(f'{record["id"]}. {record["amount"]} - {record["category"]} - {record["date"]} - {record["description"]}')    


        except FileNotFoundError:
            print('Файл finance.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def generate_report(self):
        self.report_period = int(input('Введите промежуток в днях (число): '))
        with open('finance.json', 'r', encoding='utf-8') as file:
            self.finance_records = json.load(file)
        self.filtered_records = [record for record in self.finance_records if (datetime.now() - datetime.strptime(record['date'], '%d-%m-%Y')).days <= self.report_period]
        self.income = sum(record['amount'] for record in self.filtered_records if record['amount'] > 0)
        self.expenses = sum(record['amount'] for record in self.filtered_records if record['amount'] < 0)
        print(f'Доходы: {self.income}\nРасходы: {self.expenses}')
        self.balance = self.income + self.expenses
        print(f'Баланс по итогам периода: {self.balance}')
        self.events = len(self.filtered_records)
        print(f'Количество доходов и расходов за период: {self.events}')


    def import_export_csv(self):
        print('Выберите действие: \n 1. Импорт из csv \n 2. Экспорт в csv')
        self.ie_action = int(input('Выберите действие: '))
        if self.ie_action == 1:
            self.import_from_csv()
        elif self.ie_action == 2:
            self.export_to_csv()

    def import_from_csv(self):
        try:
            self.finance_records = []
            with open('finance.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.import_id = row[0]
                    self.import_amount = row[1]
                    self.import_category = row[2]
                    self.import_date = row[3]
                    self.import_description = row[4]
                    self.import_fr = {'id': self.import_id, 'amount': self.import_amount, 'category': self.import_category, 'date': self.import_date, 'description': self.import_description}
                    self.finance_records.append(self.import_fr)
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump(self.finance_records, file, ensure_ascii=False, indent=4)
            print('Данные успешно импортированы из csv в json')

        except FileNotFoundError:
            print('Файл finance.csv не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')

    def export_to_csv(self):
        try:
            with open('finance.json', 'r', encoding='utf-8') as file:
                    self.finance_records = json.load(file)
            with open('finance.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for record in self.finance_records:
                    writer.writerow([record['id'], record['amount'], record['category'], record['date'], record['description']])
            print('Данные успешно импортированы из json в csv')

        except FileNotFoundError:
            print('Файл finance.json не найден')
        except Exception as e:
            print(f'Произошла ошибка {e}')


class Calculator:
    def __init__(self):
        print('Калькулятор')
        print(' 1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление')
        self.calc_action = int(input('Выберите действие: '))
        if self.calc_action == 1:
            self.add()
        elif self.calc_action == 2:
            self.sub()
        elif self.calc_action == 3:
            self.mul()
        elif self.calc_action == 4:
            self.div()

    def add(self):
        self.a = float(input('Введите первое число: '))
        self.b = float(input('Введите второе число: '))
        self.result = self.a + self.b
        print(f'Результат: {self.result}')

    def sub(self):
        self.a = float(input('Введите первое число: '))
        self.b = float(input('Введите второе число: '))
        self.result = self.a - self.b
        print(f'Результат: {self.result}') 

    def mul(self):
        self.a = float(input('Введите первое число: '))
        self.b = float(input('Введите второе число: '))
        self.result = self.a * self.b
        print(f'Результат: {self.result}')

    def div(self):
        self.a = float(input('Введите первое число: '))
        self.b = float(input('Введите второе число: '))
        self.result = self.a / self.b
        print(f'Результат: {self.result}')  

def main():
    print("Добро пожаловать в персональный помощник!")
    print("1. Управление заметками \n2. Управление задачами \n3. Управление контактами \n4. Управление финансовыми записями \n5. Калькулятор \n6. Выход")
    action = int(input('Выберите действие: '))
    if action == 1:
        ManageNotes()
    elif action == 2:
        ManageTasks()
    elif action == 3:
        ManageContacts()
    elif action == 4:
        FinanceRecords()
    elif action == 5:
        Calculator()
    elif action == 6:
        pass
    else:
        print(f'Неизвестное действие: {action}')
        main()

if __name__ == "__main__":
    main()