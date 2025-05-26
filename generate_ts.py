# Let's import all the relevant libraries
from neurolib.models.hopf import HopfModel
import numpy as np
import matplotlib.pyplot as plt
from nilearn.connectome import ConnectivityMeasure

#### Model parameters Model A (find G):
#### Known parameters:
w = 0.7 * np.pi
Sigma_ou = 0.1
Cmat = np.array([[1, 0.02], [0.02, 1]])
Dmat = np.zeros((2,2))
Duration= 50
G = 1.2
# We import the model
model_a1 = HopfModel(Cmat=Cmat, Dmat=Dmat)
# intrinsic angular frequency of the oscillation (omega)
model_a1.params["seed"] = 42
model_a1.params['w'] = w
# set the noise here
model_a1.params['sigma_ou'] = Sigma_ou
# set the global coupling parameter G here
model_a1.params['K_gl'] = G
# duration of the simulation (in ms)
model_a1.params['duration'] = 50
# bifurcation parameter (we will disregard it for now)
model_a1.params['a'] = 0
model_a1.run()

np.save("model_A.npy", model_a1.x)
x = np.load("model_A.npy")
plt.plot(x.T)

#### Model parameters Model B (find w):

#### Known parameters:
w = 0.6
Sigma_ou = 0.1
Cmat = np.array([[1, 0.02], [0.02, 1]])
Dmat = np.zeros((2,2))
Duration= 50
G = 0.5
# We import the model
model_b = HopfModel(Cmat=Cmat, Dmat=Dmat)
# intrinsic angular frequency of the oscillation (omega)
model_b.params["seed"] = 42
model_b.params['w'] = w
# set the noise here
model_b.params['sigma_ou'] = Sigma_ou
# set the global coupling parameter G here
model_b.params['K_gl'] = G
# duration of the simulation (in ms)
model_b.params['duration'] = 50
# bifurcation parameter (we will disregard it for now)
model_b.params['a'] = 0
model_b.run()

np.save("model_B.npy", model_b.x)
x = np.load("model_B.npy")
plt.plot(x.T)

#### Model parameters Model C (find G matrix):

#### Known parameters:
w=  1.3 * np.pi
Cmat= np.array([[1.0, 0.02, 0.04, 0.05, 0.02], 
                [0.02, 1.0, 0.03, 0.01, 0.01],
                [0.02, 0.01, 1.0, 0.01, 0.04],
                [0.05, 0.01, 0.06, 1.0, 0.06],
                [0.07, 0.02, 0.03, 0.08, 1.0]])

Sigma_ou = 0.1
Dmat = np.zeros((5,5))
Duration= 50
G = 1.25
# We import the model
model_c = HopfModel(Cmat=Cmat, Dmat=Dmat)
# intrinsic angular frequency of the oscillation (omega)
model_c.params["seed"] = 42
model_c.params['w'] = w
# set the noise here
model_c.params['sigma_ou'] = Sigma_ou
# set the global coupling parameter G here
model_c.params['K_gl'] = G
# duration of the simulation (in ms)
model_c.params['duration'] = 50
# bifurcation parameter (we will disregard it for now)
model_c.params['a'] = 0
model_c.run()

np.save("model_C.npy", model_c.x)
x = np.load("model_C.npy")