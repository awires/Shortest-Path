

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QColor
import random

#####################################
#                                   #
#   random color                    #
#   from pyqt Wiki (copy/paste)     #
#                                   #
#####################################
def randomColor():

    red = 205 + random.random() * 50
    green = 205 + random.random() * 50
    blue = 205 + random.random() * 50
    alpha = 91 + random.random() * 100
    return QColor(red, green, blue, alpha)



#####################################
#                                   #
#   create a big graph              #
#   fix global variable!!!          #
#                                   #
#####################################
#def breadboard():
G={}
for ii in range(10):
    for kk in range(40):
        temp=(ii,kk)
        #top row
        if ii == 0:
            if kk == 0:
                G[temp]={(ii,kk+1):1, (ii+1,kk):1}
            elif kk == 39:
                G[temp]={(ii,kk-1):1, (ii+1,kk):1}
            else:
                G[temp]={(ii,kk-1):1, (ii,kk+1):1, (ii+1,kk):1}
        #bottom row
        elif ii == 9:
            if kk == 0:
                G[temp]={(ii,kk+1):1, (ii-1,kk):1}
            elif kk == 39:
                G[temp]={(ii,kk-1):1, (ii-1,kk):1}
            else:
                G[temp]={(ii,kk-1):1, (ii,kk+1):1, (ii-1,kk):1}
        #every other row
        else:
            if kk == 0:
                G[temp]={(ii,kk+1):1, (ii-1,kk):1, (ii+1,kk):1}
            elif kk == 39:
                G[temp]={(ii,kk-1):1, (ii-1,kk):1, (ii+1,kk):1}
            else:
                G[temp]={(ii,kk-1):1, (ii,kk+1):1, (ii-1,kk):1, (ii+1,kk):1}               
print "worked"
    #return(G)

##------------------------------##
##                              ##
##  shortest distance from beg  ##
##  to end                      ##
##                              ##
##------------------------------##

def shortpath(beg,end):

    visited = {beg:0}
    path={}

    G2=dict(G)
    #find all paths!
    while G2:
        shortnode = 0
        for node in G2:
            #find shortest path from a node
            if node in visited:
                if shortnode == 0:
                    shortnode=node
                elif visited[node] < visited[shortnode]:
                    shortnode = node

        if shortnode == 0:
            print "Path does not exist. Start over...."
            print "\n"
            print "\n"
            #start()
            break
        tempcost = visited[shortnode]

        for edge in G2[shortnode]:
            cost = tempcost + G2[shortnode][edge]
            if edge not in visited or cost < visited[edge]:
                visited[edge] = cost
                path[edge] = shortnode
                
        del G2[shortnode]
    cost = visited[end]
    #shortest path    
    shortestpath = [end]

    while end != beg:
        shortestpath.append(path[end])
        end = path[end]
    shortestpath.reverse()


    print "Your shortest path is: "
    print shortestpath
    print "\n"
    print "At a cost of: ", cost

    #append G
    for things in shortestpath:
        del G[things]

    return(shortestpath)

#################################
#                               #
#   GUI Stuff                   #
#                               #
#################################

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

class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Short Path"))
        Form.resize(1044, 236)
        self.tblGrid = QtGui.QTableWidget(Form)
        self.tblGrid.setEnabled(False)
        self.tblGrid.setGeometry(QtCore.QRect(0, 0, 1051, 211))
        self.tblGrid.setLineWidth(1)
        self.tblGrid.setProperty("showDropIndicator", False)
        self.tblGrid.setDragEnabled(False)
        self.tblGrid.setDragDropOverwriteMode(False)
        self.tblGrid.setAlternatingRowColors(False)
        self.tblGrid.setGridStyle(QtCore.Qt.SolidLine)
        self.tblGrid.setRowCount(10)
        self.tblGrid.setColumnCount(40)
        self.tblGrid.setObjectName(_fromUtf8("tblGrid"))
        #make the cells in table 
        for ii in range(10):
            for kk in range(40):
                item = QtGui.QTableWidgetItem()
                self.tblGrid.setItem(ii, kk, item)
                
        self.tblGrid.horizontalHeader().setVisible(False)
        self.tblGrid.horizontalHeader().setDefaultSectionSize(26)
        self.tblGrid.horizontalHeader().setHighlightSections(False)
        self.tblGrid.horizontalHeader().setMinimumSectionSize(20)
        self.tblGrid.horizontalHeader().setSortIndicatorShown(False)
        self.tblGrid.horizontalHeader().setStretchLastSection(False)
        self.tblGrid.verticalHeader().setVisible(False)
        self.tblGrid.verticalHeader().setDefaultSectionSize(20)
        self.tblGrid.verticalHeader().setMinimumSectionSize(20)
        self.tblGrid.verticalHeader().setSortIndicatorShown(False)
        self.tblGrid.verticalHeader().setStretchLastSection(False)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 210, 231, 16))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnFind = QtGui.QPushButton(Form)
        self.btnFind.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.btnFind.setObjectName(_fromUtf8("btnFind"))
        self.txtEnd = QtGui.QTextEdit(Form)
        self.txtEnd.setGeometry(QtCore.QRect(160, 210, 61, 21))
        self.txtEnd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtEnd.setObjectName(_fromUtf8("txtEnd"))
        self.txtBeg = QtGui.QTextEdit(Form)
        self.txtBeg.setGeometry(QtCore.QRect(50, 210, 61, 21))
        self.txtBeg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtBeg.setObjectName(_fromUtf8("txtBeg"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)

        self.btnFind.clicked.connect(self.on_btnFind)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        __sortingEnabled = self.tblGrid.isSortingEnabled()
        self.tblGrid.setSortingEnabled(False)

        #populate the table
        for ii in range(10):
            for kk in range(40):
                temp=chr(ii+97)+str(kk+1)
                item = self.tblGrid.item(ii, kk)
                item.setText(_translate("Form", temp, None))

        self.tblGrid.setSortingEnabled(__sortingEnabled)
        self.btnFind.setText(_translate("Form", "Find Path", None))
        self.label_2.setText(_translate("Form", "End", None))
        self.label_3.setText(_translate("Form", "Start", None))
        
    #############################
    #                           #
    #   do things when i click  #
    #   the button              #
    #                           #
    #############################
    def on_btnFind(self):
        #G=breadboard()
        beg1 = self.txtBeg.toPlainText()
        end1 = self.txtEnd.toPlainText()
        beg2 = str(beg1)
        end2 = str(end1)
        if len(beg2) == 2:
            t1=beg2[0]
            t2=beg2[1]
            beg=(ord(t1)-97,ord(t2)-49)
        elif len(beg2) == 3:
            t1=beg2[0]
            t2=beg2[1]+beg2[2]
            beg=(ord(t1)-97,int(t2)-1)
        if len(end2) == 2: 
            t1=end2[0]
            t2=end2[1]
            end=(ord(t1)-97,ord(t2)-49)
        elif len(end2) == 3:
            t1=end2[0]
            t2=end2[1]+end2[2]
            end=(ord(t1)-97,int(t2)-1)
        path=shortpath(beg,end)
        #update the table
        color = randomColor()
        for nodes in path:
            item = self.tblGrid.item(nodes[0], nodes[1])
            item.setText(_translate("Form", 'x', None))
            item.setBackgroundColor(color)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



