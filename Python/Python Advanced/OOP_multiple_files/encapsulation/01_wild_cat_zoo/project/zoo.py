class Zoo():
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.animal_dict = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        self.worker_dict = {'Keeper': [], 'Caretaker': [], 'Vet': []}

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.__budget -= price
            self.animals.append(animal)

            animal_type = animal.__class__.__name__

            self.animal_dict[animal_type].append(animal)

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if len(self.animals) < self.__animal_capacity and price > self.__budget:
            return f"Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return f"Not enough space for worker"

        job = worker.__class__.__name__
        self.worker_dict[job].append(worker)
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.worker_dict[worker.__class__.__name__].remove(worker)
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_to_be_paid = 0
        for worker in self.workers:
            sum_to_be_paid += worker.salary

        if self.__budget < sum_to_be_paid:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_to_be_paid
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_to_be_paid = 0
        for animal in self.animals:
            sum_to_be_paid += animal.money_for_care

        if self.__budget < sum_to_be_paid:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_to_be_paid
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = []
        lions = self.animal_dict['Lion']
        tigers = self.animal_dict['Tiger']
        cheetahs = self.animal_dict['Cheetah']
        total_animals = len(lions) + len(tigers) + len(cheetahs)

        result.append(f"You have {total_animals} animals")
        # Lions
        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(lion.__repr__())
        # Tigers
        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(tiger.__repr__())
        # Cheetahs
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(cheetah.__repr__())

        return '\n'.join(result)

    def workers_status(self):
        result = []
        keepers = self.worker_dict['Keeper']
        caretakers = self.worker_dict['Caretaker']
        vets = self.worker_dict['Vet']
        total_workers = len(keepers) + len(caretakers) + len(vets)

        result.append(f"You have {total_workers} workers")
        #Keepers
        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(keeper.__repr__())
        #Caretakers
        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker.__repr__())
        #vets
        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(vet.__repr__())

        return '\n'.join(result)

