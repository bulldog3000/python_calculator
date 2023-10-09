def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"

while True:
    user_input = input("Введите математический пример (или 'exit' для выхода): ")

    if user_input.lower() == 'exit':
        break

    result = calculate(user_input)
    print(f"Результат: {result}")
