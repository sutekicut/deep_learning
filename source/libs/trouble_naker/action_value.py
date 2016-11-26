from collections import defaultdict
from trouble_naker import TroubleNaker

class ActionValue:
    def __init__(self):
        self.value = {}

        for q in TroubleNaker.Questions:
            self.value[q] = {}
            for a in TroubleNaker.Answers:
                self.value[q][a] = {}
                for t in TroubleNaker.Troubles:
                    self.value[q][a][t] = {}


if __name__ == '__main__':
    value = ActionValue()
    print(value.value)
    print("test")