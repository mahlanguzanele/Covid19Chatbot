from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication, QVBoxLayout, QLabel, QScrollBar
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
import threading
from backend import ChatBot


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add scrollbar to the chat area
        scroll_bar = QScrollBar(Qt.Orientation.Vertical, self.chat_area)
        self.chat_area.setVerticalScrollBar(scroll_bar)

        # Set font and style for the chat area
        font = QFont("Arial", 12)
        self.chat_area.setFont(font)
        self.chat_area.setStyleSheet("background-color: #F5F5F5; color: #333333;")

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton('Send', self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        if not user_input:
            return

        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input: str):
        # Check if user_input is a simple greeting like "hey"
        if user_input.lower() == 'hey':
            response = "Hey there! How can I help you today?"
        else:
            response = self.chatbot.get_response(user_input)

        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")
app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
