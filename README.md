# ITUFast

This is the repository for the Modern Artificial Intelligence project ITUFast, which aims to evolve a neural network that is capable of competing in a racing game. The project was developed by Winfried Baumann, Emilio Capo and David Oppenberg.

## Abstract

The task of image-input based game controllers has been popularized most notably by the paper ”Playing Atari with Deep Reinforcement Learning”, in which agents are trained to interpret an image input with Reinforcement Learning and stochastic gradient descend. Deep Neuroevolution has proven to be a competitive alternative to gradient-based training of Convolution Neural Networks, albeit only in the domain of 2D games. We therefore propose two image-based controllers exploiting two different CNN architectures, which have been trained with Deep Neuroevolution to navigate a virtual car in a 3D environment. The results show that, even if the agents did not manage to learn the task completely, this approach is promising when applied to moderate-size networks. However, there is large space for improvement, since our work was significantly limited by computational resources and time.

## Setup

1. Install version 4.21 of the Unreal Engine.
2. Make sure python3.6 is installed and the system variable `PYTHONHOME` is set to point to the python3.6 installation.
3. Clone this project with submodules: ``git clone --recurse-submodules git@github.itu.dk:wiba/itufast.git``
4. Download [the unreal python binaries](https://github.com/getnamo/UnrealEnginePython/releases) and unpack it into the project.
5. Generate and open the visual studio project and compile everything.
6. Open the project in the engine and wait until the dependencies are installed.

### Common Errors:

- If the project reports ``no module named tensorflow`` wait until it's automatically installed  
	**NOTE:** If it's not done installing after a few minutes. Open a console in ``UnrealRacing/Plugins/UnrealEnginePython/Binaries/Win64`` and install ``tensorflow`` and ``scipy`` but afterwards make sure to uninstall h5py (see next issue).
- If the project crashes after pressing play:  
Make sure h5py is **NOT** installed. See: [TF UE4 Plugin - Issue 35](https://github.com/getnamo/tensorflow-ue4/issues/35) for more information.

#### Saving Details:

- Candidate data is saved in C:/racing_evaluation/candidate_data, while results are saved in C:/racing_evaluation in .csv format.

- Candidate data will be loaded by the script if it is found, otherwise a new genome will be generated.
