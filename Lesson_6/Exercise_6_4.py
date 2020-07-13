# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started.'

    def stop(self):
        return f'{self.name} is stopped.'

    def turn_right(self):
        return f'{self.name} is turned right.'

    def turn_left(self):
        return f'{self.name} is turned left.'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}.')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car.'
        else:
            return f'Speed of {self.name} is normal for town car.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}.')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car.'
        else:
            return f'Speed of {self.name} is normal for work car.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department.'
        else:
            return f'{self.name} is not from police department.'


mazda = SportCar(140, 'Red', 'Mazda', False)
pegoute = TownCar(35, 'White', 'Pegoute', False)
toyota = WorkCar(70, 'Grey', 'Toyota', True)
skoda = PoliceCar(110, 'Blue', 'Skoda', True)
print(toyota.turn_left())
print(f'When {pegoute.turn_right()}, then {mazda.stop()}')
print(f'{toyota.go()} with speed exactly {toyota.show_speed()}')
print(f'{toyota.name} is {toyota.color}')
print(f'Is {mazda.name} a police car? {mazda.is_police}')
print(f'Is {toyota.name}  a police car? {toyota.is_police}')
print(mazda.show_speed())
print(pegoute.show_speed())
print(skoda.police())
print(skoda.show_speed())
