######################################################################
# Automatically generated by qmake (2.01a) Thu Apr 7 08:35:17 2011
######################################################################

TEMPLATE = app

TARGET = 

DEPENDPATH += .

INCLUDEPATH += .\
.. \
../inc \
../inc.fc

LIBPATH += ../lib

LIBS += -lvisLib \
-losKernel \
-losShared

# Input
HEADERS += mainwindow.h \
    mainthread.h \
    fc_comunication.h

FORMS += mainwindow.ui

SOURCES += main.cpp mainwindow.cpp \
mainthread.cpp \
    fc_comunication.cpp

RESOURCES += \
    vistestqt.qrc

target.path += ../bin 
INSTALLS += target

