from data import load_data, clean_data
from processing import calculate_statistics

def main():
    filename = "temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")

if __name__ == "__main__":
    main()

'''
if stats:: Перевіряємо, чи є в нас статистичні дані. Якщо функція calculate_statistics повернула коректний результат (не порожній словник), то виводимо статистику:
stats['min'] — мінімальна температура.
stats['max'] — максимальна температура.
stats['average'] — середнє значення температури, виводиться з точністю до двох знаків після коми.
stats['median'] — медіанна температура, також з точністю до двох знаків.
Якщо статистичні дані не були знайдені або файл порожній, то виведемо повідомлення "No temperature data available."
'''