train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5 / 9)
  return round(c_temp, 2)

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return round(f_temp)

c0_in_fahrenheit = c_to_f(0)
#print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return str(mass * acceleration)
  
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + train_force + " Newtons of force")
#The GE train supplies 226800 Newtons of force

def get_energy(mass, c = 3 * 10 ** 8):
  return str(mass * (c ** 2))

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + bomb_energy + " Joules.")
#A 1kg bomb supplies 90000000000000000 Joules.

def get_work(mass, acceleration, distance):
  return str(mass * acceleration * distance)

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + train_work + " Joules of work over " +  str(train_distance) + " meters.")
#The GE train does 22680000 Joules of work over 100 meters.
