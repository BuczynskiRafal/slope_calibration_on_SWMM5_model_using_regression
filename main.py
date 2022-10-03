from pyswmm import Simulation, Nodes, Links


"""
1. Open SWMM file - done
2. Get data about slope
3. Get data about velocity
4. Get data bout depth
5. Prepare algorithm to calibration model
    - validate velocity
    - validate depth
    - check if slope is minimal
    - if not use regression or other algorithm to calibrate slope
6. Insert new data to model
7. Execute simulation again
8. Show result in SWMM
"""

with Simulation(inputfile='example.inp') as sim:
    # print([link.linkid for link in Links(sim)])
    for link in Links(sim):
        # print(link.linkid)
        print(link.inlet_node)
        print(link.outlet_node)