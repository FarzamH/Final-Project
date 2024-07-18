import random

# Hyper-Parameters
POPULATION_SIZE = 8
GENERATIONS = 100
INITIAL_MUTATION_RATE = 0.1


# Create an individual
def create_binary_number():
    return [random.randint(0, 1) for _ in range(5)]


def binary_to_decimal(binary):
    return sum(bit * (2 ** i) for i, bit in enumerate(reversed(binary)))


def fitness(individual):
    x = binary_to_decimal(individual)
    return x ** 2


def crossover(parent1, parent2):
    return [parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(parent1))]


def mutate(individual, generation):
    mutation_rate = INITIAL_MUTATION_RATE * (1 - generation / GENERATIONS)
    if random.random() < mutation_rate:
        mutation_index = random.randint(0, len(individual) - 1)
        individual[mutation_index] = 1 - individual[mutation_index]
    return individual


def calculate_selection_probabilities(population):
    fitnesses = [fitness(ind) for ind in population]
    total_fitness = sum(fitnesses)
    return [fit / total_fitness for fit in fitnesses]


def selection(population, probabilities):
    return random.choices(population, weights=probabilities, k=1)[0]


def genetic_algorithm():
    population = [create_binary_number() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)

        if generation % 5 == 0:
            best = population[0]
            print(
                f"Generation {generation} : Best current solution = {binary_to_decimal(best)}, f(x) = {fitness(best)}")

        selection_probabilities = calculate_selection_probabilities(population)

        new_population = population[:2]

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population, selection_probabilities)
            parent2 = selection(population, selection_probabilities)
            child = crossover(parent1, parent2)
            child = mutate(child, generation)
            new_population.append(child)

        population = new_population

    best_solution = max(population, key=fitness)
    best_decimal_solution = binary_to_decimal(best_solution)
    best_fitness = fitness(best_solution)

    return best_decimal_solution, best_fitness


if __name__ == "__main__":
    best_decimal_solution, best_fitness = genetic_algorithm()
    print(f"\nBest solution: x = {best_decimal_solution}, f(x) = {best_fitness}")