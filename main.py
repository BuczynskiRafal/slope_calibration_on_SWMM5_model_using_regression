from pyswmm import Simulation


"""First option"""
sim = Simulation(inputfile='./testmodel.inp')
sim.execute()


"""Second option"""
with Simulation(inputfile='./testmodel.inp') as sim:
    for step in sim:
        step.flow_routing_stats()
