# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1811, 899)
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 0.04em solid #eff0f1;\n"
"    background-color: #31363b;\n"
"    alternate-background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    padding: 0.1em;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color: #3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QWidget:disabled:hover\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 0.23em;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.09em;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #b0b0b0;\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    min-height: 1.2em;\n"
"    border: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    margin-top: 0.5em;\n"
"    padding-top: 1em;\n"
"}\n"
""
                        "\n"
"QGroupBox:focus\n"
"{\n"
"    border: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"    top: -1.6em;\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: top center;\n"
"    background: #31363b;\n"
"    padding-left: 0.2em;\n"
"    padding-right: 0.2em;\n"
"}\n"
"\n"
"QCheckBox::indicator, QTreeView::indicator\n"
"{\n"
"    width: 1em;\n"
"    height: 1em;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QTreeView::indicator:unchecked,\n"
"QTreeView::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QTreeView::indicator:unchecked:hover,\n"
"QTreeView::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"    b"
                        "order: none;\n"
"    border-image: url(:/dark/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QTreeView::indicator:checked,\n"
"QGroupBox::indicator:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QTreeView::indicator:checked:hover,\n"
"QTreeView::indicator:checked:focus,\n"
"QTreeView::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QTreeView::indicator:indeterminate\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed,\n"
"QTreeVi"
                        "ew::indicator:indeterminate:focus,\n"
"QTreeView::indicator:indeterminate:hover,\n"
"QTreeView::indicator:indeterminate:pressed\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,\n"
"QTreeView::indicator:indeterminate:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_indeterminate_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QTreeView::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QTreeView::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 0.23em;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 0.09em;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
""
                        "QRadioButton::indicator\n"
"{\n"
"    width: 1em;\n"
"    height: 1em;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:focus\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"    outline: none;\n"
"    border-image: url(:/dark/radio_checked_disabled.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:"
                        "unchecked:disabled\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #31363b;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    color: #eff0f1;\n"
"    margin-bottom: -0.09em;\n"
"    padding-bottom: 0.09em;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    color: #eff0f1;\n"
"    margin: 0.09em;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 0.23em;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    /* Add extra padding on the right for the QMenu arrow */\n"
"    padding: 0.23em 1.5em 0.23em 1.3em;\n"
"    border: 0.09em solid transparent;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #3daee9;\n"
"}\n"
"\n"
""
                        "QMenu::item:selected:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #76797c;\n"
"}\n"
"\n"
"QMenu::indicator\n"
"{\n"
"    width: 1em;\n"
"    height: 1em;\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/checkbox_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checke"
                        "d\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected\n"
"{\n"
"    border-image: url(:/dark/radio_checked.svg);\n"
"}\n"
"\n"
"QMenu::right-arrow\n"
"{\n"
"    margin: 0.23em;\n"
"    border-image: url(:/dark/right_arrow.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"}\n"
"\n"
"QMenu::right-arrow:disabled\n"
"{\n"
"    border-image: url(:/dark/right_arrow_disabled.svg);\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #31363b;\n"
"    color: #eff0f1;\n"
"    border: 0.09em solid #31363b;\n"
"    border-radius: 0.09em;\n"
"}\n"
"\n"
"QMenuBar::item:focus:!disabled\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QTabWidget:focus,\n"
"QCheckBox:focus,\n"
"QRadioButton:focus,\n"
"QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #1d2023;\n"
"    padding: 0.23em;\n"
"    border-style: solid;\n"
"    border: 0.04em solid #76797c;\n"
"    border-radius: 0.09e"
                        "m;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0.09em;\n"
"    border: 0.09em solid #76797c;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/**\n"
" *  This is the background for the box in the bottom-right corner\n"
" *  whene both scrollbars are active.\n"
" */\n"
"QAbstractScrollArea::corner\n"
"{\n"
"    background: #31363b;\n"
"}\n"
"\n"
"/**\n"
" *  Can't do the KDE style of where the scrollbar handle\n"
" *  becomes light on the hover, and only when the handle\n"
" *  is hovered does it become stylized. This is because\n"
" *  both the handle and the background events are treated\n"
" *  together.\n"
" */\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color: #1d2023;\n"
"    height: 0.65em;\n"
"    margin: 0.13em 0.65em 0.13em 0.65em;\n"
"    border: 0.04em transparent #1d2023;\n"
"    border-radius: 0.17em;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover\n"
"{\n"
"    background-color: #76797c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    "
                        "background-color: #3daee9;\n"
"    border: 0.04em solid #3daee9;\n"
"    min-width: 0.5em;\n"
"    border-radius: 0.17em;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0em 0.13em 0em 0.13em;\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    width: 0.41em;\n"
"    height: 0.41em;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0em 0.13em 0em 0.13em;\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    width: 0.41em;\n"
"    height: 0.41em;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    width: 0.41em;\n"
"    height: 0.41em;\n"
"    subcontrol-position: right;\n"
"    subcontrol-"
                        "origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    width: 0.41em;\n"
"    height: 0.41em;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #1d2023;\n"
"    width: 0.65em;\n"
"    margin: 0.65em 0.13em 0.65em 0.13em;\n"
"    border: 0.04em transparent #1d2023;\n"
"    border-radius: 0.17em;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover\n"
"{\n"
"    background-color: #76797c;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.04em solid #3daee9;\n"
"    min-height: 0.5em;\n"
"    border-radius: 0.17em;\n"
"}\n"
"\n"
"QScrollBar::"
                        "handle:vertical:hover\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 0.13em 0em 0.13em 0em;\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    height: 0.41em;\n"
"    width: 0.41em;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0.13em 0em 0.13em 0em;\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    height: 0.41em;\n"
"    width: 0.41em;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    height: 0.41em;\n"
"    width: 0.41em;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);"
                        "\n"
"    height: 0.41em;\n"
"    width: 0.41em;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #1d2023;\n"
"    color: #eff0f1;\n"
"    border: 0.04em solid #76797c;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #1d2023;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.09em;\n"
"    border: 0.04em solid #76797c;\n"
"}\n"
"\n"
"QSizeGrip\n"
"{\n"
"    border-image: url(:/dark/sizegrip.svg);\n"
"    width: 0.5em;\n"
"    height: 0.5em;\n"
"}\n"
"\n"
"/**\n"
" *  Set the separator to be transparent, since the dock has a border.\n"
" *  On PyQt6, neither the border nor the background seem to be respected.\n"
" */\n"
"QMainWindow::separator\n"
"{\n"
"    border: 0.09em transparent #76797c;\n"
"   "
                        " background: transparent;\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 0.09em;\n"
"    background-color: #76797c;\n"
"    padding-left: 0.2em;\n"
"    margin-top: 0.2em;\n"
"    margin-bottom: 0.2em;\n"
"    margin-left: 0.41em;\n"
"    margin-right: 0.41em;\n"
"}\n"
"\n"
"QFrame[frameShape=\"2\"], /* QFrame::Panel == 0x0003 */\n"
"QFrame[frameShape=\"3\"], /* QFrame::WinPanel == 0x0003 */\n"
"QFrame[frameShape=\"4\"], /* QFrame::HLine == 0x0004 */\n"
"QFrame[frameShape=\"5\"], /* QFrame::VLine == 0x0005 */\n"
"QFrame[frameShape=\"6\"]  /* QFrame::StyledPanel == 0x0006 */\n"
"{\n"
"    border-width: 0.04em;\n"
"    padding: 0.09em;\n"
"    border-style: solid;\n"
"    border-color: #31363b;\n"
"    background-color: #76797c;\n"
"    border-radius: 0.23em;\n"
"}\n"
"\n"
"/* Provide highlighting for frame objects. */\n"
"QFrame[frameShape=\"2\"]:hover,\n"
"QFrame[frameShape=\"3\"]:hover,\n"
"QFrame[frameShape=\"4\"]:hover,\n"
"QFrame[frameShape=\"5\"]:hover,\n"
"QFrame[frameShape=\"6\"]:hover\n"
"{\n"
""
                        "    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"/* Don't provide an outline if we have a widget that takes up the space. */\n"
