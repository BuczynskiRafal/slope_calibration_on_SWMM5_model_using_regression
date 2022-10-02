from pyswmm import Simulation, Nodes


with Simulation(inputfile='Site_Drainage_Model.inp') as sim:
    node_object = Nodes(sim)

    # J1 node instalation
    J1 = node_object['J1']