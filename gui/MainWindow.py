from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from gui.MainWindow_ui import Ui_DSA
from back.filemanager import WorkFile
from algorithm_DSA.DSA import DSA

class Main(QMainWindow):
    
    def __init__(self, ui: Ui_DSA) -> None:
        super().__init__()
        self.ui = ui
        self.dsa = DSA()
        self.ui.setupUi(self)
        # Выбоор режима работы
        self.ui.senderButton.clicked.connect(lambda : self.choice(1, "DSA Отправитель"))
        self.ui.receiverButton.clicked.connect(lambda : self.choice(2, "DSA Получатель"))
        # Работа Отправителя
        self.ui.generateParamsButton.clicked.connect(lambda : self.generate_params())
        self.ui.uploadParamsButton.clicked.connect(lambda : self.upload_params())
        self.ui.saveParamsButton.clicked.connect(lambda : self.save_params())
        self.ui.p_checkButton.clicked.connect(lambda : self.check_prime(self.dsa.p))
        self.ui.q_checkButton.clicked.connect(lambda : self.check_prime(self.dsa.q))
        self.ui.generateKeysButton.clicked.connect(lambda : self.generate_keys())
        self.ui.uploadKeysButton.clicked.connect(lambda : self.upload_keys())
        self.ui.saveKeysButton.clicked.connect(lambda : self.save_keys())
        self.ui.signButton.clicked.connect(lambda : self.sign_mes())
        self.ui.saveButton.clicked.connect(lambda : self.save_sign())
        # Работа Получателя
        self.ui.uploadParamsKeyButton.clicked.connect(lambda : self.upload_params_reciver())
        self.ui.uploadButtonReciever.clicked.connect(lambda : self.upload_sign_message())
        self.ui.calculateButtonReciever.clicked.connect(lambda : self.calculate_params_reciever())
        self.ui.checkButtonReciever.clicked.connect(lambda : self.verify_sign())

    def choice(self, index, title):
        self.ui.stackedWidget.setCurrentIndex(index) 
        self.setWindowTitle(title)

    def generate_params(self):
        p, q, g = self.dsa.generate_params()
        self.ui.p_sender.setText('p:' + str(p))
        self.ui.q_sender.setText('q:' + str(q))
        self.ui.g_sender.setText('g:' + str(g))

    def upload_params(self):
        path = QFileDialog.getOpenFileName(filter='Параметры (*.params *.PARAMS)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        data = WorkFile(path).read()
        if data.get('p') is None or data.get('q') is None or data.get('g') is None:
            return QMessageBox.critical(self, self.windowTitle(), 'Некорректный файл параметров')
        self.dsa.p = data.get('p')
        self.dsa.q = data.get('q')
        self.dsa.g = data.get('g')
        self.ui.p_sender.setText('p:' + str(self.dsa.p))
        self.ui.q_sender.setText('q:' + str(self.dsa.q))
        self.ui.g_sender.setText('g:' + str(self.dsa.g))

    def __check_params(method):
        def check_exec(self, *args, **kwargs):
            if self.dsa.p is None or self.dsa.q is None or self.dsa.g is None:
                return QMessageBox.critical(self, self.windowTitle(), 'Параметры отсутствуют')
            else:
                return method(self, *args,**kwargs)
        return check_exec

    def __check_keys(method):
        def check_exec(self, *args, **kwargs):
            if self.dsa.x is None or self.dsa.y is None:
                return QMessageBox.critical(self, self.windowTitle(), 'Ключи отсутствуют')
            else:
                return method(self, *args, **kwargs)
        return check_exec

    def __check_sign(method):
        def check_exec(self, *args, **kwargs):
            if self.dsa.r is None or self.dsa.s is None:
                return QMessageBox.critical(self, self.windowTitle(), 'Подпись отсутствует')
            else:
                return method(self, *args, **kwargs)
        return check_exec

    @__check_params
    def save_params(self):
        path = QFileDialog.getSaveFileName(filter='Параметры (*.params *.PARAMS)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        WorkFile(path).write({'p':self.dsa.p, 'q': self.dsa.q, 'g':self.dsa.g})

    @__check_params
    def check_prime(self, num):
        if self.dsa.test.is_prime(num):
            return QMessageBox.information(self, self.windowTitle(), 'Число простое')
        else:
            return QMessageBox.information(self, self.windowTitle(), 'Число составное')

    @__check_params
    def generate_keys(self):
        x, y = self.dsa.generate_keys()
        self.ui.senderPublicKey.setText('Открытый ключ:' + str(x))
        self.ui.senderPrivatKey.setText('Закрытый ключ:' + str(y))

    @__check_params
    def upload_keys(self):
        path = QFileDialog.getOpenFileName(filter='Ключи (*.keys *.KEYS)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        data = WorkFile(path).read()
        if data.get('x') is None or data.get('y') is None:
            return QMessageBox.critical(self, self.windowTitle(), 'Некорректный файл ключей')
        self.dsa.x = data.get('x')
        self.dsa.y = data.get('y')
        self.ui.senderPublicKey.setText('Открытый ключ:' + str(self.dsa.x))
        self.ui.senderPrivatKey.setText('Закрытый ключ:' + str(self.dsa.y))
    
    @__check_keys
    def save_keys(self):
        path = QFileDialog.getSaveFileName(filter='Параметры (*.keys *.KEYS)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        WorkFile(path).write({'x':self.dsa.x, 'y': self.dsa.y})

    @__check_params
    @__check_keys
    def sign_mes(self):
        if self.ui.textMessageSender.toPlainText().strip() == "":
            return QMessageBox.critical(self, self.windowTitle(), 'Введите подписываемый текст')
        self.M = self.ui.textMessageSender.toPlainText().strip()
        k, m, r, s = self.dsa.sign(self.M)
        self.ui.senderRandK.setText('k:' + str(k))
        self.ui.senderMessageHash.setText('Хэш сообщения:' + str(m))
        self.ui.r_sender.setText('r:' + str(r))
        self.ui.s_sender.setText('s:' + str(s))

    @__check_sign
    def save_sign(self):
        path = QFileDialog.getSaveFileName(filter='Параметры (*.sign *.SIGN)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        WorkFile(path).write({'text':self.M, 'y': self.dsa.y, 'r': self.dsa.r, 's': self.dsa.s})
    
    def upload_params_reciver(self):
        path = QFileDialog.getOpenFileName(filter='Параметры (*.params *.PARAMS)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        data = WorkFile(path).read()
        if data.get('p') is None or data.get('q') is None or data.get('g') is None:
            return QMessageBox.critical(self, self.windowTitle(), 'Некорректный файл параметров')
        self.dsa.p = data.get('p')
        self.dsa.q = data.get('q')
        self.dsa.g = data.get('g')
        self.ui.p_Reciever.setText('p:' + str(self.dsa.p))
        self.ui.q_Reciever.setText('q:' + str(self.dsa.q))
        self.ui.g_Reciever.setText('g:' + str(self.dsa.g))

    def upload_sign_message(self):
        path = QFileDialog.getOpenFileName(filter='Параметры (*.sign *.SIGN)')[0] #TODO Суффикс
        if path == '':
            return QMessageBox.information(self, self.windowTitle(), 'Пустой путь к файлу')
        data = WorkFile(path).read()
        if data.get('text') is None or data.get('y') is None or data.get('r') is None or data.get('s') is None:
            return QMessageBox.critical(self, self.windowTitle(), 'Некорректный файл Подписи')
        self.M = data.get('text')
        self.dsa.y = data.get('y')
        self.dsa.r = data.get('r')
        self.dsa.s = data.get('s')
        self.ui.publicKeySender.setText('Открытый ключ:' + str(self.dsa.y))
        self.ui.r_reciever.setText('r:' + str(self.dsa.r))
        self.ui.s_reciever.setText('s:' + str(self.dsa.s))
        self.ui.textMessage.setPlainText(self.M)

    @__check_params
    @__check_sign
    def calculate_params_reciever(self):
        m, w, u1, u2, v = self.dsa.calculate_params(self.M)
        self.ui.HashMessageReciever.setText('Хэш сообщения:' + str(m))
        self.ui.w_Reciever.setText('w:' + str(w))
        self.ui.u1_Reciever.setText('u1:' + str(u1))
        self.ui.u2_Reciever.setText('u2:' + str(u2))
        self.ui.v_Reciever.setText('v:' + str(v))

    def verify_sign(self):
        if self.dsa.r is None or self.dsa.v is None:
            return QMessageBox.critical(self, self.windowTitle(), 'Один из параметров отсутствует')
        if self.dsa.verify():
            return QMessageBox.information(self, self.windowTitle(), 'Подпись верна')
        else:
            return QMessageBox.critical(self, self.windowTitle(), 'Подпись неверна')

    def about(self):
        return QMessageBox.aboutQt(self, self.windowTitle())