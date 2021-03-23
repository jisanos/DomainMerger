from ui.main_window import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_packs()

    def load_packs(self):
        """Here we load the diferent blacklist packs into the tree view widget
        so that the user can check the ones he wants.
        """
        # Dictionary containing the differen blacklists, within are touples of pack names mixed
        # with their respective URL.
        blacklists = {"Energized Protection": [("Spark", "https://block.energized.pro/spark/formats/domains.txt", "True Lite Protection Pack."),
                                               ("Blu", "https://block.energized.pro/blu/formats/domains.txt",
                                                "A Mid Ranger Flagship Protection Pack."),
                                               ("Blu GO", "https://block.energized.pro/bluGo/formats/domains.txt",
                                                "A Lightweight Mid Ranger Protection Pack."),
                                               ("Basic", "https://block.energized.pro/basic/formats/domains.txt",
                                                "An All-Rounder Balanced Protection Pack."),
                                               ("Porn", "https://block.energized.pro/porn/formats/domains.txt",
                                                "Blocks Access to most of the Pornware."),
                                               ("Ultimate", "https://block.energized.pro/ultimate/formats/domains.txt",
                                                "Flagship Protection Pack from Energized Protection."),
                                               ("Unified", "https://block.energized.pro/unified/formats/domains.txt",
                                                "Flagship Full Protection Pack from Energized Protection."),
                                               ("Xtreme", "https://block.energized.pro/extensions/xtreme/formats/domains.txt",
                                                "(extension) An Extreme Solution for Ultimate Protection."),
                                               ("Regional", "https://block.energized.pro/extensions/regional/formats/domains.txt",
                                                "(extension) An Extension to Block Regional Annoyances."),
                                               ("Social", "https://block.energized.pro/extensions/social/formats/domains.txt",
                                                "(extension) Social Sites and Apps Blocking."),
                                               ("Porn Lite", "https://block.energized.pro/extensions/porn-lite/formats/domains.txt",
                                               "(extension) Lite Extension Porn Pack.")],

                      "Steven Black Hosts": [("Unified Hosts", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
                                              "This hosts file is a merged collection of hosts from reputable sources, with a dash of crowd sourcing via GitHub"),
                                             ("Fake News", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts", "(extension)"),
                                             ("Porn", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts", "(extension)"),
                                             ("Social", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social/hosts", "(extension)"),
                                             ("Gambling", "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts", "(extension)")],

                      "OISD": [("Basic", "https://dbl.oisd.nl/basic/", "primarily blocks Ads, (Mobile) App Ads."),
                               ("Full", "https://dbl.oisd.nl/",
                               "Ads, (Mobile) App Ads, Phishing, Malvertising, Malware, Spyware, Ransomware, CryptoJacking, Scam... Telemetry, Analytics, Tracking (Where not needed for proper functionality)")],
                      }

        for blacklist in blacklists:
            parent = QtWidgets.QTreeWidgetItem(self.ui.treeWidget_packs)
            parent.setText(0, blacklist)
            # parent.setFlags(parent.flags(
            # ) | QtCore.Qt.ItemFlags.ItemIsAutoTristate | QtCore.Qt.ItemFlags.ItemIsUserCheckable)

            for pack, url, description in blacklists[blacklist]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(
                    child.flags() | QtCore.Qt.ItemFlags.ItemIsUserCheckable)
                child.setText(0, pack)
                child.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
