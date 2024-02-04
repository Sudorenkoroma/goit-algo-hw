
def total_salary(path):

    try:
        # Зчитування файлу
        with open(path, mode='r') as file:
            lines = [el.strip() for el in file.readlines()]

        # Створення масиву з даними
        result_list = []
        for line in lines:
            name, salary = line.split(',')
            result_list.append((name, int(salary)))

        # Розрахунок загальної суми з/п
        total = 0
        for salaries in result_list:
            total += salaries[1]

        # Розрахунок середньої з/п
        num_developers = len(result_list)
        average = int(total / num_developers)

        return average, total

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return None
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return None


dataset = 'salary_file.txt'
average, total = total_salary(dataset)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")