import sys
import speech_recognition as sr
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QTabWidget, QFileDialog, QMessageBox, QListWidget
from PyQt5.QtCore import Qt
from kanchhi3 import Ui_HomePage  # Import the Ui_HomePage class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kanchhi")
        self.setGeometry(0, 0, 1920,1080)

        # To store recent notes file paths
        self.recent_notes = []

        # Main widget container
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        self.main_layout = QVBoxLayout(self.central_widget)

        # Tab widget for main content area
        self.tabs = QTabWidget()
        self.home_widget = self.create_home_widget()
        self.settings_widget = self.create_settings_widget()
        self.notes_widget = self.create_notes_widget()

        self.tabs.addTab(self.home_widget, "Home")
        self.tabs.addTab(self.settings_widget, "History")
        self.tabs.addTab(self.notes_widget, "Notes")

        # Add tabs to main layout
        self.main_layout.addWidget(self.tabs)

        # Apply stylesheets
        self.apply_stylesheet()

    def create_home_widget(self):
        widget = Ui_HomePage()
        return widget

    def create_settings_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("History")
        label.setAlignment(Qt.AlignCenter)

        self.recent_notes_view = QListWidget()

        layout.addWidget(label)
        layout.addWidget(self.recent_notes_view)
        widget.setLayout(layout)

        return widget

    def create_notes_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Notes Page")
        label.setAlignment(Qt.AlignCenter)

        self.text_edit = QTextEdit()
        self.text_edit.setObjectName("notesTextEdit")  # Add object name for CSS styling

        start_button = QPushButton("भ्वाइस रेकर्डिङ सुरु गर्नुहोस्")
        start_button.setObjectName("startButton")  # Add object name for CSS styling
        start_button.clicked.connect(self.start_voice_recording)

        save_button = QPushButton("नोटहरू दर्ता गर्नुहोस्")
        save_button.setObjectName("saveButton")  # Add object name for CSS styling
        save_button.clicked.connect(self.save_notes)

        layout.addWidget(label)
        layout.addWidget(self.text_edit)
        layout.addWidget(start_button)
        layout.addWidget(save_button)
        widget.setLayout(layout)

        return widget

    def start_voice_recording(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ne-NP')
            self.text_edit.append(text)
            print(f"Recognized text: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    def save_notes(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Notes", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            try:
                content = self.text_edit.toPlainText()
                if content:  # Check if there is content to save
                    with open(file_path, 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding
                        file.write(content)
                    QMessageBox.information(self, "Success", f"Notes saved to {file_path}")
                    self.recent_notes.append(file_path)
                    self.update_recent_notes()
                    self.refresh_notes_page()  # Clear the text edit area after saving
                else:
                    QMessageBox.warning(self, "Warning", "There is no text to save.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save notes: {e}")

    def update_recent_notes(self):
        self.recent_notes_view.clear()
        for note in self.recent_notes[-5:]:  # Show only the last 5 notes
            self.recent_notes_view.addItem(note)

    def refresh_notes_page(self):
        self.text_edit.clear()

    def display(self, index):
        self.tabs.setCurrentIndex(index)
        if index == 1:  # When switching to the settings page
            self.update_recent_notes()

    def apply_stylesheet(self):
        stylesheet = """
            QMainWindow {
                background-color: lightgray;
            }
            QTabWidget::pane {
                border: 1px solid gray;
                background: white;
            }
            QTabBar::tab {
                background: lightgray;
                border: 1px solid gray;
                padding: 10px;
                min-width: 80px;
                font-size: 14px;
            }
            QTabBar::tab:selected {
                background: white;
                font-weight: bold;
            }
            QLabel {
                font-size: 22px;
                color: black;
            }
            QLabel#SwagatamLabel {  /* Specific styling for the welcome label */
                font-size: 50px;  /* Make the font size bigger */
                color: black;
            }
            
            QTextEdit#notesTextEdit {  /* Specific styling for the notes QTextEdit */
                background-color: whitesmoke;
                border: 1px solid gray;
                padding: 10px;
                font-size: 14px;
                color: black;
                border-radius: 5px;
            }
            QPushButton#startButton, QPushButton#saveButton {
                background-color: green;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
                border-radius: 10px;  /* Rounded corners */
                box-shadow: 0 4px gray;  /* Add a shadow */
            }
            QPushButton#startButton:hover, QPushButton#saveButton:hover {
                background-color: #1E4620;
                color: #EEEEEE;
            }
            QPushButton#startButton:active, QPushButton#saveButton:active {
                background-color: darkgreen;
                box-shadow: 0 2px gray;
                transform: translateY(2px);
            }
            QListWidget {
                border: 1px solid gray;
                background-color: white;
                padding: 5px;
            }
            
        """
        self.setStyleSheet(stylesheet)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
