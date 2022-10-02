from pyswmm import Simulation


"""First option"""
# sim = Simulation(inputfile='Site_Drainage_Model.inp')
# sim.execute()

#
# """Second option"""
# with Simulation(inputfile='Site_Drainage_Model.inp') as sim:
#     for step in sim:
#         print(step.flow_routing_stats())
