from pyswmm import Simulation


with Simulation(inputfile='Site_Drainage_Model.inp') as sim:
    sim.step_advance(300)
    for step in sim:
        print(sim.current_time)