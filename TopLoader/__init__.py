print("TopLoader V 0.0.1")
print("Happy Loading!")
print("-----------------")
import julia
from julia import Pkg
class Environment:
    envname = "env"
    jl = julia.Julia()
    pacman = Pkg
    def __init__(self,envname):
        """The initialization Function loads a virtual environment."""
        print("Loading Package Manager")
        self.pacman = Pkg
        print("Pkg loaded")
        self.envname = envname
        self.pacman.activate(envname)
        print("Activated Package Environment: " + envname)
        print("Environment available at: /" + envname)
    def Add(self, pack):
        """Adds a package"""
        self.pacman.add(pack)
    def Using(self,packagename):
        """Imports and returns a package"""
        impstring = "from julia import " + str(packagename)
        exec(impstring)
        grabstring = str(packagename)
        w = eval(grabstring)
        return(w)
    def Switch(self,envname):
        """Allows you to quickly switch environments"""
        self.pacman.activate(envname)
        print("Environment created at /" + envname)
    def List(self):
        """Lists the current packages inside of this environment"""
        return(Pkg.installed())
def Load(file):
    """Load and environment."""
    print("Loading file at: " + file)
    env = Environment(file)
    print("Environment loaded!")
    print(Pkg.installed())
    return(env)
