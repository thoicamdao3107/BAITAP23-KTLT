import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from baitap23Ext import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Tạo đối tượng UI và thiết lập giao diện
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Hiển thị cửa sổ chính
    MainWindow.show()

    # Chạy ứng dụng
    sys.exit(app.exec())
