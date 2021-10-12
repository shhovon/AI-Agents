import random

class Agent(object):
    def __init__(self):
        self.locationcondition = {'X': random.randint(0, 1), 'Y': random.randint(0, 1)}
        #history = random.choice(['lane-1','lane-2','lane-3'])
##        signal={"loc_A":random.choice(['Red','Green','Yellow','NoSignal']),
##                    "loc_B":random.choice(['Red','Green','Yellow','NoSignal']),
##                    "loc_C":random.choice(['Red','Green','Yellow','NoSignal']),
##                    "loc_D":random.choice(['Red','Green','Yellow','NoSignal'])}
        history = []

class ModelAgent(Agent):
    def __init__(self, env):
        Roadlocation = 1
        
        if Roadlocation == 0:
            print("Car is randomly placed at Lane X")
            #   1 = car ahead
            if env.locationcondition['X'] == 1:
                print("There is another car infront of us at Lane X")
                #env.locationcondition['X'] = history[0]
                env.locationcondition['X'] == 0
                print("Car stopped at Lane X..")
                print("-->moving to Lane Y")
                if env.locationcondition['Y'] == 1:
                    print("There is another car infront of us at Lane Y")
                    env.locationcondition['y'] == 0
                    print("Car stopped at Lane Y..")
                else:
                    print("Car stopped at Lane Y..")
            else:
                #   0 = no car ahead
                print("Lane X is clear, Our car is moving forward to Lane Y")
                if env.locationcondition['Y'] == 1:
                    print("There is another car infront of us at Lane Y")
                    env.locationcondition['Y'] == 0
                    print("Car stopped at Lane Y..")
                else:
                    print("Car stopped at Lane Y..")

        elif Roadlocation == 1:
            print("Car is randomly placed at Lane Y")
            if env.locationcondition['Y'] == 1:
                print("There is a car infront of us at Lane Y")
                env.locationcondition['Y'] == 0
                print("Car stopped at Lane Y..")
                print("-->moving to Lane X")
                if env.locationcondition['X'] == 1:
                    print("There is another car infront of us at Lane X")
                    env.locationcondition['X'] == 0
                    print("Car stopped at Lane X..")
                else:
                    print("Car stopped at Lane X")
            else:
                print("Lane Y is clear, Our car is moving forward to Lane X")
                if env.locationcondition['X'] == 1:
                    print("There is another car infront of us at Lane X")
                    env.locationcondition['X'] == 0
                    print("Car stopped at Lane X..")
                else:
                    print("Car stopped at Lane X..")
    
env = Agent()
lane = ModelAgent(env)
