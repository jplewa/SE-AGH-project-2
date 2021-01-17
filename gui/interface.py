# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(832, 874)
        MainWindow.setMinimumSize(QtCore.QSize(832, 874))
        MainWindow.setMaximumSize(QtCore.QSize(832, 874))
        MainWindow.setStyleSheet("background-color: white;\n"
"color: black;")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 215, 611, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.cap_shape_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.cap_shape_layout.setContentsMargins(0, 0, 0, 0)
        self.cap_shape_layout.setObjectName("cap_shape_layout")
        self.cap_shape_flat = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.cap_shape_flat.setObjectName("cap_shape_flat")
        self.cap_shape_group = QtWidgets.QButtonGroup(MainWindow)
        self.cap_shape_group.setObjectName("cap_shape_group")
        self.cap_shape_group.addButton(self.cap_shape_flat, 1)
        self.cap_shape_layout.addWidget(self.cap_shape_flat)
        self.cap_shape_bell = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.cap_shape_bell.setObjectName("cap_shape_bell")
        self.cap_shape_group.addButton(self.cap_shape_bell, 2)
        self.cap_shape_layout.addWidget(self.cap_shape_bell)
        self.cap_shape_convex = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.cap_shape_convex.setObjectName("cap_shape_convex")
        self.cap_shape_group.addButton(self.cap_shape_convex, 3)
        self.cap_shape_layout.addWidget(self.cap_shape_convex)
        self.cap_shape_conical = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.cap_shape_conical.setObjectName("cap_shape_conical")
        self.cap_shape_group.addButton(self.cap_shape_conical, 4)
        self.cap_shape_layout.addWidget(self.cap_shape_conical)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 195, 611, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 215, 31, 31))
        self.label_2.setStyleSheet("image: url(:/cap-shape-bell/img/cap-shape-bell.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 265, 611, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 285, 611, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.cap_surface_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.cap_surface_layout.setContentsMargins(0, 0, 0, 0)
        self.cap_surface_layout.setObjectName("cap_surface_layout")
        self.cap_surface_scaly = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.cap_surface_scaly.setObjectName("cap_surface_scaly")
        self.cap_surface_group = QtWidgets.QButtonGroup(MainWindow)
        self.cap_surface_group.setObjectName("cap_surface_group")
        self.cap_surface_group.addButton(self.cap_surface_scaly, 1)
        self.cap_surface_layout.addWidget(self.cap_surface_scaly)
        self.cap_surface_smooth = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.cap_surface_smooth.setObjectName("cap_surface_smooth")
        self.cap_surface_group.addButton(self.cap_surface_smooth, 2)
        self.cap_surface_layout.addWidget(self.cap_surface_smooth)
        self.cap_surface_fibrous = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.cap_surface_fibrous.setObjectName("cap_surface_fibrous")
        self.cap_surface_group.addButton(self.cap_surface_fibrous, 3)
        self.cap_surface_layout.addWidget(self.cap_surface_fibrous)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.cap_surface_layout.addWidget(self.label_22)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 285, 31, 31))
        self.label_5.setStyleSheet("image: url(:/cap-surface-smooth/img/cap-surface-smooth.png)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 400, 611, 16))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(110, 420, 611, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.stalk_root_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.stalk_root_layout.setContentsMargins(0, 0, 0, 0)
        self.stalk_root_layout.setObjectName("stalk_root_layout")
        self.stalk_root_bulbous = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.stalk_root_bulbous.setObjectName("stalk_root_bulbous")
        self.stalk_root_group = QtWidgets.QButtonGroup(MainWindow)
        self.stalk_root_group.setObjectName("stalk_root_group")
        self.stalk_root_group.addButton(self.stalk_root_bulbous, 1)
        self.stalk_root_layout.addWidget(self.stalk_root_bulbous)
        self.stalk_root_club = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.stalk_root_club.setObjectName("stalk_root_club")
        self.stalk_root_group.addButton(self.stalk_root_club, 2)
        self.stalk_root_layout.addWidget(self.stalk_root_club)
        self.stalk_root_equal = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.stalk_root_equal.setObjectName("stalk_root_equal")
        self.stalk_root_group.addButton(self.stalk_root_equal, 3)
        self.stalk_root_layout.addWidget(self.stalk_root_equal)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.stalk_root_layout.addWidget(self.label_23)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 420, 31, 31))
        self.label_7.setStyleSheet("image: url(:/stalk-root-club/img/stalk-root-club.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 610, 611, 16))
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(110, 630, 611, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.gill_spacing_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.gill_spacing_layout.setContentsMargins(0, 0, 0, 0)
        self.gill_spacing_layout.setObjectName("gill_spacing_layout")
        self.gill_spacing_close = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.gill_spacing_close.setObjectName("gill_spacing_close")
        self.gill_spacing_group = QtWidgets.QButtonGroup(MainWindow)
        self.gill_spacing_group.setObjectName("gill_spacing_group")
        self.gill_spacing_group.addButton(self.gill_spacing_close, 1)
        self.gill_spacing_layout.addWidget(self.gill_spacing_close)
        self.gill_spacing_crowded = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.gill_spacing_crowded.setObjectName("gill_spacing_crowded")
        self.gill_spacing_group.addButton(self.gill_spacing_crowded, 2)
        self.gill_spacing_layout.addWidget(self.gill_spacing_crowded)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gill_spacing_layout.addWidget(self.label_25)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gill_spacing_layout.addWidget(self.label_24)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 630, 31, 31))
        self.label_9.setStyleSheet("image: url(:/gill-spacing-crowded/img/gill-spacing-crowded.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 335, 611, 16))
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(110, 355, 611, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.cap_color_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.cap_color_layout.setContentsMargins(0, 0, 0, 0)
        self.cap_color_layout.setObjectName("cap_color_layout")
        self.cap_color_white = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.cap_color_white.setObjectName("cap_color_white")
        self.cap_color_group = QtWidgets.QButtonGroup(MainWindow)
        self.cap_color_group.setObjectName("cap_color_group")
        self.cap_color_group.addButton(self.cap_color_white, 1)
        self.cap_color_layout.addWidget(self.cap_color_white)
        self.cap_color_pink = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.cap_color_pink.setObjectName("cap_color_pink")
        self.cap_color_group.addButton(self.cap_color_pink, 2)
        self.cap_color_layout.addWidget(self.cap_color_pink)
        self.cap_color_brown = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.cap_color_brown.setObjectName("cap_color_brown")
        self.cap_color_group.addButton(self.cap_color_brown, 3)
        self.cap_color_layout.addWidget(self.cap_color_brown)
        self.label_35 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.cap_color_layout.addWidget(self.label_35)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 630, 31, 31))
        self.label_11.setStyleSheet("image: url(:/gill-spacing-close/img/gill-spacing-close.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 125, 611, 16))
        self.label_12.setObjectName("label_12")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(110, 145, 611, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.bruises_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.bruises_layout.setContentsMargins(0, 0, 0, 0)
        self.bruises_layout.setObjectName("bruises_layout")
        self.bruises_false = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.bruises_false.setChecked(True)
        self.bruises_false.setObjectName("bruises_false")
        self.bruises_group = QtWidgets.QButtonGroup(MainWindow)
        self.bruises_group.setObjectName("bruises_group")
        self.bruises_group.addButton(self.bruises_false, 1)
        self.bruises_layout.addWidget(self.bruises_false)
        self.bruises_true = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.bruises_true.setChecked(False)
        self.bruises_true.setObjectName("bruises_true")
        self.bruises_group.addButton(self.bruises_true, 2)
        self.bruises_layout.addWidget(self.bruises_true)
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.bruises_layout.addWidget(self.label_32)
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.bruises_layout.addWidget(self.label_31)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(190, 215, 31, 31))
        self.label_13.setStyleSheet("image: url(:/cap-shape-flat/img/cap-shape-flat.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(110, 470, 611, 16))
        self.label_14.setObjectName("label_14")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(110, 490, 611, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.stalk_color_above_ring_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.stalk_color_above_ring_layout.setContentsMargins(0, 0, 0, 0)
        self.stalk_color_above_ring_layout.setObjectName("stalk_color_above_ring_layout")
        self.stalk_color_above_ring_white = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.stalk_color_above_ring_white.setObjectName("stalk_color_above_ring_white")
        self.stalk_color_above_ring_group = QtWidgets.QButtonGroup(MainWindow)
        self.stalk_color_above_ring_group.setObjectName("stalk_color_above_ring_group")
        self.stalk_color_above_ring_group.addButton(self.stalk_color_above_ring_white, 1)
        self.stalk_color_above_ring_layout.addWidget(self.stalk_color_above_ring_white)
        self.stalk_color_above_ring_red = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        self.stalk_color_above_ring_red.setObjectName("stalk_color_above_ring_red")
        self.stalk_color_above_ring_group.addButton(self.stalk_color_above_ring_red, 2)
        self.stalk_color_above_ring_layout.addWidget(self.stalk_color_above_ring_red)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.stalk_color_above_ring_layout.addWidget(self.label_28)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.stalk_color_above_ring_layout.addWidget(self.label_27)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(190, 420, 31, 31))
        self.label_15.setStyleSheet("image: url(:/stalk-root-bulbous/img/stalk-root-bulbous.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(110, 540, 611, 16))
        self.label_16.setObjectName("label_16")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(110, 560, 611, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.stalk_color_below_ring_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.stalk_color_below_ring_layout.setContentsMargins(0, 0, 0, 0)
        self.stalk_color_below_ring_layout.setObjectName("stalk_color_below_ring_layout")
        self.stalk_color_below_ring_white = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.stalk_color_below_ring_white.setObjectName("stalk_color_below_ring_white")
        self.stalk_color_below_ring_group = QtWidgets.QButtonGroup(MainWindow)
        self.stalk_color_below_ring_group.setObjectName("stalk_color_below_ring_group")
        self.stalk_color_below_ring_group.addButton(self.stalk_color_below_ring_white, 1)
        self.stalk_color_below_ring_layout.addWidget(self.stalk_color_below_ring_white)
        self.stalk_color_below_ring_red = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        self.stalk_color_below_ring_red.setObjectName("stalk_color_below_ring_red")
        self.stalk_color_below_ring_group.addButton(self.stalk_color_below_ring_red, 2)
        self.stalk_color_below_ring_layout.addWidget(self.stalk_color_below_ring_red)
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.stalk_color_below_ring_layout.addWidget(self.label_30)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.stalk_color_below_ring_layout.addWidget(self.label_29)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(190, 285, 31, 31))
        self.label_17.setStyleSheet("image: url(:/cap-surface-scaly/img/cap-sufrce-scaly.png);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(110, 680, 611, 16))
        self.label_18.setObjectName("label_18")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(110, 700, 611, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.ring_number_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.ring_number_layout.setContentsMargins(0, 0, 0, 0)
        self.ring_number_layout.setObjectName("ring_number_layout")
        self.ring_number_none = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.ring_number_none.setObjectName("ring_number_none")
        self.ring_number_group = QtWidgets.QButtonGroup(MainWindow)
        self.ring_number_group.setObjectName("ring_number_group")
        self.ring_number_group.addButton(self.ring_number_none, 1)
        self.ring_number_layout.addWidget(self.ring_number_none)
        self.ring_number_one = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.ring_number_one.setObjectName("ring_number_one")
        self.ring_number_group.addButton(self.ring_number_one, 2)
        self.ring_number_layout.addWidget(self.ring_number_one)
        self.ring_number_two = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.ring_number_two.setObjectName("ring_number_two")
        self.ring_number_group.addButton(self.ring_number_two, 3)
        self.ring_number_layout.addWidget(self.ring_number_two)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.ring_number_layout.addWidget(self.label_26)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(110, 750, 611, 16))
        self.label_20.setObjectName("label_20")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(110, 770, 611, 31))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.veil_color_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.veil_color_layout.setContentsMargins(0, 0, 0, 0)
        self.veil_color_layout.setObjectName("veil_color_layout")
        self.veil_color_white = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.veil_color_white.setObjectName("veil_color_white")
        self.veil_color_group = QtWidgets.QButtonGroup(MainWindow)
        self.veil_color_group.setObjectName("veil_color_group")
        self.veil_color_group.addButton(self.veil_color_white, 1)
        self.veil_color_layout.addWidget(self.veil_color_white)
        self.veil_color_yellow = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.veil_color_yellow.setObjectName("veil_color_yellow")
        self.veil_color_group.addButton(self.veil_color_yellow, 2)
        self.veil_color_layout.addWidget(self.veil_color_yellow)
        self.veil_color_orange = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.veil_color_orange.setObjectName("veil_color_orange")
        self.veil_color_group.addButton(self.veil_color_orange, 3)
        self.veil_color_layout.addWidget(self.veil_color_orange)
        self.veil_color_brown = QtWidgets.QRadioButton(self.horizontalLayoutWidget_10)
        self.veil_color_brown.setObjectName("veil_color_brown")
        self.veil_color_group.addButton(self.veil_color_brown, 4)
        self.veil_color_layout.addWidget(self.veil_color_brown)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(500, 285, 31, 31))
        self.label_19.setStyleSheet("image: url(:/cap-surface-fibrous/img/cap-surface-fibrous.png)")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(500, 420, 31, 31))
        self.label_21.setStyleSheet("image: url(:/stalk-root-equal/img/stalk-root-equal.png);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(640, 215, 31, 31))
        self.label_33.setStyleSheet("image: url(:/cap-shape-conical/img/cap-shape-conical.png);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(500, 215, 31, 31))
        self.label_34.setStyleSheet("image: url(:/cap-shape-convex/img/cap-shape-convex.png);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.is_edible_button = QtWidgets.QPushButton(self.centralwidget)
        self.is_edible_button.setGeometry(QtCore.QRect(320, 810, 181, 32))
        self.is_edible_button.setStyleSheet("background-color: rgba(46, 204, 113, 0.4);")
        self.is_edible_button.setAutoDefault(False)
        self.is_edible_button.setDefault(False)
        self.is_edible_button.setFlat(False)
        self.is_edible_button.setObjectName("is_edible_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 611, 81))
        self.label_3.setStyleSheet("background-color: rgba(46, 204, 113, 0.4);")
        self.label_3.setObjectName("label_3")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(170, 125, 551, 20))
        self.label_36.setObjectName("label_36")
        self.clear_selected_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_selected_button.setGeometry(QtCore.QRect(590, 110, 131, 21))
        self.clear_selected_button.setStyleSheet("background-color: rgb(211,211,211);")
        self.clear_selected_button.setAutoDefault(False)
        self.clear_selected_button.setDefault(False)
        self.clear_selected_button.setFlat(False)
        self.clear_selected_button.setObjectName("clear_selected_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cap_shape_flat.setText(_translate("MainWindow", "flat"))
        self.cap_shape_bell.setText(_translate("MainWindow", "bell"))
        self.cap_shape_convex.setText(_translate("MainWindow", "convex"))
        self.cap_shape_conical.setText(_translate("MainWindow", "conical"))
        self.label.setText(_translate("MainWindow", "CAP SHAPE"))
        self.label_4.setText(_translate("MainWindow", "CAP SURFACE"))
        self.cap_surface_scaly.setText(_translate("MainWindow", "scaly"))
        self.cap_surface_smooth.setText(_translate("MainWindow", "smooth"))
        self.cap_surface_fibrous.setText(_translate("MainWindow", "fibrous"))
        self.label_6.setText(_translate("MainWindow", "STALK ROOT"))
        self.stalk_root_bulbous.setText(_translate("MainWindow", "bulbous"))
        self.stalk_root_club.setText(_translate("MainWindow", "club"))
        self.stalk_root_equal.setText(_translate("MainWindow", "equal"))
        self.label_8.setText(_translate("MainWindow", "GILL SPACING"))
        self.gill_spacing_close.setText(_translate("MainWindow", "close"))
        self.gill_spacing_crowded.setText(_translate("MainWindow", "crowded"))
        self.label_10.setText(_translate("MainWindow", "CAP COLOR"))
        self.cap_color_white.setText(_translate("MainWindow", "white"))
        self.cap_color_pink.setText(_translate("MainWindow", "pink"))
        self.cap_color_brown.setText(_translate("MainWindow", "brown"))
        self.label_12.setText(_translate("MainWindow", "BRUISES"))
        self.bruises_false.setText(_translate("MainWindow", "false"))
        self.bruises_true.setText(_translate("MainWindow", "true"))
        self.label_14.setText(_translate("MainWindow", "STALK COLOR ABOVE RING"))
        self.stalk_color_above_ring_white.setText(_translate("MainWindow", "white"))
        self.stalk_color_above_ring_red.setText(_translate("MainWindow", "red"))
        self.label_16.setText(_translate("MainWindow", "STALK COLOR BELOW RING"))
        self.stalk_color_below_ring_white.setText(_translate("MainWindow", "white"))
        self.stalk_color_below_ring_red.setText(_translate("MainWindow", "red"))
        self.label_18.setText(_translate("MainWindow", "RING NUMBER"))
        self.ring_number_none.setText(_translate("MainWindow", "none"))
        self.ring_number_one.setText(_translate("MainWindow", "one"))
        self.ring_number_two.setText(_translate("MainWindow", "two"))
        self.label_20.setText(_translate("MainWindow", "VEIL COLOR"))
        self.veil_color_white.setText(_translate("MainWindow", "white"))
        self.veil_color_yellow.setText(_translate("MainWindow", "yellow"))
        self.veil_color_orange.setText(_translate("MainWindow", "orange"))
        self.veil_color_brown.setText(_translate("MainWindow", "brown"))
        self.is_edible_button.setText(_translate("MainWindow", "Is this mushroom edible?"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">MUSHROOMS</span></p><p align=\"center\"><span style=\" font-weight:600;\">CHECK IF THE MUSHROOM IS EDIBLE</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#595959;\">MANDATORY FIELD</span></p></body></html>"))
        self.clear_selected_button.setText(_translate("MainWindow", "Clear selected"))
import gui.mushroom_attributes_rc