"QFrame[frameShape] QAbstractItemView:hover\n"
"{\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"/**\n"
" *  Note: I can't really change the background of the toolbars\n"
" *  independently, since KDE Breeze has different colors for the\n"
" *  window bar and the rest of the UI. The top toolbar uses\n"
" *  the window style, and the rest use the application style,\n"
" *  which we can't do.\n"
" */\n"
"QToolBar\n"
"{\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar:horizontal\n"
"{\n"
"    background: 0.09em solid #31363b;\n"
"}\n"
"\n"
"QToolBar:vertical\n"
"{\n"
"    background: 0.09em solid #31363b;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    border-image: url(:/dark/hmovetoolbar.svg);\n"
"}\n"
"\n"
"QToolBar::handle:vertical\n"
"{\n"
"    border-image: url(:/dark/vmovetoolbar.svg);\n"
"}\n"
"\n"
"QToolBar::separator:horizontal\n"
"{\n"
"    border-image: url(:/dark"
                        "/hseptoolbar.svg);\n"
"}\n"
"\n"
"QToolBar::separator:vertical\n"
"{\n"
"    border-image: url(:/dark/vseptoolbar.svg);\n"
"}\n"
"\n"
"QToolBar QToolButton\n"
"{\n"
"    font-weight: bold;\n"
"    min-height: 1em;\n"
"    min-width: 2em;\n"
"    border: 0.04em transparent black;\n"
"    padding-left: 0.2em;\n"
"    padding-right: 0.3em;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QToolBar QToolButton:pressed\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"    /* The padding doesn't inherit from `QToolBar QToolButton`, so leave it in. */\n"
"    padding-left: 0.2em;\n"
"    padding-right: 0.3em;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border: 0.04em solid #76797c;\n"
"    padding: 0.23em;\n"
"    border-radius: 0.09em;\n"
"    outline: none;\n"
"    min-height: 1.1em;\n"
"}\n"
"\n"
"QComboBox:open,\n"
"QPushButton:open\n"
"{\n"
"    border-width: 0.04em;\n"
"    border-color: #76797c;\n"
"}\n"
"\n"
""
                        "QComboBox:closed,\n"
"QPushButton:closed\n"
"{\n"
"    border-width: 0.04em;\n"
"    border-color: #76797c;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 0.04em;\n"
"    border-color: #76797c;\n"
"    border-style: solid;\n"
"    padding-top: 0.23em;\n"
"    padding-bottom: 0.23em;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.04em;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #454a4f;\n"
"    padding-top: -0.65em;\n"
"    padding-bottom: -0.74em;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    border: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    padding: 0.23em;\n"
"    min-width: 2.5em;\n"
"}\n"
"\n"
"QComboBox:editable\n"
"{\n"
"    background-color: #1d2023;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background-color: #626568;\n"
"    border: 0.04em solid #76797c;\n"
"    color"
                        ": #eff0f1;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.04em solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"    background-color: #626568;\n"
"    border: 0.04em solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QComboBox:focus,\n"
"QAbstractSpinBox:hover,\n"
"QAbstractSpinBox:focus,\n"
"QLineEdit:hover,\n"
"QLineEdit:focus,\n"
"QTextEdit:hover,\n"
"QTextEdit:focus,\n"
"QPlainTextEdit:hover,\n"
"QPlainTextEdit:focus,\n"
"QAbstractView:hover,\n"
"QTreeView:hover,\n"
"QTreeView:focus\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QComboBox:hover:pressed:!editable,\n"
"QPushButton:hover:pressed,\n"
"QAbstractSpinBox:hover:pressed,\n"
"QLineEdit:hover:pressed,\n"
"QTextEdit:hover:pressed,\n"
"QPlainTextEdit:hover:pressed,\n"
"QAbstractView:hover:pressed,\n"
"QTreeView:hover:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"}\n"
"\n"
"QComboBox:hover:pressed:edita"
                        "ble\n"
"{\n"
"    background-color: #1d2023;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    /* This happens for the drop-down menu always, whether editable or not.*/\n"
"    background-color: #1d2023;\n"
"    selection-background-color: #2a79a3;\n"
"    outline-color: 0em;\n"
"    border-radius: 0.09em;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 0.65em;\n"
"\n"
"    border-left-width: 0em;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 0.13em;\n"
"    border-bottom-right-radius: 0.13em;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"    margin-right: 0.41em;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"    margin-right: 0.41em;"
                        "\n"
"}\n"
"\n"
"QAbstractSpinBox\n"
"{\n"
"    padding: 0.23em;\n"
"    border: 0.09em solid #76797c;\n"
"    background-color: #1d2023;\n"
"    color: #eff0f1;\n"
"    border-radius: 0.09em;\n"
"    min-width: 3em;\n"
"    min-height: 1em;\n"
"}\n"
"\n"
"QAbstractSpinBox:hover\n"
"{\n"
"    border: 0.09em solid #3daee9;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button,\n"
"QAbstractSpinBox:up-button:hover\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    padding-right: 0.1em;\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button,\n"
"QAbstractSpinBox:down-button:hover\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center left;\n"
"    padding-left: 0.1em;\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow\n"
"{\n"
"    border-image: url(:/dark/up_arrow.svg);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:disa"
                        "bled,\n"
"QAbstractSpinBox::up-arrow:off\n"
"{\n"
"    border-image: url(:/dark/up_arrow_disabled.svg);\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    border-image: url(:/dark/up_arrow_hover.svg);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow\n"
"{\n"
"    border-image: url(:/dark/down_arrow.svg);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    border-image: url(:/dark/down_arrow_disabled.svg);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:!off:!disabled:hover\n"
"{\n"
"    border-image: url(:/dark/down_arrow_hover.svg);\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    min-width: 4em;\n"
"}\n"
"\n"
"/**\n"
" *  `QCalendarWidget QAbstractItemView:enabled` sets the color, background\n"
" *  color, and selection color for active dates in the view.\n"
" *  `QCalendarWidget QAbstractItemView:enabled` sets the disabled dates.\n"
" */\n"
"QCalendarWidget QAbstractItemView:enabled\n"
"{\n"
"    color: #eff0f1;\n"
"    selection-color: #eff0f1;\n"
"    sele"
                        "ction-background-color: #3daee9;\n"
"}\n"
"\n"
"/* Won't take hover events. */\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth\n"
"{\n"
"    border-image: url(:/dark/calendar_next.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"    icon-size: 0px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth\n"
"{\n"
"    border-image: url(:/dark/calendar_previous.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"    icon-size: 0px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox\n"
"{\n"
"    max-height: 1.5em;\n"
"    min-width: 3.5em;\n"
"    margin: 0em;\n"
"    margin-top: 0.2em;\n"
"    padding: 0em;\n"
"    outline: 0em;\n"
"    padding-left: 0.5em;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"/* BORDERS */\n"
"QTabWidget::pane\n"
"{\n"
"    padding: 0.23em;\n"
"    margin: 0.04em;\n"
"}\n"
"\n"
"QTabWidget::pane:top\n"
"{\n"
"    border: 0.04em solid #76797c;\n"
"    top: -0.04em;\n"
"}\n"
"\n"
"QTabWidget::pane:bottom\n"
"{\n"
"    border: 0.04em solid #7679"
                        "7c;\n"
"    bottom: -0.04em;\n"
"}\n"
"\n"
"QTabWidget::pane:left\n"
"{\n"
"    border: 0.04em solid #76797c;\n"
"    left: -0.04em;\n"
"}\n"
"\n"
"QTabWidget::pane:right\n"
"{\n"
"    border: 0.04em solid #76797c;\n"
"    right: -0.04em;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 0.23em;\n"
"    border-radius: 0.13em;\n"
"    /**\n"
"     *  Note: this is the underline for each tab title. It's not\n"
"     *  documented, and this took forever to track down. At least\n"
"     *  10 hours have been wasted trying to turn off this line,\n"
"     *  do not deleted this comment.\n"
"     */\n"
"    selection-color: transparent;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0em transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button\n"
"{\n"
"    /* Doesn't seem possible to resize these buttons */\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    image: url(:/dark/close.svg);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: "
                        "url(:/dark/close_hover.svg);\n"
"}\n"
"\n"
"QTabBar::close-button:pressed\n"
"{\n"
"    image: url(:/dark/close_pressed.svg);\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top,\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:top:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.04em transparent black;\n"
"    border-left: 0.04em solid #76797c;\n"
"    border-right: 0.04em solid #76797c;\n"
"    border-top: 0.09em solid #3daee9;\n"
"    background-color: #31363b;\n"
"    padding: 0.23em;\n"
"    min-width: 50px;\n"
"    border-radius: 0.09em;\n"
"    border-bottom-left-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #2c3034;\n"
"    border: 0.04em transparent black;\n"
"    border-right: 0.04em solid #76797c;\n"
"    border-bottom: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    border-bottom-left-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:top:next-selec"
                        "ted\n"
