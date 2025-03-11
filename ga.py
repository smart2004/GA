import random

# Параметры алгоритма
POPULATION_SIZE = 10  # Размер популяции
GENOME_LENGTH = 5     # Длина генома (количество бит)
MUTATION_RATE = 0.01  # Вероятность мутации
GENERATIONS = 20      # Количество поколений

# Функция для оценки приспособленности
def fitness(genome):
    # Преобразуем двоичный геном в десятичное число
    x = int(''.join(map(str, genome)), 2)
    return x ** 2  # Мы максимизируем f(x) = x^2

# Создание начальной популяции
def create_population(size):
    return [[random.randint(0, 1) for _ in range(GENOME_LENGTH)] for _ in range(size)]

# Селекция (турнирный отбор)
def selection(population):
    tournament = random.sample(population, 3)  # Случайный выбор 3-х особей
    tournament.sort(key=fitness, reverse=True)  # Сортируем по приспособленности
    return tournament[0]  # Возвращаем лучшую особь

# Кроссовер
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENOME_LENGTH - 1)  # Точка кроссовера
    child = parent1[:crossover_point] + parent2[crossover_point:]  # Создаем потомка
    return child

# Мутация
def mutate(genome):
    for i in range(GENOME_LENGTH):
        if random.random() < MUTATION_RATE:  # Если происходит мутация
            genome[i] = 1 - genome[i]  # Инвертируем бит
    return genome

# Основной цикл генетического алгоритма
def genetic_algorithm():
    population = create_population(POPULATION_SIZE)  # Создаем начальную популяцию

    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = selection(population)  # Выбор первого родителя
            parent2 = selection(population)  # Выбор второго родителя
            child = crossover(parent1, parent2)  # Кроссовер
            child = mutate(child)  # Мутация
            new_population.append(child)  # Добавляем потомка в новую популяцию
        
        population = new_population  # Обновляем популяцию

        # Вывод лучшего решения в поколении
        best_genome = max(population, key=fitness)  # Находим лучший геном
        print(f"Generation {generation + 1}: Best Genome: {best_genome}, Fitness: {fitness(best_genome)}")

# Запуск генетического алгоритма
if __name__ == "__main__":
    genetic_algorithm()