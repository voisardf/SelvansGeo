# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projets\SelvansGeo\plugin\SelvansGeo\ui_selvansgeo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from PyQt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SelvansGeo(object):
    def setupUi(self, SelvansGeo):
        SelvansGeo.setObjectName(_fromUtf8("SelvansGeo"))
        SelvansGeo.resize(521, 486)
        SelvansGeo.setAutoFillBackground(False)
        self.tabPanel = QtGui.QTabWidget(SelvansGeo)
        self.tabPanel.setEnabled(True)
        self.tabPanel.setGeometry(QtCore.QRect(10, 10, 501, 471))
        self.tabPanel.setMinimumSize(QtCore.QSize(501, 0))
        self.tabPanel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabPanel.setObjectName(_fromUtf8("tabPanel"))
        self.connexionTab = QtGui.QWidget()
        self.connexionTab.setObjectName(_fromUtf8("connexionTab"))
        self.txtPassword = QtGui.QLineEdit(self.connexionTab)
        self.txtPassword.setGeometry(QtCore.QRect(170, 290, 171, 22))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.label_4 = QtGui.QLabel(self.connexionTab)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 91, 16))
        self.label_4.setToolTip(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.connexionTab)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cmbConnection = QtGui.QComboBox(self.connexionTab)
        self.cmbConnection.setGeometry(QtCore.QRect(170, 250, 171, 22))
        self.cmbConnection.setObjectName(_fromUtf8("cmbConnection"))
        self.cmbConnection.addItem(_fromUtf8(""))
        self.cmbConnection.addItem(_fromUtf8(""))
        self.btConnection = QtGui.QPushButton(self.connexionTab)
        self.btConnection.setGeometry(QtCore.QRect(170, 320, 171, 28))
        self.btConnection.setObjectName(_fromUtf8("btConnection"))
        self.grpProjects = QtGui.QGroupBox(self.connexionTab)
        self.grpProjects.setGeometry(QtCore.QRect(10, 10, 471, 211))
        self.grpProjects.setObjectName(_fromUtf8("grpProjects"))
        self.btLoadProject = QtGui.QPushButton(self.grpProjects)
        self.btLoadProject.setEnabled(True)
        self.btLoadProject.setGeometry(QtCore.QRect(230, 110, 221, 28))
        self.btLoadProject.setObjectName(_fromUtf8("btLoadProject"))
        self.btDefineDefaultProject = QtGui.QPushButton(self.grpProjects)
        self.btDefineDefaultProject.setGeometry(QtCore.QRect(230, 140, 221, 28))
        self.btDefineDefaultProject.setObjectName(_fromUtf8("btDefineDefaultProject"))
        self.btResetDefaultProject = QtGui.QPushButton(self.grpProjects)
        self.btResetDefaultProject.setGeometry(QtCore.QRect(230, 170, 221, 28))
        self.btResetDefaultProject.setObjectName(_fromUtf8("btResetDefaultProject"))
        self.lblProject = QtGui.QLabel(self.grpProjects)
        self.lblProject.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.lblProject.setObjectName(_fromUtf8("lblProject"))
        self.lblCurrentProject = QtGui.QTextBrowser(self.grpProjects)
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
        self.lblCurrentProject.setObjectName(_fromUtf8("lblCurrentProject"))
        self.lblVersion = QtGui.QLabel(self.connexionTab)
        self.lblVersion.setGeometry(QtCore.QRect(10, 410, 471, 16))
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.tabPanel.addTab(self.connexionTab, _fromUtf8(""))
        self.tabAnalysis = QtGui.QWidget()
        self.tabAnalysis.setObjectName(_fromUtf8("tabAnalysis"))
        self.cmbAnalysis = QtGui.QComboBox(self.tabAnalysis)
        self.cmbAnalysis.setGeometry(QtCore.QRect(30, 60, 451, 22))
        self.cmbAnalysis.setObjectName(_fromUtf8("cmbAnalysis"))
        self.lblAnalysis = QtGui.QLabel(self.tabAnalysis)
        self.lblAnalysis.setGeometry(QtCore.QRect(30, 36, 141, 20))
        self.lblAnalysis.setObjectName(_fromUtf8("lblAnalysis"))
        self.btAnalysis = QtGui.QPushButton(self.tabAnalysis)
        self.btAnalysis.setGeometry(QtCore.QRect(310, 400, 171, 28))
        self.btAnalysis.setObjectName(_fromUtf8("btAnalysis"))
        self.chkSaveAnalysisResult = QtGui.QCheckBox(self.tabAnalysis)
        self.chkSaveAnalysisResult.setGeometry(QtCore.QRect(40, 340, 431, 20))
        self.chkSaveAnalysisResult.setObjectName(_fromUtf8("chkSaveAnalysisResult"))
        self.txtAnalysisName = QtGui.QLineEdit(self.tabAnalysis)
        self.txtAnalysisName.setGeometry(QtCore.QRect(40, 370, 441, 22))
        self.txtAnalysisName.setReadOnly(False)
        self.txtAnalysisName.setObjectName(_fromUtf8("txtAnalysisName"))
        self.txtMssqlQuery = QtGui.QTextEdit(self.tabAnalysis)
        self.txtMssqlQuery.setEnabled(True)
        self.txtMssqlQuery.setGeometry(QtCore.QRect(30, 220, 451, 111))
        self.txtMssqlQuery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtMssqlQuery.setObjectName(_fromUtf8("txtMssqlQuery"))
        self.btAdvancedUserMode = QtGui.QPushButton(self.tabAnalysis)
        self.btAdvancedUserMode.setGeometry(QtCore.QRect(340, 10, 141, 28))
        self.btAdvancedUserMode.setMinimumSize(QtCore.QSize(93, 28))
        self.btAdvancedUserMode.setCheckable(True)
        self.btAdvancedUserMode.setChecked(False)
        self.btAdvancedUserMode.setObjectName(_fromUtf8("btAdvancedUserMode"))
        self.lblSql = QtGui.QLabel(self.tabAnalysis)
        self.lblSql.setGeometry(QtCore.QRect(30, 200, 191, 16))
        self.lblSql.setObjectName(_fromUtf8("lblSql"))
        self.lblDateStart = QtGui.QLabel(self.tabAnalysis)
        self.lblDateStart.setEnabled(False)
        self.lblDateStart.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.lblDateStart.setObjectName(_fromUtf8("lblDateStart"))
        self.lnYearStart = QtGui.QLineEdit(self.tabAnalysis)
        self.lnYearStart.setEnabled(False)
        self.lnYearStart.setGeometry(QtCore.QRect(80, 90, 51, 20))
        self.lnYearStart.setReadOnly(False)
        self.lnYearStart.setObjectName(_fromUtf8("lnYearStart"))
        self.frameIcon = QtGui.QFrame(self.tabAnalysis)
        self.frameIcon.setGeometry(QtCore.QRect(10, 390, 41, 41))
        self.frameIcon.setStyleSheet(_fromUtf8("QFrame {bacCkground-color: red}"))
        self.frameIcon.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameIcon.setFrameShadow(QtGui.QFrame.Plain)
        self.frameIcon.setLineWidth(0)
        self.frameIcon.setObjectName(_fromUtf8("frameIcon"))
        self.chkLastSurvey = QtGui.QCheckBox(self.tabAnalysis)
        self.chkLastSurvey.setGeometry(QtCore.QRect(240, 90, 241, 20))
        self.chkLastSurvey.setChecked(True)
        self.chkLastSurvey.setObjectName(_fromUtf8("chkLastSurvey"))
        self.label_6 = QtGui.QLabel(self.tabAnalysis)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtAdmShortName = QtGui.QLineEdit(self.tabAnalysis)
        self.txtAdmShortName.setGeometry(QtCore.QRect(190, 120, 221, 22))
        self.txtAdmShortName.setText(_fromUtf8(""))
        self.txtAdmShortName.setObjectName(_fromUtf8("txtAdmShortName"))
        self.lnYearEnd = QtGui.QLineEdit(self.tabAnalysis)
        self.lnYearEnd.setEnabled(True)
        self.lnYearEnd.setGeometry(QtCore.QRect(170, 90, 51, 20))
        self.lnYearEnd.setReadOnly(False)
        self.lnYearEnd.setObjectName(_fromUtf8("lnYearEnd"))
        self.lblDateEnd = QtGui.QLabel(self.tabAnalysis)
        self.lblDateEnd.setEnabled(True)
        self.lblDateEnd.setGeometry(QtCore.QRect(140, 90, 41, 16))
        self.lblDateEnd.setObjectName(_fromUtf8("lblDateEnd"))
        self.lblCoupeType = QtGui.QLabel(self.tabAnalysis)
        self.lblCoupeType.setEnabled(True)
        self.lblCoupeType.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.lblCoupeType.setObjectName(_fromUtf8("lblCoupeType"))
        self.lnCoupeType = QtGui.QLineEdit(self.tabAnalysis)
        self.lnCoupeType.setEnabled(True)
        self.lnCoupeType.setGeometry(QtCore.QRect(190, 150, 221, 22))
        self.lnCoupeType.setReadOnly(False)
        self.lnCoupeType.setObjectName(_fromUtf8("lnCoupeType"))
        self.tabPanel.addTab(self.tabAnalysis, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listArr = QtGui.QListWidget(self.tab_2)
        self.listArr.setGeometry(QtCore.QRect(20, 40, 141, 351))
        self.listArr.setObjectName(_fromUtf8("listArr"))
        self.listAdm = QtGui.QListWidget(self.tab_2)
        self.listAdm.setGeometry(QtCore.QRect(180, 40, 141, 351))
        self.listAdm.setObjectName(_fromUtf8("listAdm"))
        self.listDiv = QtGui.QListWidget(self.tab_2)
        self.listDiv.setGeometry(QtCore.QRect(340, 40, 141, 351))
        self.listDiv.setObjectName(_fromUtf8("listDiv"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(350, 10, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabPanel.addTab(self.tab_2, _fromUtf8(""))
        self.tabEdit = QtGui.QWidget()
        self.tabEdit.setObjectName(_fromUtf8("tabEdit"))
        self.frameIcon_3 = QtGui.QFrame(self.tabEdit)
        self.frameIcon_3.setGeometry(QtCore.QRect(10, 350, 41, 41))
        self.frameIcon_3.setStyleSheet(_fromUtf8("QFrame {bacCkground-color: red}"))
        self.frameIcon_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameIcon_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frameIcon_3.setLineWidth(0)
        self.frameIcon_3.setObjectName(_fromUtf8("frameIcon_3"))
        self.grpViewNodes = QtGui.QGroupBox(self.tabEdit)
        self.grpViewNodes.setGeometry(QtCore.QRect(10, 9, 481, 81))
        self.grpViewNodes.setObjectName(_fromUtf8("grpViewNodes"))
        self.chkSelectByCanvasExtent = QtGui.QCheckBox(self.grpViewNodes)
        self.chkSelectByCanvasExtent.setGeometry(QtCore.QRect(10, 20, 311, 20))
        self.chkSelectByCanvasExtent.setChecked(True)
        self.chkSelectByCanvasExtent.setObjectName(_fromUtf8("chkSelectByCanvasExtent"))
        self.comboLayers = QtGui.QComboBox(self.grpViewNodes)
        self.comboLayers.setGeometry(QtCore.QRect(10, 50, 271, 25))
        self.comboLayers.setObjectName(_fromUtf8("comboLayers"))
        self.btHideNodes = QtGui.QPushButton(self.grpViewNodes)
        self.btHideNodes.setGeometry(QtCore.QRect(390, 50, 81, 25))
        self.btHideNodes.setObjectName(_fromUtf8("btHideNodes"))
        self.btShowNodes = QtGui.QPushButton(self.grpViewNodes)
        self.btShowNodes.setGeometry(QtCore.QRect(290, 50, 91, 25))
        self.btShowNodes.setObjectName(_fromUtf8("btShowNodes"))
        self.groupBox = QtGui.QGroupBox(self.tabEdit)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 481, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btDesactivateLayer = QtGui.QPushButton(self.groupBox)
        self.btDesactivateLayer.setGeometry(QtCore.QRect(10, 30, 191, 28))
        self.btDesactivateLayer.setCheckable(True)
        self.btDesactivateLayer.setObjectName(_fromUtf8("btDesactivateLayer"))
        self.tabPanel.addTab(self.tabEdit, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.btQgisHelp = QtGui.QPushButton(self.tab)
        self.btQgisHelp.setGeometry(QtCore.QRect(10, 90, 211, 28))
        self.btQgisHelp.setObjectName(_fromUtf8("btQgisHelp"))
        self.btSelvansGeoHelp = QtGui.QPushButton(self.tab)
        self.btSelvansGeoHelp.setGeometry(QtCore.QRect(10, 50, 211, 28))
        self.btSelvansGeoHelp.setObjectName(_fromUtf8("btSelvansGeoHelp"))
        self.frameIcon_4 = QtGui.QFrame(self.tab)
        self.frameIcon_4.setGeometry(QtCore.QRect(0, 350, 41, 41))
        self.frameIcon_4.setStyleSheet(_fromUtf8("QFrame {bacCkground-color: red}"))
        self.frameIcon_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameIcon_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frameIcon_4.setLineWidth(0)
        self.frameIcon_4.setObjectName(_fromUtf8("frameIcon_4"))
        self.btQgisPrintComposerHelp = QtGui.QPushButton(self.tab)
        self.btQgisPrintComposerHelp.setGeometry(QtCore.QRect(10, 130, 341, 28))
        self.btQgisPrintComposerHelp.setObjectName(_fromUtf8("btQgisPrintComposerHelp"))
        self.tabPanel.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(SelvansGeo)
        self.tabPanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SelvansGeo)

    def retranslateUi(self, SelvansGeo):
        SelvansGeo.setWindowTitle(_translate("SelvansGeo", "SelvansGeo", None))
        self.txtPassword.setWhatsThis(_translate("SelvansGeo", "Entrez votre mot de passe", None))
        self.txtPassword.setText(_translate("SelvansGeo", "reader_sffn_2014", None))
        self.label_4.setText(_translate("SelvansGeo", "Utilisateur: ", None))
        self.label_5.setText(_translate("SelvansGeo", "Mot de passe: ", None))
        self.cmbConnection.setToolTip(_translate("SelvansGeo", "Choisissez le type de connexion", None))
        self.cmbConnection.setWhatsThis(_translate("SelvansGeo", "Pour modifier les données, choisir le mode édition", None))
        self.cmbConnection.setItemText(0, _translate("SelvansGeo", "Consultation", None))
        self.cmbConnection.setItemText(1, _translate("SelvansGeo", "Edition", None))
        self.btConnection.setToolTip(_translate("SelvansGeo", "Se connecte à la base de données et charge (recharge) le projet", None))
        self.btConnection.setWhatsThis(_translate("SelvansGeo", "Se connecter à la base de donnée et charger le projet", None))
        self.btConnection.setText(_translate("SelvansGeo", "Connexion", None))
        self.grpProjects.setTitle(_translate("SelvansGeo", "Projet QGIS SelvansGeo", None))
        self.btLoadProject.setToolTip(_translate("SelvansGeo", "Recharge le projet affiché ci-dessus", None))
        self.btLoadProject.setWhatsThis(_translate("SelvansGeo", "Permet de recharger le projet ouvert actuellement", None))
        self.btLoadProject.setText(_translate("SelvansGeo", "(Re) Charger le projet", None))
        self.btDefineDefaultProject.setToolTip(_translate("SelvansGeo", "Permet de charger par défaut un projet personnalisé", None))
        self.btDefineDefaultProject.setWhatsThis(_translate("SelvansGeo", "Permet de choisir un projet QGIS personnalisé et de le définir comme projet par défaut", None))
        self.btDefineDefaultProject.setText(_translate("SelvansGeo", "Définir un projet personnalisé", None))
        self.btResetDefaultProject.setToolTip(_translate("SelvansGeo", "Utiliser le projet standard fournit avec SelvansGeo", None))
        self.btResetDefaultProject.setWhatsThis(_translate("SelvansGeo", "Reprendre le project fournit avec le plugin et de le définir comme projet par défaut", None))
        self.btResetDefaultProject.setText(_translate("SelvansGeo", "Reprendre le projet standard", None))
        self.lblProject.setText(_translate("SelvansGeo", "Projet actuel:", None))
        self.lblCurrentProject.setWhatsThis(_translate("SelvansGeo", "Ceci est le chemin vers le fichier QGIS chargé actuellement", None))
        self.lblVersion.setText(_translate("SelvansGeo", "<html><head/><body><p>SelvansGeo <span style=\" font-weight:600;\">1.7</span> 10.11.2016 pour QGIS <span style=\" font-weight:600;\">2.14.0+</span></p></body></html>", None))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.connexionTab), _translate("SelvansGeo", "Connexion - Projet", None))
        self.cmbAnalysis.setToolTip(_translate("SelvansGeo", "Choix de l\'analyse thématique", None))
        self.cmbAnalysis.setWhatsThis(_translate("SelvansGeo", "Choisir une analyse", None))
        self.lblAnalysis.setText(_translate("SelvansGeo", "Choix de l\'analyse:", None))
        self.btAnalysis.setWhatsThis(_translate("SelvansGeo", "Lancer l\'analyse", None))
        self.btAnalysis.setText(_translate("SelvansGeo", "Lancer l\'analyse", None))
        self.chkSaveAnalysisResult.setToolTip(_translate("SelvansGeo", "Permet de sauver le résultat de l\'analyse dans un répertoire (sans la représentation)", None))
        self.chkSaveAnalysisResult.setWhatsThis(_translate("SelvansGeo", "Enregistrer le résultat de l\'analyse sur le disque au format ESRI shapefile", None))
        self.chkSaveAnalysisResult.setText(_translate("SelvansGeo", "Sauvegarder le résultat sur le disque", None))
        self.txtAnalysisName.setWhatsThis(_translate("SelvansGeo", "Chemin d\'enregistrement du fichier ESRI shapefile", None))
        self.txtMssqlQuery.setToolTip(_translate("SelvansGeo", "Reqête SQL sur SELVANS", None))
        self.btAdvancedUserMode.setToolTip(_translate("SelvansGeo", "Visualiser les détails de la requête SELVANS", None))
        self.btAdvancedUserMode.setWhatsThis(_translate("SelvansGeo", "Permet d\'afficher la requête complète correspondant à l\'analyse en cours", None))
        self.btAdvancedUserMode.setText(_translate("SelvansGeo", "Mode avancé", None))
        self.lblSql.setText(_translate("SelvansGeo", "Requête SQL Server", None))
        self.lblDateStart.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire", None))
        self.lblDateStart.setText(_translate("SelvansGeo", "Année", None))
        self.lnYearStart.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire", None))
        self.lnYearStart.setWhatsThis(_translate("SelvansGeo", "Saisir la date du plus ancien inventaire auquel on s\'intéresse", None))
        self.chkLastSurvey.setWhatsThis(_translate("SelvansGeo", "Ne considérer que l\'inventaire le plus récent", None))
        self.chkLastSurvey.setText(_translate("SelvansGeo", "Prendre la date la plus récente", None))
        self.label_6.setText(_translate("SelvansGeo", "Filtrer par administration:", None))
        self.txtAdmShortName.setToolTip(_translate("SelvansGeo", "Entrez le ou les noms court. Ex: BDY ou BDY;BRD", None))
        self.txtAdmShortName.setWhatsThis(_translate("SelvansGeo", "Saisir le ou les codes des administrations (Ex: BDY ou BDY, COT) ", None))
        self.lnYearEnd.setToolTip(_translate("SelvansGeo", "Date de fin de la période d\'analyse", None))
        self.lnYearEnd.setWhatsThis(_translate("SelvansGeo", "Choisir la date de l\'inventaire le plus récent auquel on s\'intéresse", None))
        self.lblDateEnd.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire", None))
        self.lblDateEnd.setText(_translate("SelvansGeo", "Fin", None))
        self.lblCoupeType.setToolTip(_translate("SelvansGeo", "Date de l\'inventaire", None))
        self.lblCoupeType.setText(_translate("SelvansGeo", "Motif de coupe:", None))
        self.lnCoupeType.setToolTip(_translate("SelvansGeo", "Saisir le ou les types de coupes (ex: 13 ou 1;13)", None))
        self.lnCoupeType.setWhatsThis(_translate("SelvansGeo", "Saisir le ou les types de coupes (ex: 13 ou 1;13)", None))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tabAnalysis), _translate("SelvansGeo", "Analyses", None))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tabAnalysis), _translate("SelvansGeo", "Analyses spatiale des données SELVANS actuelles", None))
        self.listArr.setToolTip(_translate("SelvansGeo", "Click: sélection des administrations d\'un arrondissement", None))
        self.listArr.setWhatsThis(_translate("SelvansGeo", "Sélectionner un arrondissement (simple click), zoomer: double click", None))
        self.listAdm.setToolTip(_translate("SelvansGeo", "click: sélection des divisions d\'une administration, double-click: zoom sur l\'administration", None))
        self.listAdm.setWhatsThis(_translate("SelvansGeo", "Sélectionner une administration (simple click), zoomer: double click", None))
        self.listDiv.setToolTip(_translate("SelvansGeo", "double-click: zoom sur la division", None))
        self.listDiv.setWhatsThis(_translate("SelvansGeo", "Sélectionner une division (simple click), zoomer: double click", None))
        self.label.setText(_translate("SelvansGeo", "Arrondissements", None))
        self.label_2.setText(_translate("SelvansGeo", "Administrations", None))
        self.label_3.setText(_translate("SelvansGeo", "Divisions", None))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tab_2), _translate("SelvansGeo", "Navigation", None))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tab_2), _translate("SelvansGeo", "Navigation par niveaux géographiques", None))
        self.grpViewNodes.setWhatsThis(_translate("SelvansGeo", "Ne calculer les noeuds que pour l\'emprise courante (visible) afin d\'aller plus vite", None))
        self.grpViewNodes.setTitle(_translate("SelvansGeo", "Visualiser les noeuds", None))
        self.chkSelectByCanvasExtent.setText(_translate("SelvansGeo", "Seulement pour l\'emprise courante", None))
        self.comboLayers.setToolTip(_translate("SelvansGeo", "Choisir une couche pour laquelle les noeuds doivent etre affichés. La création des noeuds peut prendre du temps...", None))
        self.comboLayers.setWhatsThis(_translate("SelvansGeo", "Choisir une couche pour laquelle les noeuds doivent etre affichés. La création des noeuds peut prendre du temps...", None))
        self.btHideNodes.setToolTip(_translate("SelvansGeo", "Supprime la couche des noeuds", None))
        self.btHideNodes.setWhatsThis(_translate("SelvansGeo", "Supprime la couche des noeuds", None))
        self.btHideNodes.setText(_translate("SelvansGeo", "Masquer", None))
        self.btShowNodes.setToolTip(_translate("SelvansGeo", "Lance l\'extraction de noeuds", None))
        self.btShowNodes.setWhatsThis(_translate("SelvansGeo", "Lance l\'extraction de noeuds", None))
        self.btShowNodes.setText(_translate("SelvansGeo", "Afficher", None))
        self.groupBox.setTitle(_translate("SelvansGeo", "Désactiver une couche en sélectionnant l\'un de ses objets", None))
        self.btDesactivateLayer.setToolTip(_translate("SelvansGeo", "Désactiver une couche par clique sur une entité de cette couche", None))
        self.btDesactivateLayer.setWhatsThis(_translate("SelvansGeo", "Permet de désactiver une couche par un click sur une entité lui appartenant", None))
        self.btDesactivateLayer.setText(_translate("SelvansGeo", "Désactiver une couche", None))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tabEdit), _translate("SelvansGeo", "Édition", None))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tabEdit), _translate("SelvansGeo", "Outils d\'éditions spécifiques SelvansGeo", None))
        self.btQgisHelp.setToolTip(_translate("SelvansGeo", "Afficher l\'aide en ligne QGIS", None))
        self.btQgisHelp.setWhatsThis(_translate("SelvansGeo", "Afficher l\'aide en ligne QGIS", None))
        self.btQgisHelp.setText(_translate("SelvansGeo", "Voir l\'aide QGIS", None))
        self.btSelvansGeoHelp.setToolTip(_translate("SelvansGeo", "Afficher le manuel utilisateur SelvansGeo", None))
        self.btSelvansGeoHelp.setWhatsThis(_translate("SelvansGeo", "Afficher le manuel utilisateur SelvansGeo", None))
        self.btSelvansGeoHelp.setText(_translate("SelvansGeo", "Voir l\'aide SelvanGeo", None))
        self.btQgisPrintComposerHelp.setToolTip(_translate("SelvansGeo", "Afficher l\'aide en ligne pour le composeur d\'impression", None))
        self.btQgisPrintComposerHelp.setWhatsThis(_translate("SelvansGeo", "Afficher l\'aide en ligne pour le composeur d\'impression", None))
        self.btQgisPrintComposerHelp.setText(_translate("SelvansGeo", "Voir l\'aide QGIS du composeur d\'impression", None))
        self.tabPanel.setTabText(self.tabPanel.indexOf(self.tab), _translate("SelvansGeo", "Aide", None))
        self.tabPanel.setTabToolTip(self.tabPanel.indexOf(self.tab), _translate("SelvansGeo", "Toutes les aides dont vous avez besoin !", None))