"{\n"
"    border-right: 0.04em transparent #2c3034;\n"
"    border-bottom-left-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-bottom-left-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-bottom-left-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom,\n"
"QTabBar::tab:bottom:last,\n"
"QTabBar::tab:bottom:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.04em transparent black;\n"
"    border-left: 0.04em solid #76797c;\n"
"    border-right: 0.04em solid #76797c;\n"
"    border-bottom: 0.09em solid #3daee9;\n"
"    background-color: #31363b;\n"
"    padding: 0.23em;\n"
"    min-width: 50px;\n"
"    border-radius: 0.09em;\n"
""
                        "    border-top-left-radius: 0em;\n"
"    border-top-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #2c3034;\n"
"    border: 0.04em transparent black;\n"
"    border-top: 0.04em solid #76797c;\n"
"    border-right: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-top-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:next-selected\n"
"{\n"
"    border-right: 0.04em transparent #2c3034;\n"
"    border-top-left-radius: 0em;\n"
"    border-top-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-top-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-top-right-radius: 0"
                        "em;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left,\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:left:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.04em transparent black;\n"
"    border-top: 0.09em solid #3daee9;\n"
"    border-bottom: 0.04em solid #76797c;\n"
"    border-left: 0.04em solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.23em;\n"
"    min-height: 50px;\n"
"    border-radius: 0.09em;\n"
"    border-top-right-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #2c3034;\n"
"    border: 0.04em transparent black;\n"
"    border-top: 0.04em solid #76797c;\n"
"    border-right: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    border-top-right-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:left:previous-selected\n"
"{\n"
"    border-top: 0.04em transparent #2c3034;\n"
"    border-top-right-radius: 0em;\n"
"    border-bottom"
                        "-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-right-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-right-radius: 0em;\n"
"    border-bottom-right-radius: 0em;\n"
"}\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right,\n"
"QTabBar::tab:right:last,\n"
"QTabBar::tab:right:only-one\n"
"{\n"
"    color: #eff0f1;\n"
"    border: 0.04em transparent black;\n"
"    border-top: 0.09em solid #3daee9;\n"
"    border-bottom: 0.04em solid #76797c;\n"
"    border-right: 0.04em solid #76797c;\n"
"    background-color: #31363b;\n"
"    padding: 0.23em;\n"
"    min-height: 50px;\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-bottom-left-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
""
                        "    color: #eff0f1;\n"
"    background-color: #2c3034;\n"
"    border: 0.04em transparent black;\n"
"    border-top: 0.04em solid #76797c;\n"
"    border-left: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-bottom-left-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:right:previous-selected\n"
"{\n"
"    border-top: 0.04em transparent #2c3034;\n"
"    border-top-left-radius: 0em;\n"
"    border-bottom-left-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-bottom-left-radius: 0em;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:first:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    border-radius: 0.09em;\n"
"    border-top-left-radius: 0em;\n"
"    border-bottom-left-radius: 0em;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled\n"
"{\n"
"    border-image: url(:/dark/right_arrow.svg);\n"
""
                        "    width: 0.5em;\n"
"    height: 0.8em;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled\n"
"{\n"
"    border-image: url(:/dark/left_arrow.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled\n"
"{\n"
"    border-image: url(:/dark/right_arrow_disabled.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled\n"
"{\n"
"    border-image: url(:/dark/left_arrow_disabled.svg);\n"
"    width: 0.5em;\n"
"    height: 0.8em;\n"
"}\n"
"\n"
"QDockWidget\n"
"{\n"
"    background: #31363b;\n"
"    /**\n"
"     *  It doesn't seem possible to change the border of the\n"
"     *  QDockWidget without changing the content margins.\n"
"     */\n"
"    /**\n"
"     *  This is a bug fix so we can handle hover, pressed, and other events.\n"
"     *  Reference: https://stackoverflow.com/questions/32145080/qdockwidget-float-close-button-hover-images\n"
"     */\n"
"    titlebar-close-icon: url(:/dark/transparent.svg);\n"
"  "
                        "  titlebar-normal-icon: url(:/dark/transparent.svg);\n"
"}\n"
"\n"
"/**\n"
" *  Don't style the title, since it gives a weird, missing border\n"
" *  around the rest of the dock widget, which the remaining border\n"
" *  cannot be removed.\n"
" *\n"
" *  There is a bug in Qt6, where the icons are small. It doesn't\n"
" *  change if we use `image` instead of `border-image`, nor if we\n"
" *  use `qproperty-icon`, etc. The icon seem to be half the size\n"
" *  of our desired values.\n"
" */\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button\n"
"{\n"
"    border: 0.04em solid transparent;\n"
"    border-radius: 0.09em;\n"
"    background: transparent;\n"
"    /* Maximum icon size for buttons */\n"
"    icon-size: 14px;\n"
"}\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    image: url(:/dark/undock.svg);\n"
"}\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"    image: url(:/dark/undock_hover.svg);\n"
"}\n"
"\n"
"/* The :pressed events don't register, "
                        "seems to be a Qt bug. */\n"
"QDockWidget::float-button:pressed\n"
"{\n"
"    image: url(:/dark/undock_hover.svg);\n"
"}\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"    border-image: url(:/dark/transparent.svg);\n"
"    image: url(:/dark/close.svg);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"    image: url(:/dark/close_hover.svg);\n"
"}\n"
"\n"
"/* The :pressed events don't register, seems to be a Qt bug. */\n"
"QDockWidget::close-button:pressed\n"
"{\n"
"    image: url(:/dark/close_pressed.svg);\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView\n"
"{\n"
"    background-color: #1d2023;\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QTreeView:!selected,\n"
"QListView:selected,\n"
"QListView:!selected\n"
"{\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings\n"
"{\n"
"    border-image: url(:/dark/vline.svg);\n"
"    image: none;\n"
"}\n"
"\n"
"/* These branch indicators don't scale */\n"
"TreeView::branch:!has-siblings\n"
"{\n"
"    border-image: none;\n"
""
                        "    image: none;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/dark/branch_more.svg);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item\n"
"{\n"
"    border-image: url(:/dark/branch_end.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings\n"
"{\n"
"    image: url(:/dark/branch_closed.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover\n"
"{\n"
"    image: url(:/dark/branch_closed_hover.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:open:has-children:!has-siblings\n"
"{\n"
"    border-image: url(:/dark/branch_end_arrow.svg);\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings\n"
"{\n"
"    border-image: url(:/dark/branch_more_arrow.svg);\n"
"}\n"
"\n"
"QTreeView::b"
                        "ranch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings\n"
"{\n"
"    image: url(:/dark/branch_open.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover\n"
"{\n"
"    image: url(:/dark/branch_open_hover.svg);\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    /* Give space for elements aligned left or right. */\n"
"    padding: 0.2em;\n"
"}\n"
"\n"
"QTableView::item,\n"
"QListView::item,\n"
"QTreeView::item\n"
"{\n"
"    padding: 0.13em;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QTableView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: rgba(61, 173, 232, 0.1);\n"
"    outline: 0;\n"
"    color: #eff0f1;\n"
"    padding: 0.13em;\n"
"}\n"
"\n"
"QSlider::handle:horizontal,\n"
"QSlider::handle:vertical\n"
"{\n"
"    background: #1d2023;\n"
"    border: 0.04em solid #626568;\n"
"    width: 0.7em;\n"
"    height: 0.7em;\n"
"    borde"
                        "r-radius: 0.35em;\n"
"}\n"
"\n"
"QSlider:horizontal\n"
"{\n"
"    height: 2em;\n"
"}\n"
"\n"
"QSlider:vertical\n"
"{\n"
"    width: 2em;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    margin: -0.23em 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"    margin: 0 -0.23em;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,\n"
"QSlider::groove:vertical\n"
"{\n"
"    background: #2c3034;\n"
"    border: 0em solid #31363b;\n"
"    border-radius: 0.19em;\n"
"}\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    height: 0.4em;\n"
"}\n"
"\n"
"QSlider::groove:vertical\n"
"{\n"
"    width: 0.4em;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:horizontal:focus,\n"
"QSlider::handle:vertical:hover,\n"
"QSlider::handle:vertical:focus\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:!focus:!hover,\n"
"QSlider::handle:vertical:!focus:!hover\n"
"{\n"
"    border: 0.04em solid #626568;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal,\n"
"QSlider::add-page:vertical\n"
"{\n"
""
                        "    background: #3daee9;\n"
