#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (Qapplication, Qwidget, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Англиский', 'Испанский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зеленый', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))


app = QApplication([])


'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была снована Москва?')


RadioGroupBox = QGroupBox('Варианты ответов')


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


Layout_ans1 = QHBoxLayout()
Layout_ans2 = QHBoxLayout()
Layout_ans3 = QHBoxLayout()
Layout_ans2.addWIdget(rbtn_1)
Layout_ans2.addWIdget(rbtn_2)
Layout_ans3.addWIdget(rbtn_3)
Layout_ans3.addWIdget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
Ib_Result = QLabel('прав ты или нет?')
Ib_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(Ib_Result, alignment=(Qt.Alignleft / Qt.AlignTop))
layout_res.addWidget(Ib_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, aligment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_Line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


layout_line3.addStretch(1)
laoyut_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QvBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStrench(1)
layout_card.addSpacing(5)



def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBoox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' функция записывает значение вопроса и ответов в соответствущие виджеты
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    Ib_Question.setText(q.question)
    Ib_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ''' показать результат - устоновим переданный текст в надпись "результат" и покажем нужную панель '''
    Ib_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов '''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика/n-Всего вопросов: ', window.total, '/n-Правиьных ответов: ', window.score)
        print('Рейтинг:  ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked():
            show_correct('Наверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')


def next_question():
    ''' задает следующий вопрос из списка '''
    window.total += 1
    print('Статистика/n-Всего вопросов: ', window.total, '/n-Правиьных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)


    q = question_list[cur_question]
    ask(q)


def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')



btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()