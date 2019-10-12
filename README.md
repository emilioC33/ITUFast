# itufast

This is the repository for the Modern AI project ITUFast which aims to evolve a neuronal network that is capable of competing in a racing game.

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