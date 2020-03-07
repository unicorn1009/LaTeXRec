import os

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QFileDialog

from Ui.mainWIndow import Ui_MainWindow
from Ui.setting import Ui_Dialog
from YamlHandler import YamlHandler
from recognize import ImgToLatex


class QmyWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗体
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status_label = QLabel()
        self.status_label.setMinimumWidth(150)
        self.ui.statusbar.addWidget(self.status_label)

        # self.ui.btn_readFromClipboard.clicked.connect(self.read_from_clipboard)
        self.ui.btn_setting.clicked.connect(self.open_setting)
        self.ui.btn_copy1.clicked.connect(self.copy_result_from_latex1)
        self.ui.btn_copy2.clicked.connect(self.copy_result_from_latex2)
        self.ui.btn_copy3.clicked.connect(self.copy_result_from_latex3)
        self.ui.btn_copy4.clicked.connect(self.copy_result_from_latex4)
        self.ui.btn_selectImg.clicked.connect(self.select_img)
        self.ui.btn_readFromClipboard.clicked.connect(self.read_from_clipboard)

    def select_img(self):
        fname, _ = QFileDialog.getOpenFileName(self, "选择图片", ".", "(*.jpg | *.png)")
        if fname != "":
            # print(fname)
            self.ui.imgPrevie.setPixmap(QPixmap(fname))
            self.recognize(fname)

    def copy_result_from_latex1(self):
        self.ui.latex1.selectAll()
        self.ui.latex1.copy()

    def copy_result_from_latex2(self):
        self.ui.latex2.selectAll()
        self.ui.latex2.copy()

    def copy_result_from_latex3(self):
        self.ui.latex3.selectAll()
        self.ui.latex3.copy()

    def copy_result_from_latex4(self):
        self.ui.latex4.selectAll()
        self.ui.latex4.copy()

    def read_from_clipboard(self):
        if not QApplication.clipboard().image().isNull():
            self.ui.imgPrevie.setPixmap(QPixmap(QApplication.clipboard().image()))
            QApplication.clipboard().image().save("beforeRec.png")
            self.recognize("./beforeRec.png")
        else:
            self.ui.imgPrevie.setText("未识别到剪切板中的图片资源")
            self.ui.latex1.clear()
            self.ui.latex2.clear()
            self.ui.latex3.clear()
            self.ui.latex4.clear()
            self.ui.showimg.clear()
            self.status_label.setText("识别准确率：0")
            # pe = QPalette()
            # pe.setColor(QPalette.Window, QColor("#222222"))
            # # pe.setColor(QPalette.Background,Qt.blue)
            # self.ui.imgPrevie.setPalette(pe)

    def open_setting(self):
        setting_dialog = QmySettingDialog(self)
        setting_dialog.show()

    def recognize(self, imgPath):
        # 检查是否存在配置文件
        if os.path.exists("myConfig.yaml") and YamlHandler("myConfig.yaml").get_data("appId") != "" and YamlHandler("myConfig.yaml").get_data("appKey") != "":
            try:
                t = ImgToLatex()
                result = t.do_recognize(imgPath)
                self.ui.latex1.clear()
                self.ui.latex2.clear()
                self.ui.latex3.clear()
                self.ui.latex4.clear()
                self.ui.latex1.setText(result['latex_simplified'])
                self.ui.latex2.setText(r"\(" + result['latex_simplified'] + r"\)")
                self.ui.latex3.setText(r"$$ " + result['latex_simplified'] + r" $$")
                self.ui.latex4.setText(r"\begin{equation} " + result['latex_simplified'] + r" \end{equation}")
                # 创建状态栏上的组件
                self.status_label.setText("预估准确率： {0:.2f}%".format(result["latex_confidence_rate"] * 100))
                # 输出识别后的latex公式图片
                # image_bytes = render_latex(result['latex_simplified'], fontsize=10, dpi=300, format_='png')
                image_bytes = requests.get("https://latex.codecogs.com/png.latex?" + result['latex_simplified']).content
                with open('result.png', 'wb') as image_file:
                    image_file.write(image_bytes)
                output_png = QPixmap('./result.png')
                self.ui.showimg.setPixmap(output_png)
            except:
                self.ui.latex1.clear()
                self.ui.latex2.clear()
                self.ui.latex3.clear()
                self.ui.latex4.clear()
                self.ui.showimg.clear()
                self.status_label.setText("识别准确率：0")
        else:
            self.open_setting()


class QmySettingDialog(QDialog):
    app_id = None
    app_key = None

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗体
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("设置")
        self.setWindowModality(Qt.ApplicationModal)
        if os.path.exists("myConfig.yaml"):
            self.ui.lineEdit_app_id.setText(YamlHandler("myConfig.yaml").get_data("appId"))
            self.ui.lineEdit_app_key.setText(YamlHandler("myConfig.yaml").get_data("appKey"))
        self.accepted.connect(self.save_setting)

        # 两个变量保持id和key

    def save_setting(self):
        self.app_id = str(self.ui.lineEdit_app_id.text())
        self.app_key = str(self.ui.lineEdit_app_key.text())
        config = YamlHandler("myConfig.yaml")
        config_str = {"appId": self.app_id, "appKey": self.app_key}
        config.write_data(config_str)
