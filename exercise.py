
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if fireball_cost>self.mana:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.health -= fireball_damage
        

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
            
        

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana



class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance 

    def deposit(self, amount):
        if amount <=0:
            raise ValueError(f"cannot deposit zero or negative funds")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError(f"cannot withdraw zero or negative funds")
        if self.__balance> amount:
            self.__balance -= amount
        else:
            raise ValueError(f"insufficient funds")


class Student:
    def __init__(self, name):
        self.__courses = {}
        self.name = name

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif 80 <= score <= 89:
            return "B"
        elif 70 <= score <= 79:
            return "C"
        elif 60 <=score <= 69:
            return "D"
        else:
            return "F"
            
    def add_course(self, course_name, score):
        self.__courses[course_name]=self.calculate_letter_grade(score)

    def get_courses(self):
        return  self.__courses
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows< num:
            raise Exception(f"not enough arrows")
        else:
            self.__num_arrows-=num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name,num_arrows)
        
    def triple_shot(self, target):
        self.use_arrows(3)
        return f"{target.get_name()} was shot by 3 crossbow bolts"

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_by_blast = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
        return hit_by_blast
