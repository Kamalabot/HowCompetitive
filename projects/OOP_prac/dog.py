class Dog:
    species = "Canis familiaris"

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        print(f"{self.name} says {sound}")


philo = Dog(name="philo",age=5)
print(philo)
philo.speak('Wooo')
