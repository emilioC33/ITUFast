import tensorflow as tf
import unreal_engine as ue
from TFPluginAPI import TFPluginAPI
from tensorflow.keras import layers
from tensorflow.keras import models
import os, shutil
import re
import tensorflow as tf
import scipy
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras import backend as K
import random
from pathlib import Path


class TFRacingAI(TFPluginAPI):

    # initialize the vectors + weights or load them from a file if the id is already used
    def __init__(self):
        self.savepath = os.path.join("C:\\racing_evaluation\\candidate_data")

        # Model variables
        self.architecture = "B" # Change this value to "A" or "B" to try the related architecture
        self.model = None
        self.graph = None

        # Buffer management variables
        self.backup_images = []
        self.init = True

        if not os.path.exists(self.savepath):
                os.makedirs(self.savepath)

    def create_model(self):
        init_mean = 0
        init_stddev = 0.05
        init_seed = None
        self.model = tf.keras.Sequential()
        
        if self.architecture == "A":
            self.model.add(tf.keras.layers.Conv2D(64, kernel_size=8, activation="relu", input_shape=(64, 64, 1), strides=1,
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="conv1"))
            self.model.add(tf.keras.layers.Conv2D(32, kernel_size=8, activation="relu", strides=1,
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="conv2"))
            self.model.add(tf.keras.layers.Flatten(name="flat"))
            self.model.add(tf.keras.layers.Dense(5, activation="sigmoid",
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="output"))
            
        else: # Architecture "B"
            self.model.add(tf.keras.layers.Conv2D(32, kernel_size=8, activation="relu", input_shape=(64, 64, 4), strides=4,
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="conv1"))
            self.model.add(tf.keras.layers.Conv2D(64, kernel_size=4, activation="relu", strides=2,
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="conv2"))
            self.model.add(tf.keras.layers.Conv2D(64, kernel_size=3, activation="relu", strides=1,
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="conv3"))
            self.model.add(tf.keras.layers.Flatten(name="flat"))
            self.model.add(tf.keras.layers.Dense(512, activation="relu",
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="dense"))
            self.model.add(tf.keras.layers.Dense(5, activation="sigmoid",
                           kernel_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed),
                           bias_initializer=keras.initializers.TruncatedNormal(mean=init_mean, stddev=init_stddev, seed=init_seed), name="output"))

        self.graph = tf.get_default_graph()
        self.model.summary()

    def save(self, genome_id):
        for layer in self.model.layers:

            if layer.name != "flat":

                weights = np.array(layer.get_weights())

                filename = genome_id + "_" + layer.name + ".npy"
                np.save(os.path.join(self.savepath, filename), weights)

    def load(self, genome_id):
        for layer in self.model.layers:

            if layer.name != "flat":

                filename = genome_id + "_" + layer.name + ".npy"
                weights = np.array(np.load(os.path.join(self.savepath, filename)))
                layer.set_weights(weights)

    def randomize_weights(self):
        session = K.get_session()
        for layer in self.model.layers:
            if layer != "flat":
                for v in layer.__dict__:
                    v_arg = getattr(layer, v)
                    if hasattr(v_arg, 'initializer'):
                        initializer_method = getattr(v_arg, 'initializer')
                        initializer_method.run(session=session)


    def initialize(self, genome_id):
        self.genome_id = genome_id
        self.init = True
        
        if self.model is None:
            self.create_model()
        
        # If there's a network with that genome_id, load it (checking output to avoid loading incomplete genome data)
        if os.path.exists(os.path.join(self.savepath, str(genome_id) + "_output.npy")):
            print("Now evaluating candidate " + genome_id + ".")
            self.load(genome_id)

        # Otherwise generate a new set of weights for the network
        else:
            print("Now generating and evaluating candidate " + genome_id + ".")
            self.randomize_weights()
            self.save(genome_id)


    # add noise to existing filters and weights
    def mutate(self, parent_genome_id):
        print("Now mutating using parent genomeID: " + parent_genome_id + " - current genomeID: " + self.genome_id + ".")

        if self.model is None:
            self.create_model()

        self.load(parent_genome_id)

        for layer in self.model.layers:

            if layer.name != "flat":

                weights = np.array(layer.get_weights())

                l_w = weights[0]
                l_b = weights[1]
                rd_w = np.random.normal(loc=0, size=l_w.shape, scale=0.005)
                rd_b = np.random.normal(loc=0, size=l_b.shape, scale=0.005)
                new_weights = np.add(rd_w, l_w)
                new_bias = np.add(rd_b, l_b)

                layer.set_weights([new_weights,new_bias])

        self.save(self.genome_id)

    # expected optional api: setup your model for training
    def onSetup(self):
        pass

    def updateImagesBackup(self, img):
        self.backup_images.append(img)
        self.backup_images.pop(0)

    # expected optional api: parse input object and return a result object, which will be converted to json for UE4
    def onJsonInput(self, jsonInput):
        # Process jsonInput
        img = np.array(jsonInput['TFData']['pixels'], dtype="float32")

        if self.architecture == "B":
            img = img.reshape((-1, 64, 64, 1))
            
        else: # Architecture A
            # If first prediction for current agent, initialize buffer
            if self.init:
                self.backup_images = [img, img, img, img]
                self.init = False
            
            # Update buffer with received input
            self.updateImagesBackup(img)

            # Shape buffer to feed the network
            img = np.array(self.backup_images)
            img = img.reshape((-1, 64, 64, 4))

        
        
        # Make the prediction for this timestep
        with self.graph.as_default():
            prediction = self.model.predict(img)[0]

        ### Predicting DIRECTION ###
        right = prediction[0]
        left = prediction[1]

        # Assume no steering
        direction = 0 

        if right >= left and right > 0.5:
            direction = 1

        if left > right and left > 0.5:
            direction = -1


        ### Predicting MOTION ###
        acc = prediction[2]
        brk = prediction[3]

        # Assume no motion
        motion = 0 

        if acc >= brk and acc > 0.5:
            motion = 1

        if brk > acc and brk > 0.5:
            motion = -1


        ### Predicting HANDBREAK PULLING ###
        hbrk = False
        
        if prediction[4] > 0.5:
            hbrk = True
        
        result = {
            'right': direction,
            'acceleration': motion,
            'handbreakPulled': hbrk
        }
        
        return result

    # expected optional api: start training your network
    def onBeginTraining(self):
        pass

def getApi():
    return TFRacingAI.getInstance()
