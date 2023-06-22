from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel


app = QApplication([])
window = QWidget()
window.setWindowTitle('Programming Languages')
window.resize(400, 300)


#Step 1. Create 6 labels with the names of programming languages
sentence1 = QLabel('PHP')
sentence2 = QLabel('JavaScript')
sentence3 = QLabel('Python')
sentence4 = QLabel('Pascal')
sentence5 = QLabel('SQL')
sentence6 = QLabel('C++')


#Step 2. Create 4 layouts: 3 horizontal and 1 vertical
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


#Step 3. Link 6 objects to horizontal layouts
layoutH1.addWidget(sentence1, alignment = Qt.AlignCenter)
layoutH1.addWidget(sentence2, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence3, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence4, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence5, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence6, alignment = Qt.AlignCenter)


#Step 4. Link the horizontal layouts to the vertical layout
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)


window.show()
app.exec_()
