import random
import time

def generate_random_color_and_number():
    # Определяем список цветов 
    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "White", "Black"]
    
    # Случайный выбор цвета и числа
    random_color = random.choice(colors)
    random_number = random.randint(1, 6)
    
    # Формируем вывод
    output = f"{random_color}{random_number}"
    return output

if __name__ == "__main__":
    result = generate_random_color_and_number()
    time.sleep(1)
    print(result)
