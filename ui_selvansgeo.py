# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_selvansgeo.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelvansGeo(object):
    def setupUi(self, SelvansGeo):
        SelvansGeo.setObjectName("SelvansGeo")
        SelvansGeo.resize(540, 602)
        SelvansGeo.setAutoFillBackground(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SelvansGeo)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 581))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabPanel = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.tabPanel.setEnabled(True)
        self.tabPanel.setMinimumSize(QtCore.QSize(501, 0))
        self.tabPanel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabPanel.setObjectName("tabPanel")
        self.connexionTab = QtWidgets.QWidget()
        self.connexionTab.setObjectName("connexionTab")
        self.txtPassword = QtWidgets.QLineEdit(self.connexionTab)
        self.txtPassword.setGeometry(QtCore.QRect(170, 290, 171, 22))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.label_4 = QtWidgets.QLabel(self.connexionTab)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 91, 16))
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.connexionTab)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 121, 16))
        self.label_5.setObjectName("label_5")
        self.cmbConnection = QtWidgets.QComboBox(self.connexionTab)
        self.cmbConnection.setGeometry(QtCore.QRect(170, 250, 171, 22))
        self.cmbConnection.setObjectName("cmbConnection")
        self.cmbConnection.addItem("")
        self.cmbConnection.addItem("")
        self.btConnection = QtWidgets.QPushButton(self.connexionTab)
        self.btConnection.setGeometry(QtCore.QRect(170, 320, 171, 28))
        self.btConnection.setObjectName("btConnection")
        self.grpProjects = QtWidgets.QGroupBox(self.connexionTab)
        self.grpProjects.setGeometry(QtCore.QRect(10, 10, 471, 211))
        self.grpProjects.setObjectName("grpProjects")
        self.btLoadProject = QtWidgets.QPushButton(self.grpProjects)
        self.btLoadProject.setEnabled(True)
        self.btLoadProject.setGeometry(QtCore.QRect(230, 110, 221, 28))
        self.btLoadProject.setObjectName("btLoadProject")
        self.btDefineDefaultProject = QtWidgets.QPushButton(self.grpProjects)
        self.btDefineDefaultProject.setGeometry(QtCore.QRect(230, 140, 221, 28))
        self.btDefineDefaultProject.setObjectName("btDefineDefaultProject")
        self.btResetDefaultProject = QtWidgets.QPushButton(self.grpProjects)
        self.btResetDefaultProject.setGeometry(QtCore.QRect(230, 170, 221, 28))
        self.btResetDefaultProject.setObjectName("btResetDefaultProject")
        self.lblProject = QtWidgets.QLabel(self.grpProjects)
        self.lblProject.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.lblProject.setObjectName("lblProject")
        self.lblCurrentProject = QtWidgets.QTextBrowser(self.grpProjects)
        self.lblCurrentProject.setGeometry(QtCore.QRect(130, 30, 321, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lblCurrentProject.setPalette(palette)
        self.lblCurrentProject.setObjectName("lblCurrentProject")
        self.lblVersion = QtWidgets.QLabel(self.connexionTab)
        self.lblVersion.setGeometry(QtCore.QRect(10, 410, 471, 16))
        self.lblVersion.setObjectName("lblVersion")
        self.tabPanel.addTab(self.connexionTab, "")
        self.tabAnalysis = QtWidgets.QWidget()
        self.tabAnalysis.setObjectName("tabAnalysis")
        self.cmbAnalysis = QtWidgets.QComboBox(self.tabAnalysis)
        self.cmbAnalysis.setGeometry(QtCore.QRect(30, 60, 451, 22))
        self.cmbAnalysis.setObjectName("cmbAnalysis")
        self.lblAnalysis = QtWidgets.QLabel(self.tabAnalysis)
        self.lblAnalysis.setGeometry(QtCore.QRect(30, 36, 141, 20))
        self.lblAnalysis.setObjectName("lblAnalysis")
        self.btAnalysis = QtWidgets.QPushButton(self.tabAnalysis)
        self.btAnalysis.setGeometry(QtCore.QRect(310, 400, 171, 28))
        self.btAnalysis.setObjectName("btAnalysis")
        self.chkSaveAnalysisResult = QtWidgets.QCheckBox(self.tabAnalysis)
        self.chkSaveAnalysisResult.setGeometry(QtCore.QRect(40, 340, 431, 20))
        self.chkSaveAnalysisResult.setObjectName("chkSaveAnalysisResult")
        self.txtAnalysisName = QtWidgets.QLineEdit(self.tabAnalysis)
        self.txtAnalysisName.setGeometry(QtCore.QRect(40, 370, 441, 22))
        self.txtAnalysisName.setReadOnly(False)
        self.txtAnalysisName.setObjectName("txtAnalysisName")
        self.txtMssqlQuery = QtWidgets.QTextEdit(self.tabAnalysis)
        self.txtMssqlQuery.setEnabled(True)
        self.txtMssqlQuery.setGeometry(QtCore.QRect(30, 220, 451, 111))
        self.txtMssqlQuery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtMssqlQuery.setObjectName("txtMssqlQuery")
        self.btAdvancedUserMode = QtWidgets.QPushButton(self.tabAnalysis)
        self.btAdvancedUserMode.setGeometry(QtCore.QRect(340, 10, 141, 28))
        self.btAdvancedUserMode.setMinimumSize(QtCore.QSize(93, 28))
        self.btAdvancedUserMode.setCheckable(True)
        self.btAdvancedUserMode.setChecked(False)
        self.btAdvancedUserMode.setObjectName("btAdvancedUserMode")
        self.lblSql = QtWidgets.QLabel(self.tabAnalysis)
        self.lblSql.setGeometry(QtCore.QRect(30, 200, 191, 16))
        self.lblSql.setObjectName("lblSql")
        self.lblDateStart = QtWidgets.QLabel(self.tabAnalysis)
        self.lblDateStart.setEnabled(False)
        self.lblDateStart.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.lblDateStart.setObjectName("lblDateStart")
        self.lnYearStart = QtWidgets.QLineEdit(self.tabAnalysis)
        self.lnYearStart.setEnabled(False)
        self.lnYearStart.setGeometry(QtCore.QRect(80, 90, 51, 20))
        self.lnYearStart.setReadOnly(False)
        self.lnYearStart.setObjectName("lnYearStart")
        self.frameIcon = QtWidgets.QFrame(self.tabAnalysis)
        self.frameIcon.setGeometry(QtCore.QRect(10, 390, 41, 41))
        self.frameIcon.setStyleSheet("QFrame {bacCkground-color: red}")
        self.frameIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameIcon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameIcon.setLineWidth(0)
        self.frameIcon.setObjectName("frameIcon")
        self.chkLastSurvey = QtWidgets.QCheckBox(self.tabAnalysis)
        self.chkLastSurvey.setGeometry(QtCore.QRect(240, 90, 241, 20))
        self.chkLastSurvey.setChecked(True)
        self.chkLastSurvey.setObjectName("chkLastSurvey")
        self.label_6 = QtWidgets.QLabel(self.tabAnalysis)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.label_6.setObjectName("label_6")
        self.txtAdmShortName = QtWidgets.QLineEdit(self.tabAnalysis)
        self.txtAdmShortName.setGeometry(QtCore.QRect(190, 120, 221, 22))
        self.txtAdmShortName.setText("")
        self.txtAdmShortName.setObjectName("txtAdmShortName")
        self.lnYearEnd = QtWidgets.QLineEdit(self.tabAnalysis)
        self.lnYearEnd.setEnabled(True)
        self.lnYearEnd.setGeometry(QtCore.QRect(170, 90, 51, 20))
        self.lnYearEnd.setReadOnly(False)
        self.lnYearEnd.setObjectName("lnYearEnd")
        self.lblDateEnd = QtWidgets.QLabel(self.tabAnalysis)
        self.lblDateEnd.setEnabled(True)
        self.lblDateEnd.setGeometry(QtCore.QRect(140, 90, 41, 16))
        self.lblDateEnd.setObjectName("lblDateEnd")
        self.lblCoupeType = QtWidgets.QLabel(self.tabAnalysis)
        self.lblCoupeType.setEnabled(True)
        self.lblCoupeType.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.lblCoupeType.setObjectName("lblCoupeType")
        self.lnCoupeType = QtWidgets.QLineEdit(self.tabAnalysis)
        self.lnCoupeType.setEnabled(True)
        self.lnCoupeType.setGeometry(QtCore.QRect(190, 150, 221, 22))
        self.lnCoupeType.setReadOnly(False)
        self.lnCoupeType.setObjectName("lnCoupeType")
        self.tabPanel.addTab(self.tabAnalysis, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listArr = QtWidgets.QListWidget(self.tab_2)
        self.listArr.setGeometry(QtCore.QRect(20, 40, 141, 351))
        self.listArr.setObjectName("listArr")
        self.listAdm = QtWidgets.QListWidget(self.tab_2)
        self.listAdm.setGeometry(QtCore.QRect(180, 40, 141, 351))
        self.listAdm.setObjectName("listAdm")
        self.listDiv = QtWidgets.QListWidget(self.tab_2)
        self.listDiv.setGeometry(QtCore.QRect(340, 40, 141, 351))
        self.listDiv.setObjectName("listDiv")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 131, 16))
        self.label_3.setObjectName("label_3")
        self.tabPanel.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btQgisHelp = QtWidgets.QPushButton(self.tab)
        self.btQgisHelp.setGeometry(QtCore.QRect(10, 90, 211, 28))
        self.btQgisHelp.setObjectName("btQgisHelp")
        self.btSelvansGeoHelp = QtWidgets.QPushButton(self.tab)
        self.btSelvansGeoHelp.setGeometry(QtCore.QRect(10, 50, 211, 28))
        self.btSelvansGeoHelp.setObjectName("btSelvansGeoHelp")
        self.frameIcon_4 = QtWidgets.QFrame(self.tab)
        self.frameIcon_4.setGeometry(QtCore.QRect(0, 350, 41, 41))
        self.frameIcon_4.setStyleSheet("QFrame {bacCkground-color: red}")
        self.frameIcon_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameIcon_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameIcon_4.setLineWidth(0)
        self.frameIcon_4.setObjectName("frameIcon_4")
        self.btQgisPrintComposerHelp = QtWidgets.QPushButton(self.tab)
        self.btQgisPrintComposerHelp.setGeometry(QtCore.QRect(10, 130, 341, 28))
        self.btQgisPrintComposerHelp.setObjectName("btQgisPrintComposerHelp")
        self.tabPanel.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabPanel)

        self.retranslateUi(SelvansGeo)
        self.tabPanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SelvansGeo)

    def retranslateUi(self, SelvansGeo):
        _translate = QtCore.QCoreApplication.translate
        SelvansGeo.setWindowTitle(_translate("SelvansGeo", "SelvansGeo"))
        self.txtPassword.setWhatsThis(_translate("SelvansGeo", "Entrez votre mot de passe"))
        self.txtPassword.setText(_translate("SelvansGeo", "reader_sffn_2014"))
        self.label_4.setText(_translate("SelvansGeo", "Utilisateur: "))
        self.label_5.setText(_translate("SelvansGeo", "Mot de passe: "))
        self.cmbConnection.setToolTip(_translate("SelvansGeo", "Choisissez le type de connexion"))
        self.cmbConnection.setWhatsThis(_translate("SelvansGeo", "Pour modifier les données, choisir le mode édition"))
        self.cmbConnection.setItemText(0, _translate("SelvansGeo", "Consultation"))
        self.cmbConnection.setItemText(1, _translate("SelvansGeo", "Edition"))
        self.btConnection.setToolTip(_translate("SelvansGeo", "Se connecte à la base de données et charge (recharge) le projet"))
        self.btConnection.setWhatsThis(_translate("SelvansGeo", "Se connecter à la base de donnée et charger le projet"))
        self.btConnection.setText(_translate("SelvansGeo", "Connexion"))
        self.grpProjects.setTitle(_translate("SelvansGeo", "Projet QGIS SelvansGeo"))
        self.btLoadProject.setToolTip(_translate("SelvansGeo", "Recharge le projet affiché ci-dessus"))
        self.btLoadProject.setWhatsThis(_translate("SelvansGeo", "Permet de recharger le projet ouvert actuellement"))
        self.btLoadProject.setText(_translate("SelvansGeo", "(Re) Charger le projet"))
        self.btDefineDefaultProject.setToolTip(_translate("SelvansGeo", "Permet de charger par défaut un projet personnalisé"))
        self.btDefineDefaultProject.setWhatsThis(_translate("SelvansGeo", "Permet de choisir un projet QGIS personnalisé et de le définir comme projet par défaut"))
        self.btDefineDefaultProject.setText(_translate("SelvansGeo", "Définir un projet personnalisé"))
        self.btResetDefaultProject.setToolTip(_translate("SelvansGeo", "Utiliser le projet standard fournit avec SelvansGeo"))
        self.btResetDefaultProject.setWhatsThis(_translate("SelvansGeo", "Reprendre le project fournit avec le plugin et de le définir comme projet par défaut"))
        self.btResetDefaultProject.setText(_translate("SelvansGeo", "Reprendre le projet standard"))
        self.lblProject.setText(_translate("SelvansGeo", "Projet actuel:"))
        self.lblCurrentProject.setWhatsThis(_translate("SelvansGeo", "Ceci est le chemin vers le fichier QGIS chargé actuellement"))
        self.lblVersion.setText(_translate("SelvansGeo", "<html><head/><body><p><span style=\" font-weight:600;\">SelvansGeo 3.0.0</span> du 24.07.20017 pour QGIS <span style=\" font-weight:600;\">2.99 +</span></p></body></html>"))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.connexionTab), _translate("SelvansGeo", "Connexion - Projet"))
        self.cmbAnalysis.setToolTip(_translate("SelvansGeo", "Choix de l\'analyse thématique"))
        self.cmbAnalysis.setWhatsThis(_translate("SelvansGeo", "Choisir une analyse"))
        self.lblAnalysis.setText(_translate("SelvansGeo", "Choix de l\'analyse:"))
        self.btAnalysis.setWhatsThis(_translate("SelvansGeo", "Lancer l\'analyse"))
        self.btAnalysis.setText(_translate("SelvansGeo", "Lancer l\'analyse"))
        self.chkSaveAnalysisResult.setToolTip(_translate("SelvansGeo", "Permet de sauver le résultat de l\'analyse dans un répertoire (sans la représentation)"))
        self.chkSaveAnalysisResult.setWhatsThis(_translate("SelvansGeo", "Enregistrer le résultat de l\'analyse sur le disque au format ESRI shapefile"))
        self.chkSaveAnalysisResult.setText(_translate("SelvansGeo", "Sauvegarder le résultat sur le disque"))
        self.txtAnalysisName.setWhatsThis(_translate("SelvansGeo", "Chemin d\'enregistrement du fichier ESRI shapefile"))
        self.txtMssqlQuery.setToolTip(_translate("SelvansGeo", "Reqête SQL sur SELVANS"))
        self.btAdvancedUserMode.setToolTip(_translate("SelvansGeo", "Visualiser les détails de la requête SELVANS"))
        self.btAdvancedUserMode.setWhatsThis(_translate("SelvansGeo", "Permet d\'afficher la requête complète correspondant à l\'analyse en cours"))
        self.btAdvancedUserMode.setText(_translate("SelvansGeo", "Mode avancé"))
        self.lblSql.setText(_translate("SelvansGeo", "Requête SQL Server"))
        self.lblDateStart.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire"))
        self.lblDateStart.setText(_translate("SelvansGeo", "Année"))
        self.lnYearStart.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire"))
        self.lnYearStart.setWhatsThis(_translate("SelvansGeo", "Saisir la date du plus ancien inventaire auquel on s\'intéresse"))
        self.chkLastSurvey.setWhatsThis(_translate("SelvansGeo", "Ne considérer que l\'inventaire le plus récent"))
        self.chkLastSurvey.setText(_translate("SelvansGeo", "Prendre la date la plus récente"))
        self.label_6.setText(_translate("SelvansGeo", "Filtrer par administration:"))
        self.txtAdmShortName.setToolTip(_translate("SelvansGeo", "Entrez le ou les noms court. Ex: BDY ou BDY;BRD"))
        self.txtAdmShortName.setWhatsThis(_translate("SelvansGeo", "Saisir le ou les codes des administrations (Ex: BDY ou BDY, COT) "))
        self.lnYearEnd.setToolTip(_translate("SelvansGeo", "Date de fin de la période d\'analyse"))
        self.lnYearEnd.setWhatsThis(_translate("SelvansGeo", "Choisir la date de l\'inventaire le plus récent auquel on s\'intéresse"))
        self.lblDateEnd.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire"))
        self.lblDateEnd.setText(_translate("SelvansGeo", "Fin"))
        self.lblCoupeType.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire"))
        self.lblCoupeType.setText(_translate("SelvansGeo", "Motif de coupe:"))
        self.lnCoupeType.setToolTip(_translate("SelvansGeo", "Saisir le ou les types de coupes (ex: 13 ou 1;13)"))
        self.lnCoupeType.setWhatsThis(_translate("SelvansGeo", "Saisir le ou les types de coupes (ex: 13 ou 1;13)"))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tabAnalysis), _translate("SelvansGeo", "Analyses"))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tabAnalysis), _translate("SelvansGeo", "Analyses spatiale des données SELVANS actuelles"))
        self.listArr.setToolTip(_translate("SelvansGeo", "Click: sélection des administrations d\'un arrondissement"))
        self.listArr.setWhatsThis(_translate("SelvansGeo", "Sélectionner un arrondissement (simple click), zoomer: double click"))
        self.listAdm.setToolTip(_translate("SelvansGeo", "click: sélection des divisions d\'une administration, double-click: zoom sur l\'administration"))
        self.listAdm.setWhatsThis(_translate("SelvansGeo", "Sélectionner une administration (simple click), zoomer: double click"))
        self.listDiv.setToolTip(_translate("SelvansGeo", "double-click: zoom sur la division"))
        self.listDiv.setWhatsThis(_translate("SelvansGeo", "Sélectionner une division (simple click), zoomer: double click"))
        self.label.setText(_translate("SelvansGeo", "Arrondissements"))
        self.label_2.setText(_translate("SelvansGeo", "Administrations"))
        self.label_3.setText(_translate("SelvansGeo", "Divisions"))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tab_2), _translate("SelvansGeo", "Navigation"))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tab_2), _translate("SelvansGeo", "Navigation par niveaux géographiques"))
        self.btQgisHelp.setToolTip(_translate("SelvansGeo", "Afficher l\'aide en ligne QGIS"))
        self.btQgisHelp.setWhatsThis(_translate("SelvansGeo", "Afficher l\'aide en ligne QGIS"))
        self.btQgisHelp.setText(_translate("SelvansGeo", "Voir l\'aide QGIS"))
        self.btSelvansGeoHelp.setToolTip(_translate("SelvansGeo", "Afficher le manuel utilisateur SelvansGeo"))
        self.btSelvansGeoHelp.setWhatsThis(_translate("SelvansGeo", "Afficher le manuel utilisateur SelvansGeo"))
        self.btSelvansGeoHelp.setText(_translate("SelvansGeo", "Voir l\'aide SelvanGeo"))
        self.btQgisPrintComposerHelp.setToolTip(_translate("SelvansGeo", "Afficher l\'aide en ligne pour le composeur d\'impression"))
        self.btQgisPrintComposerHelp.setWhatsThis(_translate("SelvansGeo", "Afficher l\'aide en ligne pour le composeur d\'impression"))
        self.btQgisPrintComposerHelp.setText(_translate("SelvansGeo", "Voir l\'aide QGIS du composeur d\'impression"))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tab), _translate("SelvansGeo", "Aide"))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tab), _translate("SelvansGeo", "Toutes les aides dont vous avez besoin !"))

