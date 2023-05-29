import random

# Şehir sınıfı
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = (x_distance ** 2 + y_distance ** 2) ** 0.5
        return distance

# Genetik algoritma sınıfı
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, cities):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.cities = cities
        self.population = []

    # Rastgele bir yolculuk rotası oluşturur
    def create_route(self):
        route = random.sample(self.cities, len(self.cities))
        return route

    # Popülasyonu oluşturur
    def create_population(self):
        for _ in range(self.population_size):
            route = self.create_route()
            self.population.append(route)

    # Bir yolculuk rotasının uygunluğunu hesaplar (mesafe)
    def fitness(self, route):
        total_distance = 0
        for i in range(len(route)):
            current_city = route[i]
            next_city = route[(i + 1) % len(route)]  # Döngü için son şehire dön
            total_distance += current_city.distance_to(next_city)
        return total_distance

    # Turnuva seçimi ile ebeveynleri seçer
    def selection(self):
        tournament_size = int(self.population_size * 0.1)
        tournament = random.sample(self.population, tournament_size)
        best_route = min(tournament, key=self.fitness)
        return best_route

    # Çaprazlama işlemi 
    def crossover(self, parent1, parent2):
        start_index = random.randint(0, len(parent1) - 1)
        end_index = random.randint(start_index + 1, len(parent1))
        child1 = parent1[start_index:end_index]
        child2 = [city for city in parent2 if city not in child1]
        child = child1 + child2
        return child

    # Mutasyon işlemi
    def mutation(self, route):
        for _ in range(len(route)):
            if random.random() < self.mutation_rate:
                index1 = random.randint(0, len(route) - 1)
                index2 = random.randint(0, len(route) - 1)
                route[index1], route[index2] = route[index2], route[index1]

    # Yeni nesli oluşturur
    def create_new_generation(self):
        new_population = []
        while len(new_population) < self.population_size:
            parent1 = self.selection()
            parent2 = self.selection()
            child = self.crossover(parent1, parent2)
            self.mutation(child)
            new_population.append(child)
        self.population = new_population

    def find_best_route(self):
        best_route = min(self.population, key=self.fitness)
        return best_route



num_cities = 20

cities = []
for _ in range(num_cities):
    x = random.randint(0, 200) 
    y = random.randint(0, 200) 
    cities.append(City(x, y))


# Genetik algoritma parametreleri
population_size = 100
mutation_rate = 0.01
generation_count = 1000

# Genetik algoritma örneği ve popülasyonun oluşturulması
genetic_algorithm = GeneticAlgorithm(population_size, mutation_rate, cities)
genetic_algorithm.create_population()

# Belirtilen nesil sayısı kadar yeni nesil oluşturma
for _ in range(generation_count):
    genetic_algorithm.create_new_generation()
# En kısa rotanın alınması
best_route = genetic_algorithm.find_best_route()

print("En kısa yolculuk rotası:")
for i, city in enumerate(best_route, 1):
    print(f"{i}: {city.x}, {city.y}")

