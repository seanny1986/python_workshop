"""
Some more advanced functions. Here we have a simple "simulation".
-- Sean Morrison, 2018 
"""

# here we are returning values that can be used elsewhere
# furthermore, the simulation_step function calls the functions
# calculate_forces and calculate_accelerations. I.e. you can call
# functions from other functions
def simulation_step(x, y, dt):
    forces = calculate_forces()
    print(forces)
    dx_dt, dy_dt = calculate_accelerations(forces)
    x += dx_dt*dt
    y += dy_dt*dt
    return x, y

def calculate_forces():
    return 1.

def calculate_accelerations(forces):
    return 0.1*forces, 0.05*forces

# and here we use a loop to repeatedly call the step function. This will
# come in handy later once we start looking at quadrotor simulation
x, y, t, dt = 0, 0, 0, 0.01
for i in range(11):
	x, y = simulation_step(x, y, dt) 
	t += dt
	print("x val: {:.3f}, y val: {:.3f}, time: {:.3f}".format(x, y, t))	