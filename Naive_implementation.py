#Parameter definitions
#Four zones 1, 2, 3, 4
from Zone import Zone
from Link import Link
from Route import Route
from Trip_demand import Trip_demand
from sympy import symbols, Eq


z1 = Zone("z1", 5)
z2 = Zone("z2", 10)
z3 = Zone("z3", 5)
z4 = Zone("z4", 10)
zones = [z1, z2, z3, z4]

#Random placeholder flow demands between TAZ's
q_12 = Trip_demand("q_12", z1, z2, 5)
q_13 = Trip_demand("q_13", z1, z3, 10)
q_14 = Trip_demand("q_14", z1, z4, 5)
q_23 = Trip_demand("q_23", z2, z3, 10)
q_24 = Trip_demand("q_24", z2, z4, 20)
q_34 = Trip_demand("q_34", z3, z4, 1)
q_21 = Trip_demand("q_21", z2, z1, 1)
q_31 = Trip_demand("q_31", z3, z1, 5)
q_41 = Trip_demand("q_41", z4, z1, 10)
q_32 = Trip_demand("q_3", z3, z2, 5)
q_42 = Trip_demand("q_42", z4, z2, 10)
q_43 = Trip_demand("q_43", z4, z3, 10)
q_list = [q_12, q_13, q_14, q_23, q_21, q_24, q_31, q_32, q_34, q_41, q_42, q_43]



l1 = Link("l1", z1, z2)
l2 = Link("l1", z2, z3)
l3 = Link("l1", z3, z4)
links = [l1, l2, l3]

# Routes will be lists of links
# Routes will later be included in zones for optimizations
r12 = Route("r12", [l1], z1, z2)
r13 = Route("r13", [l1, l2], z1, z3)
r14 = Route("r14", [l1, l2, l3], z1, z4)
r23 = Route("r23",[l2], z2, z3)
r21 = Route("r21",[l1], z2, z1)
r24 = Route("r24",[l2, l3], z2, z4)
r31 = Route("r31", [l2, l1], z3, z1)
r32 = Route("r32", [l2], z3, z2)
r34 = Route("r34", [l3], z3, z4)
r41 = Route("r41", [l3, l2, l1], z4, z1)
r42 = Route("r42", [l3, l2], z4, z2)
r43 = Route("r43", [l3], z4, z3)
routes = [r12, r13, r14, r23, r21, r24, r31, r32, r34, r41, r42, r43]




def objective_1():

    #M_i
    for global_zone in zones:
        global_mobility_equation = '('
        # Mobility calculation for each zone
        #M_j
        equations = []
        for current_zone in zones:
            if global_zone != current_zone:
                for q in q_list:
                    if q.get_start() == global_zone and q.get_end() == current_zone:
                        demand = q.get_demand()
                var_list = []
                for route in routes: 
                    if route.get_start() == global_zone and route.get_end() == current_zone:
                        #Create a naming string for two new decision variables
                        route_name = route.get_name()
                        start_index = global_zone.get_name()
                        end_index = current_zone.get_name()
                        #Sample name is qr14z1z4
                        var1name = "q" + route_name + start_index + end_index
                        var2name = "t" + route_name + start_index + end_index
                        var_list.append(var1name)
                        var_list.append(var2name)
                equation = '('
                for var in var_list:
                    if equation != '(':
                        equation = equation + ' + ' + var
                    else:
                        equation = equation + var
                equation = equation + ')/' + str(demand)
                equations.append(equation)

        
        for equation in equations:
            if global_mobility_equation == '(':
                global_mobility_equation = global_mobility_equation + equation
            else:
                global_mobility_equation = global_mobility_equation + " + " + equation
        print("Zone " + global_zone.get_name() + " mobility function is " + global_mobility_equation)
                        
                        
objective_1()