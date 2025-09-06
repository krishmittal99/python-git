# 16. Robot class
class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        print(f"{self.name} is performing task: {self.task}")
        self.battery_level -= 10

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is recharged.")

    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")
