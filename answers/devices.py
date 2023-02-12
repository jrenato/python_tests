
class Smartphone():
    charge = 0
    min_charge = 5
    powered = False


    def power_on(self):
        if self.charge >= self.min_charge:
            if self.powered:
                return 'Already powered on'
            self.powered = True
            return 'Powered on'
        else:
            return 'Not enough charge'


    def power_off(self):
        if self.powered:
            self.powered = False
            return 'Powered off'
        else:
            return 'Already powered off'


    def is_powered(self):
        return self.powered


    def charge_battery(self, charge=1):
        if self.charge >= 100:
            return 'Already charged'
        self.charge += charge
        return 'Charging'


    def discharge_battery(self, discharge=1):
        self.charge -= discharge

        if self.charge < 0:
            self.charge = 0

        if self.charge > self.min_charge:
            return 'Discharging'
        else:
            self.powered = False
            return 'Powering off'


    def get_charge(self):
        return self.charge


    def play_game(self, game_name):
        if self.discharge_battery(3) == 'Powering off':
            return 'Powering off'

        return 'Playing game: {}'.format(game_name)
