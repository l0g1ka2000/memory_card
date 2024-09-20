''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo_app import app 

# віджети, які потрібно буде розмістити:
btn_Menu = QPushButton('Меню') # кнопка повернення в головне вікно 
btn_Sleep = QPushButton('Відпочити') # кнопка ховає вікно і повертає його після завершення таймера
box_Minutes = QSpinBox() # введення кількості хвилин
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти') # кнопка відповіді
lb_Question = QLabel('') # текст питання

# Панель з варіантами:
RadioGroupBox = QGroupBox("Варіанти відповідей") # група на екрані для перемикачів з відповідями
RadioGroup = QButtonGroup() # для групування перемикачів, щоб керувати їхньою поведінкою

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Панель з результатом:
AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('') # тут розміщується напис "правильно" або "неправильно"
lb_Correct = QLabel('') # тут буде написаний текст правильної відповіді

# Тепер займаємося розміщенням:

# Розміщуємо варіанти відповідей у два стовпці всередині групи:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальні будуть всередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два варіанти у перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два варіанти у другий стовпець
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку

RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей    
# розміщуємо результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо якомога більшим
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин')) # змінна для цього напису не потрібна

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка має бути великою
layout_line4.addStretch(1)

# Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # відстані між вмістом

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.

def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')

def show_question():
    ''' показати панель питань '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    # скинути вибрану радіо-кнопку
    RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіо-кнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # повернули обмеження, тепер можна вибрати тільки одну радіо-кнопку
