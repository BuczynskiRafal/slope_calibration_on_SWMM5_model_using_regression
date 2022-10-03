from pyswmm import Simulation, Nodes, Links, Link
from pyswmm.links import Conduit

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
    sim.execute()
    # print([link.linkid for link in Links(sim)])
    # for link in Links(sim):
        # print(link.linkid)
    link = Links(sim)["3"]
    print(type(link))
    # link.flow_limit = 0.5
    print('\n')
    # print(f"link.inlet_node: {link.inlet_node}")
    # print(f"link.outlet_node: {link.outlet_node}")
    # print(f"link.depth: {link.depth}")
    # print(f"link.flow: {link.flow}")
    # print(f"link.connections: {link.connections}")
    # print(f"link.depth: {link.depth}")
    # print(f"link.ds_xsection_area: {link.ds_xsection_area}")
    # print(f"link.flow: {link.flow}")
    # print(f"link.flow_limit: {link.flow_limit}")
    # print(f"link.froude: {link.froude}")
    # print(f"link.initial_flow: {link.initial_flow}")
    # print(f"link.inlet_head_loss: {link.inlet_head_loss}")
    # print(f"link.inlet_node: {link.inlet_node}")
    # print(f"link.inlet_offset: {link.inlet_offset}")
    # print(f"link.is_orifice: {link.is_orifice()}")
    # print(f"link.is_outlet: {link.is_outlet()}")
    # print(f"link.is_conduit: {link.is_conduit()}")
    # print(f"link.linkid: {link.linkid}")
    # print(f"link.outlet_head_loss: {link.outlet_head_loss}")
    # print(f"link.target_setting: {link.target_setting}")
    print(f"link.conduit_statistics: {link.conduit_statistics}")

    # stats = Conduit()
    # print(f"stats: {stats}")
