import pandas
import os


def read_candidate_evaluation(generations=15):
    df = pandas.DataFrame(columns=["ID", "Fitness", "Generation"])
    for i in range(1, generations + 1):
        gen_path = os.getcwd() + "/../dataset/racing_evaluation_2convX305gens/generation_" + str(i) + ".csv"
        ndf = pandas.read_csv(gen_path, sep=" ", names=["ID", "Fitness"])
        ndf["Generation"] = i
        df = pandas.concat([df, ndf])

    return df;
