print("TopLoader V 0.0.2")
print("Happy Loading!")
print("-----------------")
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone! ')
def loading():
    t = threading.Thread(target=animate)
    t.start()
import itertools
import threading
import sys
import time
done = False
loading()
import julia
from julia import Pkg
done = True
class Environment:
    envname = "env"
    jl = julia.Julia()
    pacman = Pkg
    def __init__(self,envname):
        """The initialization Function loads a virtual environment."""
        print("Loading Package Manager")
        self.pacman = Pkg
        print("Pkg loaded")
        if envname != "Global":
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
    def Remove(self,packagename):
        """Removes a given package from the environment."""
        self.pacman.rm(packagename)
        print("Package " + packagename + " Has been successfully removed.")
    def Build(self,packagename):
        self.pacman.build(packagename)
    def Update(self):
        self.pacman.update()
    def Instantiate(self):
        self.pacman.instantiate()
    def Test(self,packagename):
        self.pacman.test(packagename)
    def Resolve(self):
        self.pacman.resolve()
    def Include(self,filepath):
        self.jl.include(filepath)
        print("You will now be able to add your file with Environment.add()")
def Load(file):
    """Load and environment."""
    print("Loading file at: " + file)
    env = Environment(file)
    print("Environment loaded!")
    print(Pkg.installed())
    return(env)
