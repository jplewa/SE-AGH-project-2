import copy
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import controller
import data
from gui.interface import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controller, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.is_edible_button.clicked.connect(self.is_edible_button_clicked)
        self.ui.clear_selected_button.clicked.connect(self.clear_selected)
        self.button_groups = {}
        self.controller = controller
        self.data = {}
        self.set_up_gui_data()

    def is_edible_button_clicked(self):
        self.data = copy.deepcopy(data.data)
        self.check_values()
        category, result = self.controller.calculate(self.data)
        if category == 'undefined':
            edible_probability = round(result['edible'] * 100, 2)
            QMessageBox.about(
                self,
                'Info',
                f'The class of this mushroom is unknown.\nThe probability of it being edible is {edible_probability}%.'
            )
        else:
            probability = round(result[category] * 100, 2)
            QMessageBox.about(
                self,
                'Info',
                f'This mushroom is {category}.\nThe probability is {probability}%.'
            )

    def set_up_gui_data(self):
        self.button_groups = self.get_all_groups()
        for group in self.button_groups:
            buttons = group.buttons()
            self.button_groups[group]['values'] = []
            for i, button in enumerate(buttons):
                group.setId(button, i)
                self.button_groups[group]['values'].append(button.objectName().split('_')[-1])

    def get_all_groups(self):
        """ Return all groups of radio boxes, ex. cap_shape_group, cap_surface_group, ..."""
        return {group: {'name': group.objectName().replace('_group', '')} for group
                in self.children() if type(group) == QtWidgets.QButtonGroup}

    def clear_selected(self):
        """ Clear all selected radio button"""
        for group in self.button_groups:
            checked = group.checkedButton()
            if checked:
                group.setExclusive(False)
                checked.setChecked(False)
                group.setExclusive(True)

    def check_values(self):
        """Assign values from slected radio buttons"""
        for group in self.button_groups:
            id = group.checkedId()
            if id != -1:  # -1 means nothing was found:
                name = self.button_groups[group]['name']
                value = self.button_groups[group]['values'][id]
                self.data[name] = value
        # for el in self.data:  # for debugging purposes - print which radio buttons were selected
        #     print(el, self.data[el])
        # print('-------------------')


def main():
    network_controller = controller.Controller('./model/network_v1.xdsl')
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(network_controller)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
