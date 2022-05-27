import yarp
from time import sleep
import numpy as np

class FingertipUtils:

    def __init__(self, id_list):
        while not yarp.Network.checkNetwork():
            print("YARP network is not up. Checking again in 2 seconds.")
            sleep(2)

        yarp.Network.init()
        self.id_list = id_list
        self.fingertip_stream = yarp.BufferedPortVector()

    def start(self):
        # setting up connection for recieving data from the fingertip
        self.fingertip_stream.open("/fingertip_input:o")
        yarp.NetworkBase.connect(
            "/SkinFingertipDemo/skin/fingertip", "/fingertip_input:o")
        if not yarp.NetworkBase.connect("/SkinFingertipDemo/skin/fingertip", "/fingertip_input:o"):
            print("Failed to connect to yarp port for fingertip input")
            return False  # break
        return True

    def yarp_vector_to_numpy(self, vector):
        return np.array([vector[i] for i in range(vector.size())])

    def get_taxel_values(self):
        return 255 - self.yarp_vector_to_numpy(self.fingertip_stream.read())[self.id_list]