#connecting the module with layouts
from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


#creating an application object
app = QApplication([])
# creating the main window object
my_win = QWidget()
# creating the name of the main window
my_win.setWindowTitle('My first app')
# setting the point where the window will show up on the computer screen
my_win.move(900, 70)
# setting the window size
my_win.resize(400, 200)
# giving the window the command to show up
my_win.show()
# creating a vertical layout
line = QVBoxLayout()
# creating a button object and setting a label on it
button = QPushButton('Secret button')
# putting the text on the center of the layout
line.addWidget(button, alignment = Qt.AlignCenter)
# adding the resulting line to the application window
my_win.setLayout(line)


#a function that creates and displays the second phrase
def show_fun_title():
    fun_title = QLabel('You are a miracle!')
    line.addWidget(fun_title, alignment = Qt.AlignCenter)
    my_win.setLayout(line)


# linking a button press to a function call
button.clicked.connect(show_fun_title)
#Leaves the app open until the exit button is pressed
app.exec_()
