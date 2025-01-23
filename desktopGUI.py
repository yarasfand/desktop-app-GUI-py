from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class AdvancedDesignApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Patient App")
        self.setGeometry(100, 100, 800, 600) 
        self.setStyleSheet("background-color: #013220;")  # Dark green background

        # Create grid layout
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)  # Spacing between boxes

        # Options with text and images
        options = [
            {"text": "Call Nurse", "image": "./assets/nurse.png"},
            {"text": "Go to Washroom", "image": "./assets/toilet.png"},
            {"text": "Need Food", "image": "./assets/diet.png"},
            {"text": "Turn Off Lights", "image": "./assets/switch-off.png"}
        ]

        # Add boxes to the grid
        for index, option in enumerate(options):
            row, col = divmod(index, 2)  # Two rows, two columns

            # Create a container for the image and text
            outerContainer = QWidget()
            container = QWidget()
            container_layout = QVBoxLayout()
            container_layout.setAlignment(Qt.AlignCenter)

            # Add text
            text_label = QLabel(option["text"])
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setFont(QFont("Poppins", 16, QFont.Bold))  # Poppins font, bold, size 16
            text_label.setStyleSheet("color: white;")  # White text

            # Add an image
            image_label = QLabel()
            pixmap = QPixmap(option["image"])  # Replace with the path to your image
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)

            # Add text and image to the container layout
            container_layout.addWidget(text_label)
            container_layout.addWidget(image_label)
            container.setLayout(container_layout)
            container.setStyleSheet("""
                background-color: #2e8b57;  /* Lighter green for card */
               
                border-radius: 10px;
                padding: 20px;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);  /* White shade effect */
            """)

            grid_layout.addWidget(container, row, col)

        # Set layout
        self.setLayout(grid_layout)

# Run the app
if __name__ == "__main__":
    app = QApplication([])
    window = AdvancedDesignApp()
    window.show()
    app.exec_()