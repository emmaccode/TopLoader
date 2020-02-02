<div align="center"><img src="https://github.com/emmettgb/TopLoader/blob/0.0.1/toploader.jpg" width="300" /><h1>TopLoader</h1></div>



### Easily Manage Julia Environments From Python
Hello, and happy loading! You can install TopLoader with:
```bash
sudo pip3 install TopLoader
```
Now from TopLoader you can either load a Julia environment, or create a new one:
```python
Python 3.7.6 (default, Dec 19 2019, 22:52:49) 
[GCC 9.2.1 20190827 (Red Hat 9.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import TopLoader
TopLoader V 0.0.1
Happy Loading!
-----------------
```
## Usage
If you don't have an environment to load, the first thing to do is construct an environment, which you can do with the TopLoader.Environment constructor. In the case that you are loading, you can use TopLoader.load(filepath) to load an environment. Running through Environment functions:
#### Setting an Environment
```python
>>> env = TopLoader.Environment("Environment_Name")
Loading Package Manager
Pkg loaded
Activating new environment at `~/Projects/TopLoader/Environment_Name/Project.toml`
Activated Package Environment: Environment_Name
Environment available at: /Environment_Name
```
**To use you're Julia installation's packages, set the environment name to "Global", here's an example:**
```python
from TopLoader import Environment
env = Environment("Global")
```
-------------------------------------------------
Constructing our Environment takes a name parameter, shown above. 
You can use any string, of course. 
The environment won't instantiate until you add a package. 
So in other words, a randomly created environment won't mess up your harddrive.
#### Add(package_name)
```python
>>> env.Add("Lathe")
 Resolving package versions...
  Updating `~/Projects/TopLoader/test/Project.toml`
  [38d8eb38] + Lathe v0.0.3

```
The Add() Method takes an obvious hyperparameter to add a package through Pkg.
#### List()
```python 
>>> env.List()
{'Lathe': <PyCall.jlwrap 0.0.3>}
```
Using the List() method will return all packages installed in the environment.
#### Switch(environment_name)
```python
>>> env.Switch("Julio")
Activating new environment at `~/Projects/TopLoader/Julio/Project.toml`
Environment created at /Julio

```
The Switch() method will switch virtual environments, and can also be used to load a new environment. That being said, for newly constructed types, you can either change the parameter to an existing environment, or simply use the provided load() function to construct an Environment type which will hold said Pkg environment.
#### Using(Package_Name)
```python
>>> lathe = env.Using("Lathe")
>>> lathe.stats.mean([5,10,15])
10.0
```
Using will import a package and return it, i.e. set it equal to something. Afterwards, you can and might as well access the package like you normally would.
# Full Example Session (Including Loading):
```python
>>> from TopLoader import Environment
TopLoader V 0.0.1
Happy Loading!
-----------------
>>> env = Environment("env")
Loading Package Manager
Pkg loaded
Activating new environment at `~/Projects/example_project/env/Project.toml`
Activated Package Environment: env
Environment available at: /env
>>> env.Add("Lathe")
  Updating registry at `~/.julia/registries/General`
  Updating git-repo `https://github.com/JuliaRegistries/General.git`
 Resolving package versions...
  Updating `~/Projects/example_project/env/Project.toml`
  [38d8eb38] + Lathe v0.0.3
  Updating `~/Projects/example_project/env/Manifest.toml`
  [324d7699] + CategoricalArrays v0.7.7
  [34da2185] + Compat v3.2.0
  [9a962f9c] + DataAPI v1.1.0
  [a93c6f00] + DataFrames v0.20.0
  [864edb3b] + DataStructures v0.17.9
  [e2d170a0] + DataValueInterfaces v1.0.0
  [41ab1584] + InvertedIndices v1.0.0
  [82899510] + IteratorInterfaceExtensions v1.0.0
  [682c06a0] + JSON v0.21.0
  [38d8eb38] + Lathe v0.0.3
  [e1d29d7a] + Missings v0.4.3
  [bac558e1] + OrderedCollections v1.1.0
  [69de0a69] + Parsers v0.3.10
  [2dfb63ee] + PooledArrays v0.5.3
  [189a3867] + Reexport v0.2.0
  [a2af1166] + SortingAlgorithms v0.3.1
  [3783bdb8] + TableTraits v1.0.0
  [bd369af6] + Tables v0.2.11
  [2a0f44e3] + Base64 
  [ade2ca70] + Dates 
  [8bb1440f] + DelimitedFiles 
  [8ba89e20] + Distributed 
  [9fa8497b] + Future 
  [b77e0a4c] + InteractiveUtils 
  [76f85450] + LibGit2 
  [8f399da3] + Libdl 
  [37e2e46d] + LinearAlgebra 
  [56ddb016] + Logging 
  [d6f4376e] + Markdown 
  [a63ad114] + Mmap 
  [44cfe95a] + Pkg 
  [de0858da] + Printf 
  [3fa0cd96] + REPL 
  [9a3f8284] + Random 
  [ea8e919c] + SHA 
  [9e88b42a] + Serialization 
  [1a1011a3] + SharedArrays 
  [6462fe0b] + Sockets 
  [2f01184e] + SparseArrays 
  [10745b16] + Statistics 
  [8dfed614] + Test 
  [cf7118a7] + UUIDs 
  [4ec0a83e] + Unicode 
>>> env.List()
{'Lathe': <PyCall.jlwrap 0.0.3>}
>>> env.Using("Lathe")
<module 'julia.Lathe' (<julia.core.JuliaModuleLoader object at 0x7fb6424a50d0>)>
>>> array = [5,10,15,20,25,30,35,40]
>>> lathe = env.Using("Lathe")
>>> mu = lathe.stats.mean(array)
>>> print(mu)
22.5
>>> env.Switch("SecondEnv")
Activating new environment at `~/Projects/example_project/SecondEnv/Project.toml`
Environment created at /SecondEnv
>>> env.List()
{}
>>> from TopLoader import Load
>>> environment = Load("env")
Loading file at: env
Loading Package Manager
Pkg loaded
Activating environment at `~/Projects/example_project/env/Project.toml`
Activated Package Environment: env
Environment available at: /env
Environment loaded!
{'Lathe': <PyCall.jlwrap 0.0.3>}
>>> environment.List()
{'Lathe': <PyCall.jlwrap 0.0.3>}
```