"    border-radius: 0.19em;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal,\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    background: #626568;\n"
"    border-radius: 0.19em;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 0.04em solid #76797c;\n"
"    border-radius: 0.09em;\n"
"    margin: 0.23em;\n"
"    padding: 0.23em;\n"
"    padding-top: 0.1em;\n"
"    padding-right: 1.2em;\n"
"    min-height: 1.1em;\n"
"}\n"
"\n"
"QToolButton::right-arrow,\n"
"QToolButton::left-arrow,\n"
"QToolButton::up-arrow,\n"
"QToolButton::down-arrow\n"
"{\n"
"    /* Undo the padding when we have an arrow */\n"
"    padding-right: -1.2em;\n"
"}\n"
"\n"
"QToolButton::right-arrow\n"
"{\n"
"    image: url(:/dark/right_arrow.svg);\n"
"}\n"
"\n"
"QToolButton::left-arrow\n"
"{\n"
"    image: url(:/dark/left_arrow.svg);\n"
"}\n"
"\n"
"QToolButton::up-arrow\n"
"{\n"
"    image: url(:/dark/up_arrow.svg);\n"
"}\n"
"\n"
"QToolButton::down-arrow\n"
"{\n"
"    image: url(:/dark/down"
                        "_arrow.svg);\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QToolButton::menu-indicator\n"
"{\n"
"    border-image: none;\n"
"    image: url(:/dark/down_arrow.svg);\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"    top: -0.7ex;\n"
"    left: -0.09em;\n"
"    padding-right: 0.09em;\n"
"}\n"
"\n"
"QToolButton::menu-arrow\n"
"{\n"
"    border-image: none;\n"
"    image: url(:/dark/down_arrow.svg);\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QToolButton::menu-button\n"
"{\n"
"    border-top-right-radius: 0.5em;\n"
"    border-bottom-right-radius: 0.5em;\n"
"    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */\n"
"    width: 1.3em;\n"
"    padding: 0.23em;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button::menu-arrow\n"
"{\n"
"    left: -0.09em;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover\n"
"{\n"
"    background-color: transparent;\n"
""
                        "}\n"
"\n"
"QToolButton:checked,\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: #3daee9;\n"
"    padding: 0.23em;\n"
"    padding-right: 1.2em;\n"
"    min-height: 1.3em;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 0.23em;\n"
"    outline: none;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 0em solid black;\n"
"    gridline-color: #31363b;\n"
"    background-color: #1d2023;\n"
"}\n"
"\n"
"QTableView:!selected,\n"
"QTableView:selected\n"
"{\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border-radius: 0em;\n"
"}\n"
"\n"
"QAbstractItemView::item\n"
"{\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QAbstractItemView::item:pressed\n"
"{\n"
"    background: #2a79a3;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QAbstractItemView::item:selected:!active\n"
"{\n"
"    background: rgba(61, 173, 232, 0.1);\n"
"}\n"
"\n"
"/* Use background with qlineargradient to avoid ugly border on widget. */\n"
"QAbstractItemV"
                        "iew::item:selected:active\n"
"{\n"
"    background: qlineargradient(\n"
"        x1: 0.5, y1: 0.5\n"
"        x2: 0.5, y2: 1,\n"
"        stop: 0 #2a79a3,\n"
"        stop: 1 #2a79a3\n"
"    );\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QAbstractItemView::item:selected:hover\n"
"{\n"
"    background: qlineargradient(\n"
"        x1: 0.5, y1: 0.5\n"
"        x2: 0.5, y2: 1,\n"
"        stop: 0 #2f88b7,\n"
"        stop: 1 #2f88b7\n"
"    );\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.04em transparent;\n"
"    border-radius: 0em;\n"
"    margin: 0em;\n"
"    padding: 0em;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.04em solid #76797c;\n"
"    color: #eff0f1;\n"
"    padding: 0.23em;\n"
"    padding-top: 0.3em;\n"
"    border-radius: 0em;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 0.04em solid "
                        "#76797c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0.04em solid #76797c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #ffffff;\n"
"    background-color: #334e5e;\n"
"}\n"
"\n"
"/* Note that this doesn't work for QTreeView unless the header is clickable */\n"
"QHeaderView::section:hover,\n"
"QHeaderView::section::horizontal::first:hover,\n"
"QHeaderView::section::horizontal::only-one:hover,\n"
"QHeaderView::section::vertical::first:hover,\n"
"QHeaderView::section::vertical::only-one:hover\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"}\n"
"\n"
"QHeaderView::down-arrow\n"
"{\n"
"    image: url(:/dark/down_arrow.svg);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-top: 0.2em;\n"
"    width: "
                        "0.8em;\n"
"    height: 0.5em;\n"
"}\n"
"\n"
"QHeaderView::up-arrow\n"
"{\n"
"    image: url(:/dark/up_arrow.svg);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-top: 0.2em;\n"
"    width: 0.8em;\n"
"    height: 0.5em;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section\n"
"{\n"
"    background-color: #31363b;\n"
"    border: 0.04em transparent #76797c;\n"
"    border-top: 0.04em solid #76797c;\n"
"    border-left: 0.04em solid #76797c;\n"
"    border-radius: 0em;\n"
"}\n"
"\n"
"/* No hover event */\n"
"QTableView QTableCornerButton:hover\n"
"{\n"
"    border: 0.04em transparent #76797c;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section:pressed\n"
"{\n"
"    border: 0.04em solid #3daee9;\n"
"    border-radius: 0em;\n"
"}\n"
"\n"
"QToolBox\n"
"{\n"
"    padding: 0.23em;\n"
"    border: 0.09em transparent black;\n"
"}\n"
"\n"
"QToolBox::tab\n"
"{\n"
"    border-bottom: 0.09em solid #76797c;\n"
"    margin-left: 1.5em;\n"
"}\n"
"\n"
"QToolBox::tab:selected,\n"
"QT"
                        "oolBox::tab:hover\n"
"{\n"
"    border-bottom: 0.09em solid #3daee9;\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"    border: 0.09em solid #2c3034;\n"
"    background: -0.5em solid #2c3034;\n"
"    max-width: 0em;\n"
"    max-height: 0em;\n"
"}\n"
"\n"
"/**\n"
" *  It's not possible to get satisfactory rounded borders here.\n"
" *  If you set the border to be negative, while adjusting the\n"
" *  widths, you get an asymmetrical curve which produces an\n"
" *  unappealing border.\n"
" */\n"
"QProgressBar:horizontal,\n"
"QProgressBar:vertical\n"
"{\n"
"    background-color: #626568;\n"
"    border: 0.9em solid #31363b;\n"
"    border-radius: 0.13em;\n"
"    padding: 0em;\n"
"}\n"
"\n"
"QProgressBar:horizontal\n"
"{\n"
"    height: 0.2em;\n"
"    min-width: 6em;\n"
"    text-align: right;\n"
"    padding-left: -0.03em;\n"
"    padding-right: -0.03em;\n"
"    margin-top: 0.2em;\n"
"    margin-bottom: 0.2em;\n"
"    margin-right: 1.3em;\n"
"}\n"
"\n"
"QProgressBar:vertical\n"
"{\n"
"    width: 0.2em;\n"
"    min-heig"
                        "ht: 6em;\n"
"    text-align: bottom;\n"
"    padding-top: -0.03em;\n"
"    padding-bottom: -0.03em;\n"
"    margin-left: 0.2em;\n"
"    margin-right: 0.2em;\n"
"    margin-bottom: 0.41em;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal,\n"
"QProgressBar::chunk:vertical\n"
"{\n"
"    background-color: #3daee9;\n"
"    border: 0.9em transparent;\n"
"    border-radius: 0.08em;\n"
"}\n"
"\n"
"QScrollArea,\n"
"QScrollArea:focus,\n"
"QScrollArea:hover\n"
"{\n"
"    border: 0em solid black;\n"
"}\n"
"\n"
"/* ICONS */\n"
"/**\n"
" *  Qt's built-in icons can look pretty bad if the system theme\n"
" *  is a different color than the current one. For example, when\n"
" *  using a dark theme, with a light UI, the `Ok` button is greyed\n"
" *  out for an about dialog.\n"
" *\n"
" *  QDialogButtonBox will apply for all standard buttons in all standard\n"
" *  widgets, such as QMessageBox, etc. However, we do need to override\n"
" *  standard icons elsewhere.\n"
" *\n"
" *  The rest of the icons make little sense to implement:\n"
""
                        " *      Qt uses native window decorations.\n"
