from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 850)
        # MainWindow.setStyleSheet("")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#2c3a41;")
        self.centralwidget.setObjectName("centralwidget")

        # Set up layouts and widgets
        self.setup_image_layouts()
        self.setup_sidebar_1()
        self.setup_buttons()
        self.setup_sidebar_3()
        self.setup_sidebar_2()

        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar and Status Bar
        self.setup_menu_and_status_bar(MainWindow)

        # Retranslate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_image_layouts(self):
        """Set up the layout for displaying original and processed images."""
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 190, 1000, 530))
        self.layoutWidget.setObjectName("layoutWidget")

        self.images_layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.images_layout.setContentsMargins(20, 0, 20, 0)
        self.images_layout.setObjectName("images_layout")

        # Original Image GroupBox
        self.original_image_groupbox = QtWidgets.QGroupBox(self.layoutWidget)
        self.original_image_groupbox.setStyleSheet("QGroupBox{ color: rgb(255, 255, 255); }")
        self.original_image_groupbox.setObjectName("original_image_groupbox")
        self.images_layout.addWidget(self.original_image_groupbox)

        # Processed Image GroupBox
        self.processed_image_groupbox = QtWidgets.QGroupBox(self.layoutWidget)
        self.processed_image_groupbox.setStyleSheet("QGroupBox{ color: rgb(255, 255, 255); }")
        self.processed_image_groupbox.setObjectName("processed_image_groupbox")
        self.images_layout.addWidget(self.processed_image_groupbox)

    def setup_sidebar_1(self):
        """Set up the first sidebar with buttons."""
        self.sidebar_1_layout = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_1_layout.setGeometry(QtCore.QRect(20, 130, 261, 600))
        self.sidebar_1_layout.setObjectName("sidebar_1_layout")

        self.side_bar_1 = QtWidgets.QVBoxLayout(self.sidebar_1_layout)
        self.side_bar_1.setContentsMargins(0, 0, 0, 0)
        self.side_bar_1.setObjectName("side_bar_1")

        # Edge Detection Button
        self.edge_detection_button = self.create_button(
            "Edge Detection", self.sidebar_1_layout, "edge_detection_button",
            minimum_size=(200, 40),  # Set minimum size (width, height)
            maximum_size=(240, 45)  # Set maximum size (width, height)
        )
        self.side_bar_1.addWidget(self.edge_detection_button)

        # Object Contour Button
        self.object_contour_button = self.create_button(
            "Object Contour", self.sidebar_1_layout, "object_contour_button",
            minimum_size=(200, 40),  # Set minimum size (width, height)
            maximum_size=(240, 45)  # Set maximum size (width, height)
        )
        self.side_bar_1.addWidget(self.object_contour_button)

    def setup_buttons(self):
        """Set up buttons in the central widget."""
        # Back Button
        self.back_button = self.create_button(
            "⇦", self.centralwidget, "back_button", geometry=QtCore.QRect(20, 30, 50, 50),
            font_size=40, font_family="Hiragino Sans GB", hover_color="rgb(253, 94, 80)"
        )

        # Save Button
        self.save_button = self.create_button(
            "Save", self.centralwidget, "save_button", geometry=QtCore.QRect(410, 30, 200, 45)
        )

        # Reset Button
        self.reset_button = self.create_button(
            "Reset", self.centralwidget, "reset_button", geometry=QtCore.QRect(690, 30, 200, 45)
        )

        # Upload Button
        self.upload_button = self.create_button(
            "Upload Photo", self.centralwidget, "upload_button", geometry=QtCore.QRect(970, 30, 200, 45)
        )

        # Quit App Button
        self.quit_app_button = self.create_button(
            "X", self.centralwidget, "quit_app_button", geometry=QtCore.QRect(1220, 30, 50, 50),
            font_size=40, font_family="Hiragino Sans GB", hover_color="rgb(253, 94, 80)"
        )

    def setup_sidebar_3(self):
        """Set up the third sidebar with group boxes and buttons."""
        self.sidebar_3_layout = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_3_layout.setGeometry(QtCore.QRect(10, 130, 285, 630))
        self.sidebar_3_layout.setObjectName("sidebar_3_layout")

        self.sidebar_3 = QtWidgets.QVBoxLayout(self.sidebar_3_layout)
        self.sidebar_3.setContentsMargins(0, 0, 0, 0)
        self.sidebar_3.setObjectName("sidebar_3")

        # Initial Contour GroupBox
        self.initial_conour_groupBox = self.create_group_box(
            "Initial Contour", self.sidebar_3_layout, "initial_conour_groupBox"
        )
        self.setup_initial_contour(self.initial_conour_groupBox)
        self.sidebar_3.addWidget(self.initial_conour_groupBox)

        # Snake Contour GroupBox
        self.snake_contour_groupBox = self.create_group_box(
            "Snake Contour", self.sidebar_3_layout, "snake_contour_groupBox"
        )
        self.setup_snake_contour(self.snake_contour_groupBox)
        self.sidebar_3.addWidget(self.snake_contour_groupBox)

        # Active Contour GroupBox
        self.active_contour_groupbox = self.create_group_box(
            "Active Contour", self.sidebar_3_layout, "active_contour_groupbox"
        )
        self.setup_active_contour(self.active_contour_groupbox)
        self.sidebar_3.addWidget(self.active_contour_groupbox)

        # Apply Contour Button
        self.apply_contour_button = self.create_button(
            "Apply Contour", self.sidebar_3_layout, "apply_contour_button"
        )
        # self.apply_contour_button.setFixedSize(200, 45)

        GroupBoxStyleSheet = """
            QGroupBox {
                color: white;
                border: 5px solid white;
            }
        """

        self.initial_conour_groupBox.setStyleSheet(GroupBoxStyleSheet)
        self.snake_contour_groupBox.setStyleSheet(GroupBoxStyleSheet)
        self.active_contour_groupbox.setStyleSheet(GroupBoxStyleSheet)

        self.sidebar_3.addWidget(self.apply_contour_button)

    def setup_sidebar_2(self):
        """Set up the second sidebar with labels, sliders, and buttons."""
        self.sidebar_2_layout = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_2_layout.setGeometry(QtCore.QRect(10, 100, 271, 680))
        self.sidebar_2_layout.setObjectName("sidebar_2_layout")

        self.sidebar_5 = QtWidgets.QVBoxLayout(self.sidebar_2_layout)
        self.sidebar_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.sidebar_5.setContentsMargins(0, 0, 0, 0)
        self.sidebar_5.setObjectName("sidebar_5")

        # Parametric Shape Label
        self.parametric_shape_label = self.create_label(
            "Parametric Shape", self.sidebar_2_layout, "parametric_shape_label", font_size=16, bold=True
        )
        self.sidebar_5.addWidget(self.parametric_shape_label)

        # Parametric Shape ComboBox
        self.parametric_shape_combobox = QtWidgets.QComboBox(self.sidebar_2_layout)
        self.parametric_shape_combobox.setMinimumSize(QtCore.QSize(0, 25))
        self.parametric_shape_combobox.setStyleSheet(
            "QComboBox{ background-color: rgb(255, 255, 255); border: 1px solid white; }"
            "QComboBox:hover { border-color:rgb(5, 255, 142); color: rgb(5, 255, 142); }"
        )

        self.parametric_shape_combobox.setObjectName("parametric_shape_combobox")
        self.sidebar_5.addWidget(self.parametric_shape_combobox)

        # Line Threshold Label and Slider
        self.line_threshold_label = self.create_label(
            "Line Threshold", self.sidebar_2_layout, "line_threshold_label", font_size=16, bold=True
        )
        self.sidebar_5.addWidget(self.line_threshold_label)

        self.line_threshold_slider = QtWidgets.QSlider(self.sidebar_2_layout)
        self.line_threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.line_threshold_slider.setObjectName("line_threshold_slider")
        self.sidebar_5.addWidget(self.line_threshold_slider)

        # Circle Label and Sliders
        self.circle_label = self.create_label(
            "Circle", self.sidebar_2_layout, "circle_label", font_size=16, bold=True
        )
        self.sidebar_5.addWidget(self.circle_label)

        self.min_radius_label = self.create_label(
            "Minimum Radius", self.sidebar_2_layout, "min_radius_label"
        )
        self.sidebar_5.addWidget(self.min_radius_label)

        self.min_radius_slider = QtWidgets.QSlider(self.sidebar_2_layout)
        self.min_radius_slider.setOrientation(QtCore.Qt.Horizontal)
        self.min_radius_slider.setObjectName("min_radius_slider")
        self.sidebar_5.addWidget(self.min_radius_slider)

        self.max_radius_label = self.create_label(
            "Maximum Radius", self.sidebar_2_layout, "max_radius_label"
        )
        self.sidebar_5.addWidget(self.max_radius_label)

        self.max_radius_slider = QtWidgets.QSlider(self.sidebar_2_layout)
        self.max_radius_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_radius_slider.setObjectName("max_radius_slider")
        self.sidebar_5.addWidget(self.max_radius_slider)

        self.circle_threshold_label = self.create_label(
            "Circle Threshold", self.sidebar_2_layout, "circle_threshold_label"
        )
        self.sidebar_5.addWidget(self.circle_threshold_label)

        self.circle_threshold_slider = QtWidgets.QSlider(self.sidebar_2_layout)
        self.circle_threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.circle_threshold_slider.setObjectName("circle_threshold_slider")
        self.sidebar_5.addWidget(self.circle_threshold_slider)

        # Ellipse Label and Sliders
        self.ellipse_label = self.create_label(
            "Ellipse", self.sidebar_2_layout, "ellipse_label", font_size=16, bold=True
        )
        self.sidebar_5.addWidget(self.ellipse_label)

        self.min_radius_label_2 = self.create_label(
            "Minimum Radius", self.sidebar_2_layout, "min_axis_len_label"
        )
        self.sidebar_5.addWidget(self.min_radius_label_2)

        self.min_radius_slider_2 = QtWidgets.QSlider(self.sidebar_2_layout)
        self.min_radius_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.min_radius_slider_2.setObjectName("min_ellipse_len_slider")
        self.sidebar_5.addWidget(self.min_radius_slider_2)

        self.max_radius_label_2 = self.create_label(
            "Maximum Radius", self.sidebar_2_layout, "max_axis_len_label"
        )
        self.sidebar_5.addWidget(self.max_radius_label_2)

        self.max_radius_slider_2 = QtWidgets.QSlider(self.sidebar_2_layout)
        self.max_radius_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.max_radius_slider_2.setObjectName("max_ellipse_slider")
        self.sidebar_5.addWidget(self.max_radius_slider_2)

        # Apply Button
        self.apply_button = self.create_button(
            "Apply", self.sidebar_2_layout, "apply_button"
        )
        self.sidebar_5.addWidget(self.apply_button)

    def setup_menu_and_status_bar(self, MainWindow):
        """Set up the menu bar and status bar."""
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def create_button(self, text, parent, object_name, geometry=None, font_size=14, font_family="",
                      hover_color="rgb(5, 255, 142)", minimum_size=None, maximum_size=None):
        """Helper function to create a button."""
        button = QtWidgets.QPushButton(parent)
        if geometry:
            button.setGeometry(geometry)
        button.setFont(QtGui.QFont(font_family, font_size))
        button.setStyleSheet(
            f"QPushButton {{ color: rgb(255, 255, 255); border: 3px solid rgb(255, 255, 255); height:40px; }}"
            f"QPushButton:hover {{ border-color:{hover_color}; color: {hover_color}; }}"
        )
        button.setObjectName(object_name)
        button.setText(text)

        # Set minimum and maximum size if provided
        if minimum_size:
            button.setMinimumSize(QtCore.QSize(*minimum_size))
        if maximum_size:
            button.setMaximumSize(QtCore.QSize(*maximum_size))

        return button

    def create_label(self, text, parent, object_name, font_size=11, bold=False):
        """Helper function to create a label."""
        label = QtWidgets.QLabel(parent)
        label.setFont(QtGui.QFont("", font_size, QtGui.QFont.Bold if bold else QtGui.QFont.Normal))
        label.setStyleSheet("QLabel{ color: rgb(255, 255, 255); }")
        label.setObjectName(object_name)
        label.setText(text)
        return label

    def create_group_box(self, title, parent, object_name):
        """Helper function to create a group box."""
        group_box = QtWidgets.QGroupBox(parent)
        group_box.setStyleSheet("color: rgb(255, 255, 255);"
                                "QGroupBox:border: 5px solid rgb(255, 255, 255); }")
        group_box.setObjectName(object_name)
        group_box.setTitle(title)
        return group_box

    def setup_initial_contour(self, group_box):
        """Set up the initial contour group box."""
        grid_layout = QtWidgets.QGridLayout(group_box)
        grid_layout.setObjectName("gridLayout_3")

        self.circle_radius_label = self.create_label(
            "Circle Radius", group_box, "circle_radius_label"
        )
        grid_layout.addWidget(self.circle_radius_label, 0, 0, 1, 1)

        self.circle_radius_spinBox = QtWidgets.QSpinBox(group_box)
        self.circle_radius_spinBox.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
        self.circle_radius_spinBox.setObjectName("circle_radius_spinBox")
        grid_layout.addWidget(self.circle_radius_spinBox, 0, 1, 1, 1)

    def setup_snake_contour(self, group_box):
        """Set up the snake contour group box."""
        grid_layout = QtWidgets.QGridLayout(group_box)
        grid_layout.setVerticalSpacing(20)
        grid_layout.setObjectName("gridLayout_2")

        self.area_label = self.create_label("Area", group_box, "area_label")
        grid_layout.addWidget(self.area_label, 0, 0, 1, 1)

        self.area_spinBox = QtWidgets.QSpinBox(group_box)
        self.area_spinBox.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
        self.area_spinBox.setObjectName("area_spinBox")
        grid_layout.addWidget(self.area_spinBox, 0, 1, 1, 1)

        self.perimeter_label = self.create_label("Perimeter", group_box, "perimeter_label")
        grid_layout.addWidget(self.perimeter_label, 1, 0, 1, 1)

        self.perimeter_spinBox = QtWidgets.QSpinBox(group_box)
        self.perimeter_spinBox.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
        self.perimeter_spinBox.setObjectName("perimeter_spinBox")
        grid_layout.addWidget(self.perimeter_spinBox, 1, 1, 1, 1)

    def setup_active_contour(self, group_box):
        """Set up the active contour group box."""
        grid_layout = QtWidgets.QGridLayout(group_box)
        grid_layout.setVerticalSpacing(35)
        grid_layout.setObjectName("gridLayout")

        labels = ["Window Size", "Num of Points", "Num of Itr", "Alpha", "Beta", "Gamma"]
        for i, label_text in enumerate(labels):
            label = self.create_label(label_text, group_box, f"{label_text.lower().replace(' ', '_')}_label")
            grid_layout.addWidget(label, i, 0, 1, 1)

            if label_text == "Window Size":
                self.window_size_spin_box = QtWidgets.QSpinBox(group_box)
                self.window_size_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.window_size_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.window_size_spin_box, i, 1, 1, 1)

            elif label_text == "Num of Points":
                self.num_of_points_spin_box = QtWidgets.QSpinBox(group_box)
                self.num_of_points_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.num_of_points_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.num_of_points_spin_box, i, 1, 1, 1)

            elif label_text == "Num of Itr":
                self.num_of_itr_spin_box = QtWidgets.QSpinBox(group_box)
                self.num_of_itr_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.num_of_itr_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.num_of_itr_spin_box, i, 1, 1, 1)

            elif label_text == "Alpha":
                self.alpha_spin_box = QtWidgets.QSpinBox(group_box)
                self.alpha_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.alpha_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.alpha_spin_box, i, 1, 1, 1)

            elif label_text == "Beta":
                self.beta_spin_box = QtWidgets.QSpinBox(group_box)
                self.beta_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.beta_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.beta_spin_box, i, 1, 1, 1)

            elif label_text == "Gamma":
                self.gamma_spin_box = QtWidgets.QSpinBox(group_box)
                self.gamma_spin_box.setStyleSheet("QSpinBox{ color: rgb(255, 255, 255); }")
                self.gamma_spin_box.setObjectName(f"{label_text.lower().replace(' ', '_')}_spinBox")
                grid_layout.addWidget(self.gamma_spin_box, i, 1, 1, 1)

    def retranslateUi(self, MainWindow):
        """Translate the UI elements."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.original_image_groupbox.setTitle(_translate("MainWindow", "Original Image"))
        self.processed_image_groupbox.setTitle(_translate("MainWindow", "Processed Image"))
        self.edge_detection_button.setText(_translate("MainWindow", "Edge Detection"))
        self.object_contour_button.setText(_translate("MainWindow", "Object Contour"))
        self.back_button.setText(_translate("MainWindow", "⇦"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.upload_button.setText(_translate("MainWindow", "Upload Photo"))
        self.quit_app_button.setText(_translate("MainWindow", "X"))
        self.initial_conour_groupBox.setTitle(_translate("MainWindow", "Initial Contour"))
        self.circle_radius_label.setText(_translate("MainWindow", "Circle Radius"))
        self.snake_contour_groupBox.setTitle(_translate("MainWindow", "Snake Contour"))
        self.area_label.setText(_translate("MainWindow", "Area"))
        self.perimeter_label.setText(_translate("MainWindow", "Perimeter"))
        self.active_contour_groupbox.setTitle(_translate("MainWindow", "Active Contour"))
        self.apply_contour_button.setText(_translate("MainWindow", "Apply Contour"))
        self.parametric_shape_label.setText(_translate("MainWindow", "Parametric Shape"))
        self.line_threshold_label.setText(_translate("MainWindow", "Line Threshold"))
        self.circle_label.setText(_translate("MainWindow", "Circle"))
        self.min_radius_label.setText(_translate("MainWindow", "Minimum Radius"))
        self.max_radius_label.setText(_translate("MainWindow", "Maximum Radius"))
        self.circle_threshold_label.setText(_translate("MainWindow", "Circle Threshold"))
        self.ellipse_label.setText(_translate("MainWindow", "Ellipse"))
        self.min_radius_label_2.setText(_translate("MainWindow", "Minimum Radius"))
        self.max_radius_label_2.setText(_translate("MainWindow", "Maximum Radius"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
