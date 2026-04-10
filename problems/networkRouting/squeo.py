from path_search.node import Node
# Nodes
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"

# Node latency
node_latency = {
A: 1,
B: 2,
C: 1,
D: 3,
E: 2,
F: 1,
G: 2
}
# Edge latency
network = {
A: {B: 2, C: 5},
B: {D: 4, E: 1},
C: {F: 3},
D: {G: 6},
E: {D: 2, G: 3},
F: {E: 4, G: 2},
G: {}
}

class NetworkRoutingProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        possible_action = list(network.get(state, {}).keys())
        print(f"Possible actions from {state}: {possible_action}")
        return possible_action

    def result(self, _, action):
        return action
    
    def explore(self, node):
        path = [node]
        while node._parent is not None:
            path.append(node._parent)
            node = node._parent
        
        return path[::-1]
    
    def action_cost(self, state, action):
        return node_latency[state] + network[state][action]
    
    def is_goal(self, state):
        return state == self.goal_state
    