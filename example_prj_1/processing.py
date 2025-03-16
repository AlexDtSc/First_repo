def calculate_statistics(temperatures: list[float]) -> dict:
    if not temperatures:
        return None

    min_temp = min(temperatures)
    max_temp = max(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)
    median_temp = calculate_median(temperatures)

    return {
        "min": min_temp,
        "max": max_temp,
        "average": avg_temp,
        "median": median_temp,
    }

def calculate_median(temperatures: list[float]) -> float:
    temperatures.sort()
    n = len(temperatures)
    mid = n // 2
    if n % 2 == 0:
        return (temperatures[mid - 1] + temperatures[mid]) / 2
    else:
        return temperatures[mid]
    
    
# Для непарної кількості спостережень медіана є спостереженням з номером k=(n+1)/2. де n - кількість елементів у відсортованій за зростанням вибірці [1,4,7...,20]
# Для парної кількості спостережень медіана обчислюється як середнє значення
# спостережень з номерами n/2 і (n+2)/2  ->    k = (n/2 + (n+2)/2) / 2