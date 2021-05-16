# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from menstruit import Ui_MainWindow


class Menstruit(QMainWindow):
    def __init__(self, title="Default", parent=None):
        super(Menstruit, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.title = title
        self.ui.setupUi(self)
        self.setWindowTitle(self.title)
        self.ui.button.clicked.connect(self.fonc)
        self.ui.button_3.clicked.connect(self.fonct)

    #########################################################################################################################################################
    #  Premiere partie du programme  "" toutes les fonctions dans cette sous partie se charge de calculer l'ovulation ""
    #########################################################################################################################################################
    def fevrier(self, a, b, c, d): # calcul d'ovulation du meme mois "fevrier"
        resultat = 0
        if b == d:
            for i in range(a, c + 1):
                resultat +=1
            # res = resultat - 14
            # print('vos jours fertile sont du  %d Fevrier  au %d Fevrier ' % (res - 2, res+3 ))
            self.ui.label_8.setText(str(resultat))
            print(resultat)
            ress = resultat + int(c)
            a = ress - 28
            print(a)
            res = a - 14

    def janvier(self, a, b, c, d): # meme mois "janvier"
        resultat = 0
        if b == d:
            for i in range(a, c + 1):
                resultat +=1
            print(resultat)
            ress = resultat + c
            self.ui.label_8.setText(str(resultat))
            n = ress - 31
            print(n)
            res = n - 14
            print(res)

# cette fonction gere  les autres mois finisans le 30 du meme mois
    def autre(self, a, b, c, d):
        resultat = 0
        for i in range(a, c + 1):
            resultat +=1
        print(resultat)
        self.ui.label_8.setText(str(resultat))
# celle ci gere  les mois finissant le 31 du meme mois
    def autres(self, a, b, c, d):
        resultat = 0
        for i in range(a, c + 1):
            resultat +=1
        print(resultat)
        self.ui.label_8.setText(str(resultat))

 # Toutes les fonctions  en dessous gere d'un mois à un autre

    def fev_avril(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 28 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        self.ui.label_8.setText(str(resultat))
        an = ress - 30
        print(resultat)

    def fev_mars(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 28 + 1):
            resultat += 1
        resultat += c
        print(resultat)
        self.ui.label_8.setText(str(resultat))


    def janv_mars(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 31 + 1):
            resultat += 1
        resultat += c + 28
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def avril_juin(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def juin_auot(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def auot_octobre(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def octobre_decembre(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def autre_plus(self, a, b, c, d):
        if self.ui.mois.currentIndex() == 3 or self.ui.mois.currentIndex() == 5 or self.ui.mois.currentIndex() == 8 or self.ui.mois.currentIndex() == 10:
            d = self.ui.mois_2.currentIndex()
            print(d)
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def autres_mois(self, a, b, c, s):
        d = 0
        if self.ui.mois.currentIndex():
            d = self.ui.mois_2.currentIndex()
            print(d)
        resultat = 0
        for x in range(a, 31 + 1):
            resultat += 1
        resultat += c
        print(resultat)
        self.ui.label_8.setText(str(resultat))


    def mars_mai(self, a, b, c, s):
        if self.ui.mois.currentIndex() == 2:
            d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 31 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def mai_juillet(self, a, b, c, s):
        if self.ui.mois.currentIndex():
            d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 31 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def juillet_septembre(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 31 + 1):
            resultat += 1
        resultat += c + 30
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    def septembre_novembre(self, a, b, c, d):
        d = self.ui.mois_2.currentIndex()
        resultat = 0
        for x in range(a, 30 + 1):
            resultat += 1
        resultat += c + 31
        ress = resultat + c
        an = ress - 30
        print(resultat)
        self.ui.label_8.setText(str(resultat))

    #########################################################################################################################################################
    # Deuxime partie du programme "" dans cette dexieme sous partie du prog avec le cycle definit on calcue les prochaine menstruation ""                   #
    #########################################################################################################################################################

    def janvier_autres(self, a, b, c, d): # appelé janvier_autres pour eviter la confusion de nom
        """ tous les fonction predefini dans cette sous partie joue le meme role le calcul de menstruation
            celle ci s'occupe de des mois se terminant le 31
        """
        d = 0
        if self.ui.mois_3.currentIndex():
            d = self.ui.mois_3.currentIndex()
        ress = a + c
        an = ress - 31
        print(an)
        if an == 0:
            an = 31
            print(an)
            res = an - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 3, res + 3))
            l_date = QDate(2021, d+1, res - 3)

            # upper bound date
            u_date = QDate(2021, d+1, res + 3)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        elif an < 0:
            print(an)
            cn = 31 + an
            print(cn)
            res = cn - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 2, res + 2))
            l_date = QDate(2021, d+1, res - 2)

            # upper bound date
            u_date = QDate(2021, d+1, res + 2)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        else:
            print(an)
            res = an - 14
            print(res)
            if res < 0:
                cn = 31 + res
                print(cn)
                bn = cn + 2
                if bn > 31:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn-2, bn - 31))
                    l_date = QDate(2021, d+1, cn-2)

                    # upper bound date
                    u_date = QDate(2021, d + 2, bn - 31)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn - 2, cn + 2))
                    l_date = QDate(2021, d+1, cn - 2)

                    # upper bound date
                    u_date = QDate(2021, d+1, cn + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
            elif res == 0:
                cn = 31 - 2
                print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn, 2))
                l_date = QDate(2021, d+1, cn)

                # upper bound date
                u_date = QDate(2021, d + 2, 2)
                # self.ui.calendarWidget.setCurrentPage(2021, 3)
                self.ui.calendarWidget.setDateRange(l_date, u_date)
            else:
                an = res - 2
                if an < 0:
                    ax = 31 + an
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (ax, res + 2))
                    l_date = QDate(2021, d+1 , ax)

                    # upper bound date
                    u_date = QDate(2021, d + 2, res + 1)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                elif an == 0:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (31, res + 2))
                    l_date = QDate(2021, d+1, 30)

                    # upper bound date
                    u_date = QDate(2021, d + 2, res + 1)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (an, res + 2))
                    l_date = QDate(2021, d + 2, an)

                    # upper bound date
                    u_date = QDate(2021, d + 2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)


    def fevrier_autres(self, a, b, c, d):
        """Fevrier etant un mois particulier, un fonction lui est entierement dedié pour le calcul"""
        if self.ui.jours_3.currentIndex():
            d = self.ui.mois_3.currentIndex()
        print(d)
        ress = a + c
        an = ress - 28
        print(an)
        if an == 0:
            an = 29
            print(an)
            res = an - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 3, res + 3))
            l_date = QDate(2021, d+1 , res - 3)

            # upper bound date
            u_date = QDate(2021, d+1 , res + 3)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        elif an < 0:
            print(an)
            cn = 28 + an
            print(cn)
            res = cn - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 2, res + 2))
            l_date = QDate(2021, d+1 , res - 2)

            # upper bound date
            u_date = QDate(2021, d+1 , res + 2)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        else:
            print(an)
            res = an - 14
            print(res)
            if res < 0:
                cn = 28 + res
                print(cn)
                bn = cn + 3
                if bn > 28:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn, bn - 28))
                    l_date = QDate(2021, d+1 , cn)

                    # upper bound date
                    u_date = QDate(2021, d + 2, bn - 28)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn - 2, cn + 2))
                    l_date = QDate(2021, d+2 , cn - 2)

                    # upper bound date
                    u_date = QDate(2021, d+2 , cn + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
            elif res == 0:
                cn = 28 - 2
                print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn, 2))
                l_date = QDate(2021, d+1 , cn)

                # upper bound date
                u_date = QDate(2021, d+2, 2)
                # self.ui.calendarWidget.setCurrentPage(2021, 3)
                self.ui.calendarWidget.setDateRange(l_date, u_date)
            else:
                an = res - 2
                if an < 0:
                    ax = 28 + an
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (ax, res + 2))
                    l_date = QDate(2021, d+1, ax)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                elif an == 0:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (28, res + 2))
                    l_date = QDate(2021, d+1, 28)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (an, res + 2))
                    l_date = QDate(2021, d+2, an)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)



    def juin_autres(self, a, b, c, d):
        """Cette fonction joue le meme role que les precedentes mais gere seulement pour les mois finisant le 30 """
        d = 0
        if self.ui.jours_3.currentIndex():
            d = self.ui.mois_3.currentIndex()
        ress = a + c
        an = ress - 30
        print(an)
        if an == 0:
            an = 30
            print(an)
            res = an - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 2, res + 2))
            l_date = QDate(2021, d+1 , res - 2)

            # upper bound date
            u_date = QDate(2021, d+1 , res + 2)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        elif an < 0:
            print(an)
            cn = 30 + an
            print(cn)
            res = cn - 14
            # b = 31+res
            print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (res - 2, res + 2))
            l_date = QDate(2021, d + 1, res - 2)

            # upper bound date
            u_date = QDate(2021, d + 1, res + 2)
            # self.ui.calendarWidget.setCurrentPage(2021, 3)
            self.ui.calendarWidget.setDateRange(l_date, u_date)
        else:
            print(an)
            res = an - 14
            print(res)
            if res < 0:
                cn = 30 + res
                print(cn)
                bn = cn + 2
                if bn > 30:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn, bn - 30))
                    l_date = QDate(2021, d + 1, cn)

                    # upper bound date
                    u_date = QDate(2021, d + 2, bn - 30)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn - 2, cn + 2))
                    l_date = QDate(2021, d + 1, cn - 2)

                    # upper bound date
                    u_date = QDate(2021, d + 1, cn + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
            elif res == 0:
                cn = 30 - 2
                print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (cn, 2))
                l_date = QDate(2021, d + 1, cn)

                # upper bound date
                u_date = QDate(2021, d + 2, 2)
                # self.ui.calendarWidget.setCurrentPage(2021, 3)
                self.ui.calendarWidget.setDateRange(l_date, u_date)
            else:
                an = res - 2
                if an < 0:
                    ax = 30 + an
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (ax, res + 2))
                    l_date = QDate(2021, d+1, ax)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                elif an == 0:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (30, res + 2))
                    l_date = QDate(2021, d+1, 30)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)
                else:
                    print('vos jours fertiles seront du  %d  au %d  du mois prochain' % (an, res + 2))
                    l_date = QDate(2021, d+2, an)

                    # upper bound date
                    u_date = QDate(2021, d+2, res + 2)
                    # self.ui.calendarWidget.setCurrentPage(2021, 3)
                    self.ui.calendarWidget.setDateRange(l_date, u_date)


    def fonc(self):
        a = int(self.ui.jours.currentText())
        b = self.ui.mois.currentText()
        c = int(self.ui.jours_2.currentText())
        d = self.ui.mois_2.currentText()
        if b == d:
            if self.ui.mois.currentIndex() == 0:
                self.janvier(a, b, c, d)
            elif self.ui.mois.currentIndex() == 1:
                self.fevrier(a, b, c, d)
            elif self.ui.mois.currentIndex() == 3 or self.ui.mois.currentIndex() == 5 or self.ui.mois.currentIndex() == 8 or self.ui.mois.currentIndex() == 10:
                self.autre(a, b, c, d)
            else:
                self.autres(a, b, c, d)

        elif self.ui.mois.currentIndex() == 1 and self.ui.mois_2.currentIndex() == 2:
            self.fev_mars(a, b, c, d)

        elif self.ui.mois.currentIndex() == 1 and self.ui.mois_2.currentIndex() == 3:
            self.fev_avril(a, b, c, d)

        elif self.ui.mois.currentIndex() == 3 and self.ui.mois_2.currentIndex() == 5:
            self.avril_juin(a, b, c, d)

        elif self.ui.mois.currentIndex() == 2 and self.ui.mois_2.currentIndex() == 4:
            self.mars_mai(a, b, c, d)

        elif self.ui.mois.currentIndex() == 4 and self.ui.mois_2.currentIndex() == 6:
            self.mai_juillet(a, b, c, d)

        elif self.ui.mois.currentIndex() == 6 and self.ui.mois_2.currentIndex() == 8:
            self.juillet_septembre(a, b, c, d)

        elif self.ui.mois.currentIndex() == 8 and self.ui.mois_2.currentIndex() == 10:
            self.septembre_novembre(a, b, c, d)

        elif self.ui.mois.currentIndex() == 3 or self.ui.mois.currentIndex() == 5 or self.ui.mois.currentIndex() == 8 or self.ui.mois.currentIndex() == 10:
            self.autre_plus(a, b, c, d)

        elif self.ui.mois.currentIndex() == 0 and self.ui.mois_2.currentIndex() == 2:
            self.janv_mars(a, b, c, d)

        else:
            self.autres_mois(a, b, c, d)

    def fonct(self):
        a = int(self.ui.jours_3.currentText())
        b = self.ui.mois_3.currentText()
        c = int(self.ui.jours_4.currentText())
        d = self.ui.mois_2.currentText()
        if self.ui.mois_3.currentIndex() == 0 or self.ui.mois_3.currentIndex() == 2 or self.ui.mois_3.currentIndex() == 4 or self.ui.mois_3.currentIndex() == 6 or self.ui.mois_3.currentIndex() == 7 or self.ui.mois_3.currentIndex() == 9 or self.ui.mois_3.currentIndex() == 11:
            self.janvier_autres(a, b, c, d)

        if self.ui.mois_3.currentIndex() == 1:
            self.fevrier_autres(a, b, c, d)

        if self.ui.mois_3.currentIndex() == 3 or self.ui.mois_3.currentIndex() == 5 or self.ui.mois_3.currentIndex() == 8 or self.ui.mois_3.currentIndex() == 10:
            self.juin_autres(a, b, c, d)


# comme dans un programme ordinaire nous lançons le programme   
if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = Menstruit('Calcul ovulation')

    style = """
        QWidget{
            background: 
        }
         QPushButton
        {
            color: white;
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 2px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
        }

        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #0892D0;
            }
        QLabel{
            color: blue;
        }
           QLabel#label_2{
            color: black;
            background-color: yellow;
        }

         QLabel#label_3{
            color: black;
            background-color: orange;
        }
    """
    app.setStyleSheet(style)

    myWindow.show()

    sys.exit(app.exec_())

