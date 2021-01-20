import copy
import sys

from PyQt5 import QtWidgets

import controller
import data
from gui.interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clear_selected_button.clicked.connect(self.clear_selected)
        self.button_groups = {}
        self.controller = controller
        self.data = copy.deepcopy(data.data)
        self.set_up_gui_data()

    def get_predicted_result(self):
        category, label, result = self.controller.calculate(self.data)
        if category == 'error':
            result = {
                value: f'{str(round(probability * 100, 2))}%'
                for value, probability in
                result.items()
            }

            message = f'<p style="color:orange">Invalid option chosen.\n' \
                      f'The probability distribution for {label} is {result}</p>'
            return message

        if category == 'undefined':
            edible_probability = round(result['edible'] * 100, 2)
            message = f'<p style="color:orange">The class of this mushroom is unknown.\n' \
                      f'The probability of it being edible is {edible_probability}%</p>'
        else:
            color = 'green' if category == 'edible' else 'red'
            probability = round(result[category] * 100, 2)
            message = f'<p style="color:{color}">This mushroom is {category}. The probability is {probability}%.'

        return message

    def set_up_gui_data(self):
        self.button_groups = self.get_all_groups()
        for group in self.button_groups:
            buttons = group.buttons()
            self.button_groups[group]['values'] = []
            for i, button in enumerate(buttons):
                group.setId(button, i)
                self.button_groups[group]['values'].append(
                    button.objectName().split('_')[-1])
            group.buttonClicked.connect(self.update_predicted_result)

    def update_predicted_result(self):
        button_group = self.sender()
        clicked_button_id = button_group.checkedId()
        if clicked_button_id != -1:  # -1 means nothing was found:
            name = self.button_groups[button_group]['name']
            value = self.button_groups[button_group]['values'][clicked_button_id]
            self.data[name] = value
            result = self.get_predicted_result()
            self.ui.result_label.setText(result)
            # for el in self.data:  # for debugging purposes - print which radio buttons were selected
            #     print(el, self.data[el])
            # print('-------------------')

    def get_all_groups(self):
        """ Return all groups of radio boxes, ex. cap_shape_group, cap_surface_group, ..."""
        return {group: {'name': group.objectName().replace('_group', '')} for group
                in self.children() if type(group) == QtWidgets.QButtonGroup}

    def clear_selected(self):
        """ Clear all selected radio buttons """
        self.data = copy.deepcopy(data.data)
        self.ui.result_label.setText("")
        for group in self.button_groups:
            checked = group.checkedButton()
            if checked:
                group.setExclusive(False)
                checked.setChecked(False)
                group.setExclusive(True)


def main():
    network_controller = controller.Controller('./model/network_v1.xdsl')
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(network_controller)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
