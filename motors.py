class Rotation_Motor():

    def __init__(self, name):
        self.running = False
        self.name = name

    def start(self):
        self.running = True
        print(f'{self.name} motor is running !')

    def stop(self):
        self.running = False
        print(f'{self.name} motor has stopped !')
