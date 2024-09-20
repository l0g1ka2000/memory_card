from PyQt5.QtWidgets import QWidget
from random import shuffle # будемо перемішувати відповіді в картці питання

from memo_app import app
from memo_data import Form, FormView

from memo_main_layout import layout_main, btn_card, btn_form, wdgt_edit, wdgt_card
from memo_card_layout import (
    # app, layout_card, - це більше не потрібно!
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result
)
from memo_edit_layout import (txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
main_width, main_height = 800, 450 # початкові розміри головного вікна

text_wrong = '''<font color="red">Невірно</font>'''
text_correct = '''<font color="green">Вірно</font>'''

# поки ще працюємо з одним питанням, а не списком питань. Створюємо:
frm = Form('Кому на Русі жити добре?', 'Програмістам', 'Дворянам', 'Селянам', 'Об’єднаним пролетаріям')

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)  
frm_card = FormView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])
frm_edit = FormView(frm, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)

def check_result():
    ''' перевірка, чи правильну відповідь обрано
    якщо відповідь була обрана, то напис "вірно/невірно" набуває потрібного значення
    і показується панель відповідей '''
    
    correct = frm_card.answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
    if correct:
        # відповідь правильна, запишемо
        lb_Result.setText(text_correct) # напис "вірно" або "невірно"
        lb_Correct.setText(frm_card.answer.text()) # це доводиться робити вручну
        show_result()
    else:
        incorrect = frm_card.wrong_answer1.isChecked() or frm_card.wrong_answer2.isChecked() or frm_card.wrong_answer3.isChecked()
        if incorrect:
            # відповідь неправильна, запишемо і відобразимо у статистиці
            lb_Result.setText(text_wrong) # напис "вірно" або "невірно"
            lb_Correct.setText(frm_card.answer.text()) # це доводиться робити вручну
            show_result()

def click_OK(self):
    # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
    if btn_OK.text() != 'Наступне':
        check_result()

def show_card():
    # показати питання
    wdgt_edit.hide()
    wdgt_card.show()

def show_form():
    # редагувати питання
    wdgt_card.hide()
    wdgt_edit.show()

btn_card.clicked.connect(show_card)
btn_form.clicked.connect(show_form)
btn_OK.clicked.connect(click_OK)

win_card = QWidget()
win_card.resize(main_width, main_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_main)
# show_data() замість цього використовуємо методи об'єктів, що зв'язують форми з даними:
frm_card.show()
frm_edit.show()
show_question()
show_card()

win_card.show()
app.exec_()
