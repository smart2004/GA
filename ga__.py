import random  # Импортируем модуль random для генерации случайных чисел

# Параметры алгоритма
POPULATION_SIZE = 10  # Размер популяции
GENOME_LENGTH = 5     # Длина генома (количество бит)
MUTATION_RATE = 0.1  # Вероятность мутации
GENERATIONS = 10      # Количество поколений

# Функция для оценки приспособленности
def fitness(genome):
    # Преобразуем геном (список бит) в целое число
    x = int(''.join(map(str, genome)), 2)
    # Возвращаем значение функции f(x) = x^2
    return x ** 2

# Создание начальной популяции
def create_population(size):
    # Генерируем популяцию из случайных индивидов (списков бит)
    return [[random.randint(0, 1) for _ in range(GENOME_LENGTH)] for _ in range(size)]

# Селекция (турнирный отбор)
def selection(population):
    # Случайно выбираем 3 индивида из популяции для турнира
    tournament = random.sample(population, 3)
    # Сортируем турниров по их приспособленности (от наилучшего к наихудшему)
    tournament.sort(key=fitness, reverse=True)
    # Возвращаем лучшего индивида из турнира
    return tournament[0]

# Основной цикл генетического алгоритма
def genetic_algorithm():
    # Создаем начальную популяцию
    population = create_population(POPULATION_SIZE)

    # Цикл по поколениям
    for generation in range(GENERATIONS):
        new_population = []  # Новая популяция для следующего поколения
        
        # Формируем новую популяцию
        for _ in range(POPULATION_SIZE):
            # Выбираем двух родителей
            parent1 = selection(population)
            parent2 = selection(population)

            # Кроссовер: выбираем случайную точку для кроссовера
            crossover_point = random.randint(1, GENOME_LENGTH - 1)
            # Создаем потомка путем комбинирования геномов родителей
            child = parent1[:crossover_point] + parent2[crossover_point:]

            # Мутация: случайно изменяем бит в геноме с заданной вероятностью
            if random.random() < MUTATION_RATE:
                mutation_point = random.randint(0, GENOME_LENGTH - 1)
                child[mutation_point] = 1 - child[mutation_point]  # Переключаем бит

            # Добавляем потомка в новую популяцию
            new_population.append(child)

        # Обновляем популяцию
        population = new_population
        # Находим лучший индивид в текущем поколении
        best_genome = max(population, key=fitness)
        # Выводим информацию о текущем поколении
        print(f"Поколение {generation}: лучший геном {best_genome}, приспособленность {fitness(best_genome)}")

# Запуск алгоритма
genetic_algorithm()
