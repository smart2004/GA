import random

# Параметры
POPULATION_SIZE = 10
GENOME_LENGTH = 5
MUTATION_RATE = 0.01
GENERATIONS = 20

# Функция для оценки приспособленности
def fitness(genome):
    x = int(''.join(map(str, genome)), 2)
    return x ** 2

# Создание начальной популяции
def create_population(size):
    return [[random.randint(0, 1) for _ in range(GENOME_LENGTH)] for _ in range(size)]

# Селекция (турнирный отбор)
def selection(population):
    tournament = random.sample(population, 3)
    tournament.sort(key=fitness, reverse=True)
    return tournament


print(tournament)