" *      Qt normally uses native file dialogs, which look nicer.\n"
" *      Media controls are used in custom widgets, which aren't standard.\n"
" */\n"
"QDialogButtonBox\n"
"{\n"
"    dialogbuttonbox-buttons-have-icons: true;\n"
"\n"
"    dialog-cancel-icon: url(:/dark/dialog_cancel.svg);\n"
"    dialog-close-icon: url(:/dark/dialog_close.svg);\n"
"    dialog-ok-icon: url(:/dark/dialog_ok.svg);\n"
"    dialog-open-icon: url(:/dark/dialog_open.svg);\n"
"    dialog-reset-icon: url(:/dark/dialog_reset.svg);\n"
"    dialog-save-icon: url(:/dark/dialog_save.svg);\n"
"    /**\n"
"     *  No support yet for overriding saveall.\n"
"     *  dialog-saveall-icon: url(:/dark/dialog_saveall.svg);\n"
"     */\n"
"    dialog-yes-icon: url(:/dark/dialog_ok.svg);\n"
"    dialog-help-icon: url(:/dark/dialog_help.svg);\n"
"    dialog-no-icon: url(:/dark/dialog_no.svg);\n"
"    dialog-apply-icon: url(:/dark/dialog_ok.svg);\n"
"    dialog-discard-icon: url(:/dark/dialog_discard.svg);"
                        "\n"
"}\n"
"\n"
"QMessageBox\n"
"{\n"
"    messagebox-critical-icon: url(:/dark/message_critical.svg);\n"
"    messagebox-information-icon: url(:/dark/message_information.svg);\n"
"    messagebox-question-icon: url(:/dark/message_question.svg);\n"
"    messagebox-warning-icon: url(:/dark/message_warning.svg);\n"
"}\n"
"\n"
"/* Set some styles for these custom dialog buttons */\n"
"QDialogButtonBox QPushButton,\n"
"QMessageBox QPushButton\n"
"{\n"
"    min-height: 1.1em;\n"
"    min-width: 5em;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.tabWidget.setFont(font1)
        self.HOMETAP = QWidget()
        self.HOMETAP.setObjectName(u"HOMETAP")
        self.frame_4 = QFrame(self.HOMETAP)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 110, 571, 611))
        self.frame_4.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"}\n"
"QFrame:hover#frame_4\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.statwaiting = QTableWidget(self.frame_4)
        if (self.statwaiting.columnCount() < 5):
            self.statwaiting.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.statwaiting.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.statwaiting.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.statwaiting.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.statwaiting.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.statwaiting.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.statwaiting.setObjectName(u"statwaiting")
        self.statwaiting.setGeometry(QRect(10, 40, 551, 521))
        font2 = QFont()
        font2.setPointSize(8)
        self.statwaiting.setFont(font2)
        self.statwaiting.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 580, 171, 16))
        self.label_2.setFont(font1)
        self.statlblwaiting = QLabel(self.frame_4)
        self.statlblwaiting.setObjectName(u"statlblwaiting")
        self.statlblwaiting.setGeometry(QRect(190, 580, 171, 16))
        self.statlblwaiting.setFont(font1)
        self.statlblwaiting.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_40 = QLabel(self.frame_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 10, 541, 20))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_40.setFont(font3)
        self.label_40.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.HOMETAP)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(600, 110, 571, 611))
        self.frame_5.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.statinproc = QTableWidget(self.frame_5)
        if (self.statinproc.columnCount() < 5):
            self.statinproc.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.statinproc.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.statinproc.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.statinproc.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.statinproc.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.statinproc.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.statinproc.setObjectName(u"statinproc")
        self.statinproc.setGeometry(QRect(10, 40, 551, 521))
        self.statinproc.setFont(font2)
        self.statinproc.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 580, 171, 16))
        self.label_5.setFont(font1)
        self.statlblinproc = QLabel(self.frame_5)
        self.statlblinproc.setObjectName(u"statlblinproc")
        self.statlblinproc.setGeometry(QRect(190, 580, 171, 16))
        self.statlblinproc.setFont(font1)
        self.statlblinproc.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_41 = QLabel(self.frame_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 10, 541, 20))
        self.label_41.setFont(font3)
        self.label_41.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.HOMETAP)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1190, 110, 571, 611))
        self.frame_6.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.statfinish = QTableWidget(self.frame_6)
        if (self.statfinish.columnCount() < 5):
            self.statfinish.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.statfinish.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.statfinish.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.statfinish.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.statfinish.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.statfinish.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.statfinish.setObjectName(u"statfinish")
        self.statfinish.setGeometry(QRect(10, 40, 551, 521))
        self.statfinish.setFont(font2)
        self.statfinish.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 580, 171, 16))
        self.label_11.setFont(font1)
        self.statlblfinish = QLabel(self.frame_6)
        self.statlblfinish.setObjectName(u"statlblfinish")
        self.statlblfinish.setGeometry(QRect(190, 580, 171, 16))
        self.statlblfinish.setFont(font1)
        self.statlblfinish.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_42 = QLabel(self.frame_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 10, 541, 20))
        self.label_42.setFont(font3)
        self.label_42.setAlignment(Qt.AlignCenter)
        self.frame_14 = QFrame(self.HOMETAP)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, 10, 1751, 81))
        self.frame_14.setStyleSheet(u"background-color: rgb(40, 45, 50);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_48 = QLabel(self.frame_14)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 10, 1731, 20))
        self.label_48.setFont(font3)
        self.label_48.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_14)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 40, 171, 28))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton:hover#pushButton\n"
