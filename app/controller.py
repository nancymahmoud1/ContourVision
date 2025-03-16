from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, center
from app.design2 import Ui_MainWindow
from app.utils.clean_cache import remove_directories
from app.services.image_service import ImageServices
from app.processing.contour import Contour
import cv2
import numpy as np
from skimage.filters import gaussian



class MainWindowController:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Track the previous sidebar
        self.previous_sidebar = None

        # Show sidebar_1 initially
        self.show_sidebar_1()

        # Center alignment for shapes_sidebar_layout
        self.ui.verticalLayout_5.setAlignment(Qt.AlignCenter)

        # Connect button signals
        self.ui.quit_app_button.clicked.connect(self.closeApp)
        self.ui.back_button.clicked.connect(self.go_back)  # Connect back button
        self.ui.shape_detection_button.clicked.connect(self.show_sidebar_2)
        self.ui.object_contour_button.clicked.connect(self.show_sidebar_3)
        self.ui.canny_edge_detection_button.clicked.connect(self.show_filter_sidebar)
        self.ui.line_detection_button.clicked.connect(lambda: self.show_groupbox(self.ui.line_groupBox))
        self.ui.circle_detection_button.clicked.connect(lambda: self.show_groupbox(self.ui.circle_groupBox))
        self.ui.ellipse_detection_button.clicked.connect(lambda: self.show_groupbox(self.ui.ellipse_groupBox))
        self.srv = ImageServices()
        self.ui.upload_button.clicked.connect(self.drawImage)
        self.ui.save_button.clicked.connect(lambda: self.srv.save_image(self.processed_image))
        self.ui.reset_button.clicked.connect(self.reset_images)
        self.ui.apply_contour_button.clicked.connect(self.apply_contour)
        self.contour = Contour()

    def drawImage(self):
        self.path = self.srv.upload_image_file()
        self.original_image = cv2.imread(self.path)
        self.processed_image = self.original_image

        # If user cancels file selection, path could be None
        if self.path:
            self.srv.clear_image(self.ui.original_image_groupbox)
            self.srv.clear_image(self.ui.processed_image_groupbox)
            self.srv.set_image_in_groupbox(self.ui.original_image_groupbox, self.original_image)
            self.srv.set_image_in_groupbox(self.ui.processed_image_groupbox, self.processed_image)

    def reset_images(self):
        if self.original_image is None:
            return

        self.srv.clear_image(self.ui.processed_image_groupbox)
        self.srv.set_image_in_groupbox(self.ui.processed_image_groupbox, self.original_image)

    def run(self):
        """Run the application."""
        self.MainWindow.showFullScreen()
        self.app.exec_()

    def quit_app(self):
        """Quit the application."""
        self.app.quit()
        remove_directories()

    def closeApp(self):
        """Close the application."""
        remove_directories()
        self.app.quit()

    def show_sidebar_1(self):
        """Show sidebar_1 and hide other sidebars."""
        self.ui.sidebar_2_layout.hide()  # Hide sidebar_2
        self.ui.sidebar_3_layout.hide()  # Hide sidebar_3
        self.ui.page_filter_layout.hide()
        self.ui.shapes_sidebar_layout.hide()  # Hide shapes_sidebar_layout
        self.ui.sidebar_1_layout.show()  # Show sidebar_1
        self.previous_sidebar = None  # Reset previous sidebar
        self.ui.back_button.hide()

    def show_sidebar_2(self):
        """Show sidebar_2 and hide other sidebars."""
        self.ui.sidebar_1_layout.hide()  # Hide sidebar_1
        self.ui.sidebar_3_layout.hide()  # Hide sidebar_3
        self.ui.page_filter_layout.hide()
        self.ui.shapes_sidebar_layout.hide()  # Hide shapes_sidebar_layout
        self.ui.sidebar_2_layout.show()  # Show sidebar_2
        self.previous_sidebar = "sidebar_1"  # Set previous sidebar
        self.ui.back_button.show()

    def show_sidebar_3(self):
        """Show sidebar_3 and hide other sidebars."""
        self.ui.sidebar_1_layout.hide()  # Hide sidebar_1
        self.ui.sidebar_2_layout.hide()  # Hide sidebar_2
        self.ui.page_filter_layout.hide()
        self.ui.shapes_sidebar_layout.hide()  # Hide shapes_sidebar_layout
        self.ui.sidebar_3_layout.show()  # Show sidebar_3
        self.previous_sidebar = "sidebar_1"  # Set previous sidebar
        self.ui.back_button.show()

    def show_filter_sidebar(self):
        """Show filter sidebar and hide other sidebars."""
        self.ui.sidebar_1_layout.hide()  # Hide sidebar_1
        self.ui.sidebar_2_layout.hide()  # Hide sidebar_2
        self.ui.sidebar_3_layout.hide()  # Hide sidebar_3
        self.ui.shapes_sidebar_layout.hide()  # Hide shapes_sidebar_layout
        self.ui.page_filter_layout.show()
        self.previous_sidebar = "sidebar_1"  # Set previous sidebar
        self.ui.back_button.show()

    def show_groupbox(self, groupbox_to_show):
        """
        Show shapes_sidebar_layout and the specified group box, hide other group boxes.

        Args:
            groupbox_to_show (QGroupBox): The group box to show (e.g., line_groupBox, circle_groupBox, ellipse_groupBox).
        """
        # Hide all sidebars
        self.ui.sidebar_1_layout.hide()  # Hide sidebar_1
        self.ui.sidebar_2_layout.hide()  # Hide sidebar_2
        self.ui.sidebar_3_layout.hide()  # Hide sidebar_3
        self.ui.page_filter_layout.hide()  # Hide filter sidebar

        # Show the shapes_sidebar_layout
        self.ui.shapes_sidebar_layout.show()

        # Hide all group boxes
        self.ui.line_groupBox.hide()
        self.ui.circle_groupBox.hide()
        self.ui.ellipse_groupBox.hide()

        # Show the specified group box
        groupbox_to_show.show()

        # Set previous sidebar to sidebar_2 (Shape Detection)
        self.previous_sidebar = "sidebar_2"

    def go_back(self):
        """Handle the back button click."""
        if self.previous_sidebar == "sidebar_1":
            self.show_sidebar_1()
        elif self.previous_sidebar == "sidebar_2":
            self.show_sidebar_2()
        elif self.previous_sidebar == "sidebar_3":
            self.show_sidebar_3()
        else:
            self.show_sidebar_1()  # Default to sidebar_1 if no previous sidebar is set

    def apply_contour(self):
        if self.original_image is None:
            print("No image available")
            return
        if self.processed_image is None:
            print("No image available")
            return

        num_points = self.ui.num_of_points_spinBox.value()
        num_iterations = self.ui.num_of_itr_spinBox.value()
        alpha = self.ui.alpha_spinBox.value()
        beta = self.ui.beta_spinBox.value()
        gamma = self.ui.gamma_spinBox.value()
        radius = self.ui.circle_radius_spinBox.value()
        window_size = self.ui.window_size_spinBox.value()
        center= self.original_image.shape[0]//2, self.original_image.shape[1]//2

        # Initialize the contour
        original_snake = self.contour.initialize_contour(self.original_image, center, radius,num_points)

        # Evolve the contour
        # Smooth the image
        image = gaussian(self.original_image, sigma=1)
        processed_snake = self.contour.active_contour_greedy(image, original_snake, max_num_iter=num_iterations, alpha=alpha, beta=beta, gamma=gamma)


        original_image_with_snake = self.draw_contour_on_image(self.original_image,original_snake)
        self.showImage(original_image_with_snake, self.ui.original_image_groupbox)

        processed_image_with_snake = self.draw_contour_on_image(self.processed_image,processed_snake)
        self.showImage(processed_image_with_snake, self.ui.processed_image_groupbox)

        # Compute chain code, area, and perimeter


    def showImage(self, image, groupbox):
        if image is None:
            print("Error: Processed image is None.")
            return  # Prevents crashing

        self.srv.clear_image(groupbox)
        self.srv.set_image_in_groupbox(groupbox, image)

    def draw_contour_on_image(self, image, snake):
        """
        Draws the contour (snake) on the image.

        Args:
            image (ndarray): The original image.
            snake (ndarray): The contour points.

        Returns:
            ndarray: The image with the contour drawn on it.
        """
        # Create a copy of the original image to draw on
        image_with_contour = image.copy()

        # Convert snake points to integer for drawing
        snake_points = np.array(snake, dtype=np.int32)

        # Draw the contour on the image
        for point in snake_points:
            cv2.circle(image_with_contour, tuple(point), radius=2, color=(0, 255, 0), thickness=-1)  # Green color for contour

        return image_with_contour