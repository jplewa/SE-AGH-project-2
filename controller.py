import data as parameters

import pysmile
import pysmile_license


class Controller:
    def __init__(self, model_path, threshold=0.95):
        self.net = pysmile.Network()
        self.net.read_file(model_path)
        self.threshold = threshold

    def calculate(self, data):
        for mushroom_part, evidence in data.items():
            if evidence is None:
                continue
            if mushroom_part == 'bruises':
                evidence = evidence == 'True'
            try:
                self.net.set_evidence(mushroom_part, evidence)
            except:
                self.net.update_beliefs()
                results = {
                    value: probability
                    for value, probability
                    in zip(
                        parameters.parameters[mushroom_part],
                        self.net.get_node_value(mushroom_part)
                    )
                }
                return ('error', mushroom_part, results)
        try:
            self.net.update_beliefs()
            edible, poisonous = self.net.get_node_value('Class')
            result = {
                'edible': edible,
                'poisonous': poisonous
            }
            if edible >= self.threshold:
                return ('edible', 'Class', result)
            elif poisonous >= self.threshold:
                return ('poisonous', 'Class', result)
            else:
                return ('undefined', 'Class', result)
        except:
            return ('undefined', 'Class', result)
        finally:
            self.net.clear_all_evidence()
