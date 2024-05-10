class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}\nСрок выполнения: {self.deadline}\nСтатус: {status}"


def add_task(task_list, description, deadline):
    task = Task(description, deadline)
    task_list.append(task)


def mark_task_completed(task_list, task_index):
    if 0 <= task_index < len(task_list):
        task_list[task_index].mark_as_completed()


def get_current_tasks(task_list):
    current_tasks = [task for task in task_list if not task.completed]
    return current_tasks


# Пример использования:
tasks = []

# Добавление задач
add_task(tasks, "Сделать уборку", "10.05.2024")
add_task(tasks, "Подготовить отчет", "15.05.2024")
add_task(tasks, "Позвонить в банк", "12.05.2024")

# Отметка задачи как выполненной
mark_task_completed(tasks, 0)

# Вывод текущих задач
current_tasks = get_current_tasks(tasks)
print("Текущие задачи:")
for index, task in enumerate(current_tasks):
    print(f"Задача {index + 1}:")
    print(task)
    print()

