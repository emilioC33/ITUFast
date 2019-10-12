import plot as p
import dataset.dataset as ds
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

# LOADING DATAFRAME #
num_gen = 305
df = ds.read_candidate_evaluation(num_gen)

# RETRIEVING ELITE FOR EACH GENERATION #
dfelite = pd.DataFrame()
for gen in range(1, num_gen+1):
    dftmp = df[df["Generation"]==gen]
    dftmp = dftmp.sort_values(by="Fitness")
    dftmp = dftmp.tail(30)
    dfelite = pd.concat([dfelite, dftmp])

# PLOTTING THE DATAFRAME #
b = sb.boxplot(x="Generation", y="Fitness", data=dfelite, color="skyblue")
b.axes.set_title("Elite Evolution for Architecture A",fontsize=30)
fig = plt.gcf()
fig.set_size_inches(18, 9)
plt.xticks([0, 50, 100, 150, 200, 250, 300], [0, 50, 100, 150, 200, 250, 300])
b.set_xlabel("Generation", fontsize=20)
b.set_ylabel("Fitness", fontsize=20)
b.tick_params(labelsize=10)
plt.savefig(fname="plot_2convX305gens.eps", quality=95, dpi=1000)
plt.show()
