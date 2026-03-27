from street_problem import StreetProblem
from cities import * 
from search import Search
from strategies import RandomStrategy

problem = StreetProblem(TRANI, MODUGNO)

strategy = RandomStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    path = result.path()
    print(path)
    
