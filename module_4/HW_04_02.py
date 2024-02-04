def get_cats_info(path):
    try:
        # Зчитування файлу
        with open(path, mode='r') as file:
            lines = [el.strip() for el in file.readlines()]

        # Створення списку словників
        data = []
        for line in lines:
            name, id, age = line.split(',')
            cat_ifo = {
                "name": name,
                "id": id,
                "age": age
            }
            data.append(cat_ifo)
        return data
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")


cats_info = get_cats_info("cats_file.txt")
print(cats_info)