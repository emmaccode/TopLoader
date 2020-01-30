<div align="center"><img src="https://github.com/emmettgb/TopLoader/blob/0.0.1/toploader.jpg" width="300" /><h1>TopLoader</h1></div>



#### Easily Manage Julia Environments From Python
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
The Switch() method will create switch virtual environments, and can also be used to load a new environment. That being said, for newly constructed types, you can either change the parameter to an existing environment, or simply use the provided load() function to construct an Environment type which will hold said Pkg environment.
#### Using(Package_Name)
```python
>>> lathe = env.Using("Lathe")
>>> lathe.stats.mean([5,10,15])
10.0
```
Using will import a package and return it, i.e. set it equal to something. Afterwards, you can and might as well access the package like you normally would.
