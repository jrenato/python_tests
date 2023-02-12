from lib_tests.devices import Smartphone

smartphone = Smartphone()

# Initial state: off and without battery
assert smartphone.is_powered() == False
assert smartphone.get_charge() == 0

# Try to turn on the smartphone with insufficient battery
assert smartphone.power_on() == 'Not enough charge'

# Charging battery
assert smartphone.charge_battery() == 'Charging'
assert smartphone.get_charge() == 1

# Try to turn on the smartphone with insufficient battery
assert smartphone.power_on() == 'Not enough charge'

# Charge the smartphone until 100%
assert smartphone.charge_battery(99) == 'Charging'
assert smartphone.get_charge() == 100

# Try to charge the smartphone with full battery
assert smartphone.charge_battery() == 'Already charged'

# Try to turn on the smartphone with full battery
assert smartphone.power_on() == 'Powered on'

# Try to turn on a smartphone that is already on
assert smartphone.power_on() == 'Already powered on'

# Play a game called 'Snake', which consumes 3% of the battery
assert smartphone.play_game('Snake') == 'Playing game: Snake'
assert smartphone.get_charge() == 97

# It consumes 1% of the battery
assert smartphone.discharge_battery() == 'Discharging'
assert smartphone.get_charge() == 96

# Discharge the smartphone until it reaches 7%
assert smartphone.discharge_battery(89) == 'Discharging'
assert smartphone.get_charge() == 7

# Play Snake again and the smartphone turns off because it is below 5%
assert smartphone.play_game('Snake') == 'Powering off'
assert smartphone.is_powered() == False
assert smartphone.get_charge() == 4

# Try to turn off the smartphone, but it is already off
assert smartphone.power_off() == 'Already powered off'

# Try to turn on the smartphone with insufficient battery
assert smartphone.power_on() == 'Not enough charge'

print("Passed all tests! :)")