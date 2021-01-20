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
            self.net.set_evidence(mushroom_part, evidence)
        try:
            self.net.update_beliefs()
            edible, poisonous = self.net.get_node_value('Class')
            result = {
                'edible': edible,
                'poisonous': poisonous
            }
            if edible >= self.threshold:
                return ('edible', result)
            elif poisonous >= self.threshold:
                return ('poisonous', result)
            else:
                return ('undefined', result)
        except:
            return ('undefined', result)
        finally:
            self.net.clear_all_evidence()