"{\n"
"	background-color: rgb(45, 50, 55);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"")
        self.exitbutton = QPushButton(self.frame_14)
        self.exitbutton.setObjectName(u"exitbutton")
        self.exitbutton.setGeometry(QRect(880, 40, 171, 28))
        self.exitbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitbutton.setStyleSheet(u"\n"
"QPushButton:hover#exitbutton\n"
"{\n"
"	background-color: rgb(45, 50, 55);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"")
        self.drpc = QLabel(self.frame_14)
        self.drpc.setObjectName(u"drpc")
        self.drpc.setGeometry(QRect(230, 30, 171, 16))
        self.drpc.setFont(font1)
        self.drpc.setStyleSheet(u"color: rgb(255, 140, 0);")
        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 191, 16))
        self.label_3.setFont(font1)
        self.tmpc = QLabel(self.frame_14)
        self.tmpc.setObjectName(u"tmpc")
        self.tmpc.setGeometry(QRect(230, 50, 171, 16))
        self.tmpc.setFont(font1)
        self.tmpc.setStyleSheet(u"color: rgb(255, 140, 0);")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 50, 191, 16))
        self.label_4.setFont(font1)
        self.frame_15 = QFrame(self.HOMETAP)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 740, 1751, 81))
        self.frame_15.setStyleSheet(u"background-color: rgb(40, 45, 50);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_50 = QLabel(self.frame_15)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 10, 1731, 20))
        self.label_50.setFont(font3)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.drpc_2 = QLabel(self.frame_15)
        self.drpc_2.setObjectName(u"drpc_2")
        self.drpc_2.setGeometry(QRect(130, 30, 211, 20))
        self.drpc_2.setFont(font1)
        self.drpc_2.setStyleSheet(u"color: rgb(255, 140, 0);")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 91, 16))
        self.label_6.setFont(font1)
        self.tmpc_2 = QLabel(self.frame_15)
        self.tmpc_2.setObjectName(u"tmpc_2")
        self.tmpc_2.setGeometry(QRect(130, 50, 171, 16))
        self.tmpc_2.setFont(font1)
        self.tmpc_2.setStyleSheet(u"color: rgb(255, 140, 0);")
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 50, 91, 16))
        self.label_7.setFont(font1)
        self.tabWidget.addTab(self.HOMETAP, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_7 = QFrame(self.tab_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 571, 711))
        self.frame_7.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 541, 20))
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 680, 171, 16))
        self.label_14.setFont(font1)
        self.cardiocount = QLabel(self.frame_7)
        self.cardiocount.setObjectName(u"cardiocount")
        self.cardiocount.setGeometry(QRect(190, 680, 171, 16))
        self.cardiocount.setFont(font1)
        self.cardiocount.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 50, 141, 16))
        self.label_16.setFont(font1)
        self.cardioname = QLabel(self.frame_7)
        self.cardioname.setObjectName(u"cardioname")
        self.cardioname.setGeometry(QRect(160, 50, 141, 16))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.cardioname.setFont(font4)
        self.cardioname.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.cardiotime = QLabel(self.frame_7)
        self.cardiotime.setObjectName(u"cardiotime")
        self.cardiotime.setGeometry(QRect(450, 50, 81, 16))
        self.cardiotime.setFont(font4)
        self.cardiotime.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(310, 50, 131, 16))
        self.label_19.setFont(font1)
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 380, 141, 16))
        self.label_20.setFont(font1)
        self.cardiowaiting = QTableWidget(self.frame_7)
        if (self.cardiowaiting.columnCount() < 4):
            self.cardiowaiting.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.cardiowaiting.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.cardiowaiting.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.cardiowaiting.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.cardiowaiting.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.cardiowaiting.setObjectName(u"cardiowaiting")
        self.cardiowaiting.setGeometry(QRect(10, 110, 551, 251))
        self.cardiowaiting.setFont(font2)
        self.cardiowaiting.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 90, 141, 16))
        self.label_21.setFont(font1)
        self.cardiofinish = QTableWidget(self.frame_7)
        if (self.cardiofinish.columnCount() < 4):
            self.cardiofinish.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.cardiofinish.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.cardiofinish.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.cardiofinish.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.cardiofinish.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.cardiofinish.setObjectName(u"cardiofinish")
        self.cardiofinish.setGeometry(QRect(10, 400, 551, 261))
        self.cardiofinish.setFont(font2)
        self.cardiofinish.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(600, 10, 571, 711))
        self.frame_8.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 541, 20))
        self.label_22.setFont(font3)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 680, 171, 16))
        self.label_23.setFont(font1)
        self.orthocount = QLabel(self.frame_8)
        self.orthocount.setObjectName(u"orthocount")
        self.orthocount.setGeometry(QRect(190, 680, 171, 16))
        self.orthocount.setFont(font1)
        self.orthocount.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 50, 141, 16))
        self.label_25.setFont(font1)
        self.orthoname = QLabel(self.frame_8)
        self.orthoname.setObjectName(u"orthoname")
        self.orthoname.setGeometry(QRect(160, 50, 141, 16))
        self.orthoname.setFont(font4)
        self.orthoname.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.orthotime = QLabel(self.frame_8)
        self.orthotime.setObjectName(u"orthotime")
        self.orthotime.setGeometry(QRect(450, 50, 81, 16))
        self.orthotime.setFont(font4)
        self.orthotime.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(310, 50, 131, 16))
        self.label_28.setFont(font1)
        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 380, 141, 16))
        self.label_29.setFont(font1)
        self.orthowaiting = QTableWidget(self.frame_8)
        if (self.orthowaiting.columnCount() < 4):
            self.orthowaiting.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.orthowaiting.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.orthowaiting.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.orthowaiting.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.orthowaiting.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.orthowaiting.setObjectName(u"orthowaiting")
        self.orthowaiting.setGeometry(QRect(10, 110, 551, 251))
        self.orthowaiting.setFont(font2)
        self.orthowaiting.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 90, 141, 16))
        self.label_30.setFont(font1)
        self.orthofinish = QTableWidget(self.frame_8)
        if (self.orthofinish.columnCount() < 4):
            self.orthofinish.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.orthofinish.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.orthofinish.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.orthofinish.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.orthofinish.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.orthofinish.setObjectName(u"orthofinish")
        self.orthofinish.setGeometry(QRect(10, 400, 551, 261))
        self.orthofinish.setFont(font2)
        self.orthofinish.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.frame_9 = QFrame(self.tab_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(1190, 10, 571, 711))
        self.frame_9.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 541, 20))
        self.label_31.setFont(font3)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 680, 171, 16))
        self.label_32.setFont(font1)
        self.dermacount = QLabel(self.frame_9)
        self.dermacount.setObjectName(u"dermacount")
        self.dermacount.setGeometry(QRect(190, 680, 171, 16))
        self.dermacount.setFont(font1)
        self.dermacount.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 50, 141, 16))
        self.label_34.setFont(font1)
        self.dermaname = QLabel(self.frame_9)
        self.dermaname.setObjectName(u"dermaname")
        self.dermaname.setGeometry(QRect(160, 50, 141, 16))
        self.dermaname.setFont(font4)
        self.dermaname.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.dermatime = QLabel(self.frame_9)
        self.dermatime.setObjectName(u"dermatime")
        self.dermatime.setGeometry(QRect(450, 50, 81, 16))
        self.dermatime.setFont(font4)
        self.dermatime.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_37 = QLabel(self.frame_9)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(310, 50, 131, 16))
        self.label_37.setFont(font1)
        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 380, 141, 16))
        self.label_38.setFont(font1)
        self.dermawaiting = QTableWidget(self.frame_9)
        if (self.dermawaiting.columnCount() < 4):
            self.dermawaiting.setColumnCount(4)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.dermawaiting.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.dermawaiting.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.dermawaiting.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.dermawaiting.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        self.dermawaiting.setObjectName(u"dermawaiting")
        self.dermawaiting.setGeometry(QRect(10, 110, 551, 251))
        self.dermawaiting.setFont(font2)
        self.dermawaiting.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 90, 141, 16))
        self.label_39.setFont(font1)
        self.dermafinished = QTableWidget(self.frame_9)
        if (self.dermafinished.columnCount() < 4):
            self.dermafinished.setColumnCount(4)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.dermafinished.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.dermafinished.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.dermafinished.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.dermafinished.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        self.dermafinished.setObjectName(u"dermafinished")
        self.dermafinished.setGeometry(QRect(10, 400, 551, 261))
        self.dermafinished.setFont(font2)
        self.dermafinished.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 410, 551, 311))
        self.frame_10.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 10, 521, 20))
        self.label_43.setFont(font3)
        self.label_43.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.frame_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 50, 141, 16))
        self.label_46.setFont(font1)
        self.gm1name = QLabel(self.frame_10)
        self.gm1name.setObjectName(u"gm1name")
        self.gm1name.setGeometry(QRect(160, 50, 141, 16))
        self.gm1name.setFont(font4)
        self.gm1name.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.gm1time = QLabel(self.frame_10)
        self.gm1time.setObjectName(u"gm1time")
        self.gm1time.setGeometry(QRect(450, 50, 81, 16))
        self.gm1time.setFont(font4)
        self.gm1time.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_49 = QLabel(self.frame_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(310, 50, 131, 16))
        self.label_49.setFont(font1)
        self.gm1using = QTableWidget(self.frame_10)
        if (self.gm1using.columnCount() < 3):
            self.gm1using.setColumnCount(3)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.gm1using.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.gm1using.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.gm1using.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        if (self.gm1using.rowCount() < 1):
            self.gm1using.setRowCount(1)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.gm1using.setVerticalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.gm1using.setItem(0, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.gm1using.setItem(0, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.gm1using.setItem(0, 2, __qtablewidgetitem45)
        self.gm1using.setObjectName(u"gm1using")
        self.gm1using.setGeometry(QRect(10, 110, 531, 81))
        self.gm1using.setFont(font2)
        self.gm1using.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.gm1stat = QLabel(self.frame_10)
        self.gm1stat.setObjectName(u"gm1stat")
        self.gm1stat.setGeometry(QRect(160, 80, 141, 16))
        self.gm1stat.setFont(font4)
        self.label_52 = QLabel(self.frame_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 80, 141, 16))
        self.label_52.setFont(font1)
        self.gm1max = QTableWidget(self.frame_10)
        if (self.gm1max.columnCount() < 3):
            self.gm1max.setColumnCount(3)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.gm1max.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.gm1max.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.gm1max.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        if (self.gm1max.rowCount() < 1):
            self.gm1max.setRowCount(1)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.gm1max.setVerticalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.gm1max.setItem(0, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.gm1max.setItem(0, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.gm1max.setItem(0, 2, __qtablewidgetitem52)
        self.gm1max.setObjectName(u"gm1max")
        self.gm1max.setGeometry(QRect(10, 210, 531, 81))
        self.gm1max.setFont(font2)
        self.gm1max.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.frame_11 = QFrame(self.tab)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(610, 410, 551, 311))
        self.frame_11.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.frame_11)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(10, 10, 521, 20))
        self.label_61.setFont(font3)
        self.label_61.setAlignment(Qt.AlignCenter)
        self.label_64 = QLabel(self.frame_11)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(10, 50, 141, 16))
        self.label_64.setFont(font1)
        self.gm2name = QLabel(self.frame_11)
        self.gm2name.setObjectName(u"gm2name")
        self.gm2name.setGeometry(QRect(160, 50, 141, 16))
        self.gm2name.setFont(font4)
        self.gm2name.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.gm2time = QLabel(self.frame_11)
        self.gm2time.setObjectName(u"gm2time")
        self.gm2time.setGeometry(QRect(450, 50, 81, 16))
        self.gm2time.setFont(font4)
        self.gm2time.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_67 = QLabel(self.frame_11)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(310, 50, 131, 16))
        self.label_67.setFont(font1)
        self.gm2using = QTableWidget(self.frame_11)
        if (self.gm2using.columnCount() < 3):
            self.gm2using.setColumnCount(3)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.gm2using.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.gm2using.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.gm2using.setHorizontalHeaderItem(2, __qtablewidgetitem55)
        if (self.gm2using.rowCount() < 1):
            self.gm2using.setRowCount(1)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.gm2using.setVerticalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.gm2using.setItem(0, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.gm2using.setItem(0, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.gm2using.setItem(0, 2, __qtablewidgetitem59)
        self.gm2using.setObjectName(u"gm2using")
        self.gm2using.setGeometry(QRect(10, 110, 531, 81))
        self.gm2using.setFont(font2)
        self.gm2using.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.gm2stat = QLabel(self.frame_11)
        self.gm2stat.setObjectName(u"gm2stat")
        self.gm2stat.setGeometry(QRect(160, 80, 141, 16))
        self.gm2stat.setFont(font4)
        self.label_69 = QLabel(self.frame_11)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 80, 141, 16))
        self.label_69.setFont(font1)
        self.gm2max = QTableWidget(self.frame_11)
        if (self.gm2max.columnCount() < 3):
            self.gm2max.setColumnCount(3)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.gm2max.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.gm2max.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.gm2max.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        if (self.gm2max.rowCount() < 1):
            self.gm2max.setRowCount(1)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.gm2max.setVerticalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.gm2max.setItem(0, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.gm2max.setItem(0, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.gm2max.setItem(0, 2, __qtablewidgetitem66)
        self.gm2max.setObjectName(u"gm2max")
        self.gm2max.setGeometry(QRect(10, 210, 531, 81))
        self.gm2max.setFont(font2)
        self.gm2max.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.frame_12 = QFrame(self.tab)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(1210, 410, 551, 311))
        self.frame_12.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"background-color: rgb(40, 45, 50);\n"
"	border-color: rgb(255, 44, 121);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_70 = QLabel(self.frame_12)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 10, 521, 20))
        self.label_70.setFont(font3)
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_73 = QLabel(self.frame_12)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(10, 50, 141, 16))
        self.label_73.setFont(font1)
        self.gm3name = QLabel(self.frame_12)
        self.gm3name.setObjectName(u"gm3name")
        self.gm3name.setGeometry(QRect(160, 50, 141, 16))
        self.gm3name.setFont(font4)
        self.gm3name.setStyleSheet(u"color: rgb(255, 44, 121);")
        self.gm3time = QLabel(self.frame_12)
        self.gm3time.setObjectName(u"gm3time")
        self.gm3time.setGeometry(QRect(450, 50, 81, 16))
        self.gm3time.setFont(font4)
        self.gm3time.setStyleSheet(u"color: rgb(28, 167, 236);")
        self.label_76 = QLabel(self.frame_12)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(310, 50, 131, 16))
        self.label_76.setFont(font1)
        self.gm3using = QTableWidget(self.frame_12)
        if (self.gm3using.columnCount() < 3):
            self.gm3using.setColumnCount(3)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.gm3using.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.gm3using.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.gm3using.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        if (self.gm3using.rowCount() < 1):
            self.gm3using.setRowCount(1)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.gm3using.setVerticalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.gm3using.setItem(0, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.gm3using.setItem(0, 1, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.gm3using.setItem(0, 2, __qtablewidgetitem73)
        self.gm3using.setObjectName(u"gm3using")
        self.gm3using.setGeometry(QRect(10, 110, 531, 81))
        self.gm3using.setFont(font2)
        self.gm3using.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.gm3stat = QLabel(self.frame_12)
        self.gm3stat.setObjectName(u"gm3stat")
        self.gm3stat.setGeometry(QRect(160, 80, 141, 16))
        self.gm3stat.setFont(font4)
        self.label_78 = QLabel(self.frame_12)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(10, 80, 141, 16))
        self.label_78.setFont(font1)
        self.gm3max = QTableWidget(self.frame_12)
        if (self.gm3max.columnCount() < 3):
            self.gm3max.setColumnCount(3)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.gm3max.setHorizontalHeaderItem(0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.gm3max.setHorizontalHeaderItem(1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.gm3max.setHorizontalHeaderItem(2, __qtablewidgetitem76)
        if (self.gm3max.rowCount() < 1):
            self.gm3max.setRowCount(1)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.gm3max.setVerticalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.gm3max.setItem(0, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.gm3max.setItem(0, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.gm3max.setItem(0, 2, __qtablewidgetitem80)
        self.gm3max.setObjectName(u"gm3max")
        self.gm3max.setGeometry(QRect(10, 210, 531, 81))
        self.gm3max.setFont(font2)
        self.gm3max.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.frame_13 = QFrame(self.tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 1751, 381))
        self.frame_13.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(40, 45, 50);\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border-color:  rgb(28, 167, 236);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.bankeralgo = QTableWidget(self.frame_13)
        if (self.bankeralgo.columnCount() < 4):
            self.bankeralgo.setColumnCount(4)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.bankeralgo.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.bankeralgo.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.bankeralgo.setHorizontalHeaderItem(2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.bankeralgo.setHorizontalHeaderItem(3, __qtablewidgetitem84)
        if (self.bankeralgo.rowCount() < 3):
            self.bankeralgo.setRowCount(3)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.bankeralgo.setVerticalHeaderItem(0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.bankeralgo.setVerticalHeaderItem(1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.bankeralgo.setVerticalHeaderItem(2, __qtablewidgetitem87)
        self.bankeralgo.setObjectName(u"bankeralgo")
        self.bankeralgo.setGeometry(QRect(10, 70, 591, 161))
        self.bankeralgo.setFont(font2)
        self.bankeralgo.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_44 = QLabel(self.frame_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 40, 581, 20))
        self.label_44.setFont(font3)
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 10, 1731, 20))
        self.label_45.setFont(font3)
        self.label_45.setAlignment(Qt.AlignCenter)
        self.treatwaiting = QTableWidget(self.frame_13)
        if (self.treatwaiting.columnCount() < 4):
            self.treatwaiting.setColumnCount(4)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.treatwaiting.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.treatwaiting.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.treatwaiting.setHorizontalHeaderItem(2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.treatwaiting.setHorizontalHeaderItem(3, __qtablewidgetitem91)
        self.treatwaiting.setObjectName(u"treatwaiting")
        self.treatwaiting.setGeometry(QRect(610, 70, 561, 281))
        self.treatwaiting.setFont(font2)
        self.treatwaiting.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.treatfinish = QTableWidget(self.frame_13)
        if (self.treatfinish.columnCount() < 4):
            self.treatfinish.setColumnCount(4)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.treatfinish.setHorizontalHeaderItem(0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.treatfinish.setHorizontalHeaderItem(1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.treatfinish.setHorizontalHeaderItem(2, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.treatfinish.setHorizontalHeaderItem(3, __qtablewidgetitem95)
        self.treatfinish.setObjectName(u"treatfinish")
        self.treatfinish.setGeometry(QRect(1180, 70, 561, 281))
        self.treatfinish.setFont(font2)
        self.treatfinish.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_62 = QLabel(self.frame_13)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(610, 40, 551, 20))
        self.label_62.setFont(font3)
        self.label_62.setAlignment(Qt.AlignCenter)
        self.label_63 = QLabel(self.frame_13)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(1180, 40, 551, 20))
        self.label_63.setFont(font3)
        self.label_63.setAlignment(Qt.AlignCenter)
        self.bankeravbl = QTableWidget(self.frame_13)
        if (self.bankeravbl.columnCount() < 3):
            self.bankeravbl.setColumnCount(3)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.bankeravbl.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.bankeravbl.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.bankeravbl.setHorizontalHeaderItem(2, __qtablewidgetitem98)
        if (self.bankeravbl.rowCount() < 1):
            self.bankeravbl.setRowCount(1)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.bankeravbl.setVerticalHeaderItem(0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.bankeravbl.setItem(0, 0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.bankeravbl.setItem(0, 1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.bankeravbl.setItem(0, 2, __qtablewidgetitem102)
        self.bankeravbl.setObjectName(u"bankeravbl")
        self.bankeravbl.setGeometry(QRect(10, 270, 591, 81))
        self.bankeravbl.setFont(font2)
        self.bankeravbl.setStyleSheet(u"background-color: rgb(45, 50, 55);")
        self.label_71 = QLabel(self.frame_13)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(10, 240, 531, 20))
        self.label_71.setFont(font3)
        self.label_71.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(580, 410, 16, 311))
        self.line.setStyleSheet(u"background-color: rgb(40, 45, 50);\n"
"color: rgb(40, 45, 50);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1180, 410, 16, 311))
        self.line_2.setStyleSheet(u"background-color: rgb(40, 45, 50);\n"
"color: rgb(40, 45, 50);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MOH - Hospital Operating", None))
        ___qtablewidgetitem = self.statwaiting.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.statwaiting.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem2 = self.statwaiting.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem3 = self.statwaiting.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem4 = self.statwaiting.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.statlblwaiting.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Waiting", None))
        ___qtablewidgetitem5 = self.statinproc.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.statinproc.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem7 = self.statinproc.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem8 = self.statinproc.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem9 = self.statinproc.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.statlblinproc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"In process", None))
        ___qtablewidgetitem10 = self.statfinish.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.statfinish.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem12 = self.statfinish.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem13 = self.statfinish.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem14 = self.statfinish.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TYPE", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.statlblfinish.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Finished", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Treatment Dashbord", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.exitbutton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.drpc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doctor review patients :", None))
        self.tmpc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Treatment patients :", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Definitions", None))
        self.drpc_2.setText(QCoreApplication.translate("MainWindow", u"Degree of importance", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DOI :", None))
        self.tmpc_2.setText(QCoreApplication.translate("MainWindow", u"Thread ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID : ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HOMETAP), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cardiology", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.cardiocount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.cardioname.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.cardiotime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Finished : ", None))
        ___qtablewidgetitem15 = self.cardiowaiting.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.cardiowaiting.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem17 = self.cardiowaiting.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem18 = self.cardiowaiting.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Waiting : ", None))
        ___qtablewidgetitem19 = self.cardiofinish.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem20 = self.cardiofinish.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem21 = self.cardiofinish.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem22 = self.cardiofinish.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Orthopedics", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.orthocount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.orthoname.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.orthotime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Finished : ", None))
        ___qtablewidgetitem23 = self.orthowaiting.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem24 = self.orthowaiting.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem25 = self.orthowaiting.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem26 = self.orthowaiting.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Waiting : ", None))
        ___qtablewidgetitem27 = self.orthofinish.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.orthofinish.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem29 = self.orthofinish.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem30 = self.orthofinish.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Dermatology", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Number of patients : ", None))
        self.dermacount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.dermaname.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.dermatime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Finished : ", None))
        ___qtablewidgetitem31 = self.dermawaiting.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem32 = self.dermawaiting.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem33 = self.dermawaiting.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem34 = self.dermawaiting.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Waiting : ", None))
        ___qtablewidgetitem35 = self.dermafinished.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem36 = self.dermafinished.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem37 = self.dermafinished.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem38 = self.dermafinished.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Doctor Review [P]", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"General Medicine #1", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.gm1name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.gm1time.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        ___qtablewidgetitem39 = self.gm1using.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem40 = self.gm1using.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem41 = self.gm1using.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem42 = self.gm1using.verticalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Using resources : ", None));

        __sortingEnabled = self.gm1using.isSortingEnabled()
        self.gm1using.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.gm1using.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem44 = self.gm1using.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem45 = self.gm1using.item(0, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm1using.setSortingEnabled(__sortingEnabled)

        self.gm1stat.setText(QCoreApplication.translate("MainWindow", u"idle", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Status : ", None))
        ___qtablewidgetitem46 = self.gm1max.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem47 = self.gm1max.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem48 = self.gm1max.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem49 = self.gm1max.verticalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Max :", None));

        __sortingEnabled1 = self.gm1max.isSortingEnabled()
        self.gm1max.setSortingEnabled(False)
        ___qtablewidgetitem50 = self.gm1max.item(0, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem51 = self.gm1max.item(0, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem52 = self.gm1max.item(0, 2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm1max.setSortingEnabled(__sortingEnabled1)

        self.label_61.setText(QCoreApplication.translate("MainWindow", u"General Medicine #2", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.gm2name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.gm2time.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        ___qtablewidgetitem53 = self.gm2using.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem54 = self.gm2using.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem55 = self.gm2using.horizontalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem56 = self.gm2using.verticalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Using resources : ", None));

        __sortingEnabled2 = self.gm2using.isSortingEnabled()
        self.gm2using.setSortingEnabled(False)
        ___qtablewidgetitem57 = self.gm2using.item(0, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem58 = self.gm2using.item(0, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem59 = self.gm2using.item(0, 2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm2using.setSortingEnabled(__sortingEnabled2)

        self.gm2stat.setText(QCoreApplication.translate("MainWindow", u"idle", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Status : ", None))
        ___qtablewidgetitem60 = self.gm2max.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem61 = self.gm2max.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem62 = self.gm2max.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem63 = self.gm2max.verticalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Max :", None));

        __sortingEnabled3 = self.gm2max.isSortingEnabled()
        self.gm2max.setSortingEnabled(False)
        ___qtablewidgetitem64 = self.gm2max.item(0, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem65 = self.gm2max.item(0, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem66 = self.gm2max.item(0, 2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm2max.setSortingEnabled(__sortingEnabled3)

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"General Medicine #3", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Current Serving : ", None))
        self.gm3name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.gm3time.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Remaining time: ", None))
        ___qtablewidgetitem67 = self.gm3using.horizontalHeaderItem(0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem68 = self.gm3using.horizontalHeaderItem(1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem69 = self.gm3using.horizontalHeaderItem(2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem70 = self.gm3using.verticalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Using resources : ", None));

        __sortingEnabled4 = self.gm3using.isSortingEnabled()
        self.gm3using.setSortingEnabled(False)
        ___qtablewidgetitem71 = self.gm3using.item(0, 0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem72 = self.gm3using.item(0, 1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem73 = self.gm3using.item(0, 2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm3using.setSortingEnabled(__sortingEnabled4)

        self.gm3stat.setText(QCoreApplication.translate("MainWindow", u"idle", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Status : ", None))
        ___qtablewidgetitem74 = self.gm3max.horizontalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem75 = self.gm3max.horizontalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem76 = self.gm3max.horizontalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem77 = self.gm3max.verticalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Max :", None));

        __sortingEnabled5 = self.gm3max.isSortingEnabled()
        self.gm3max.setSortingEnabled(False)
        ___qtablewidgetitem78 = self.gm3max.item(0, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem79 = self.gm3max.item(0, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem80 = self.gm3max.item(0, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.gm3max.setSortingEnabled(__sortingEnabled5)

        ___qtablewidgetitem81 = self.bankeralgo.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem82 = self.bankeralgo.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem83 = self.bankeralgo.horizontalHeaderItem(2)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Resources", None));
        ___qtablewidgetitem84 = self.bankeralgo.horizontalHeaderItem(3)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem85 = self.bankeralgo.verticalHeaderItem(0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Room 1", None));
        ___qtablewidgetitem86 = self.bankeralgo.verticalHeaderItem(1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Room 2", None));
        ___qtablewidgetitem87 = self.bankeralgo.verticalHeaderItem(2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Room 3", None));
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Banker Algorithm", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Treatment Dashbord", None))
        ___qtablewidgetitem88 = self.treatwaiting.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem89 = self.treatwaiting.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem90 = self.treatwaiting.horizontalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem91 = self.treatwaiting.horizontalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem92 = self.treatfinish.horizontalHeaderItem(0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem93 = self.treatfinish.horizontalHeaderItem(1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem94 = self.treatfinish.horizontalHeaderItem(2)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"DOI", None));
        ___qtablewidgetitem95 = self.treatfinish.horizontalHeaderItem(3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Waiting", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Finished", None))
        ___qtablewidgetitem96 = self.bankeravbl.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Medical nutrition", None));
        ___qtablewidgetitem97 = self.bankeravbl.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Steam device", None));
        ___qtablewidgetitem98 = self.bankeravbl.horizontalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Injections", None));
        ___qtablewidgetitem99 = self.bankeravbl.verticalHeaderItem(0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Using resources : ", None));

        __sortingEnabled6 = self.bankeravbl.isSortingEnabled()
        self.bankeravbl.setSortingEnabled(False)
        ___qtablewidgetitem100 = self.bankeravbl.item(0, 0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem101 = self.bankeravbl.item(0, 1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem102 = self.bankeravbl.item(0, 2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.bankeravbl.setSortingEnabled(__sortingEnabled6)

        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Available Resources", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Treatment [P]", None))
    # retranslateUi

