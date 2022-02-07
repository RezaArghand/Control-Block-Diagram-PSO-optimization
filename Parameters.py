import control.matlab as control

s = control.tf('s')

# parameters of PSO optimization algorithm
number_of_particles = 50  # particle count
damping_rate_W = 0.9  # inertia damper
max_of_variable = 1  # max domain
min_of_variable = -1  # min domain
satisfaction_cost_number = 1.0e-200  # satisfaction point
W = 0.95  # inertia
C1 = 1.4962  # cognitive (particle)
C2 = 2.4962  # social (swarm)
max_iteration_number = 100  # max iteration
# end parameters of PSO optimization


# pid selection
# 0: pid is set to zero (pid and its root are ignored)
# 1: pid is calculated as 1 (pid is ignored but the path remains in block diagram)
# 2: pid is calculated in PSO (default)
pid1 = 2
pid2 = 2
pid3 = 2
# end pid selection

# plant define
Plant = 1 / (s ** 2 + 10 * s + 20)  # Plant of the block diagram
# end plant define
