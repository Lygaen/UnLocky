class Tension_Capteur():

    def __init__(self, name):
        self.chock_state = False
        self.name = name

    def got_chock(self, check:int):
        if self.chock_state:
            print(f'{self.name} tension captors detect a chock at check {check} !')
        else:
            print(f"{self.name} tension captors didn't detected a chock | check {check}")
        return self.chock_state

    def set_chock(self, chock: bool):
        self.chock_state = chock


class Poussoir_Capteur():

    def __init__(self, name):
        self.state = False
        self.name = name

    def set_state(self, new_state: bool):
        self.state = new_state
        if self.state:
            print(f'{self.name} poussoir captor is enabled')
        else:
            print(f"{self.name} poussoir captor isn't enabled")
