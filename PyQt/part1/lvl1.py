#connecting the module with layouts
from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


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


# creating a horizontal layout
line = QHBoxLayout()
# creating a text object
title = QLabel('Hello, world!')
# putting the text on the center of the layout
line.addWidget(title, alignment=Qt.AlignCenter)
# adding the resulting line to the application window
my_win.setLayout(line)
#Leaves the app open until the exit button is pressed
app.exec_()
