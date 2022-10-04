import pprint
from pyswmm import Simulation, Nodes, Links, Link
from pyswmm.links import Conduit


pp = pprint.PrettyPrinter(indent=4)

"""
1. Open SWMM file - done
2. Get start nodes of network
3. Get data about slope
4. Get data about velocity
5. Get data bout depth
6. Prepare algorithm to calibration model
    - validate velocity
    - validate depth
    - check if slope is minimal
    - if not use regression or other algorithm to calibrate slope
7. Insert new data to model
8. Execute simulation again
9. Show result in SWMM
"""

# 1. Open SWMM file - using the context manager will automatically remove garbage
with Simulation(inputfile='example.inp') as sim:
    link = Links(sim)["C3"]

    print("\n\n\nConduits\n")
    # link = Links(sim)["C2"]

    sim.step_advance(300)
    for ind, step in enumerate(sim):
        pp.pprint(link.conduit_statistics)

    # 1. Get data about slope
    # 1.1. Get data about connectors levels

    # 1.2. Calculate slope
    # 1.3. Validate slope
    # 1.4. If not minimal insert calculate new connectors levels and insert to model.