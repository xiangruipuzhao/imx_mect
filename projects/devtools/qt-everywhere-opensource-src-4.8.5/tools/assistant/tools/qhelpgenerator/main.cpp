/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt Assistant of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and Digia.  For licensing terms and
** conditions see http://qt.digia.com/licensing.  For further information
** use the contact form at http://qt.digia.com/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Digia gives you certain additional
** rights.  These rights are described in the Digia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3.0 as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU General Public License version 3.0 requirements will be
** met: http://www.gnu.org/copyleft/gpl.html.
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "../shared/helpgenerator.h"

#include <QtCore/QDir>
#include <QtCore/QFileInfo>
#include <QtCore/QCoreApplication>
#include <QtCore/QTranslator>
#include <QtCore/QLocale>
#include <QtCore/QLibraryInfo>

#include <private/qhelpprojectdata_p.h>

QT_USE_NAMESPACE

class QHG {
    Q_DECLARE_TR_FUNCTIONS(QHelpGenerator)
};

int main(int argc, char *argv[])
{
    QString error;
    QString arg;
    QString compressedFile;
    QString projectFile;
    QString basePath;
    bool showHelp = false;
    bool showVersion = false;
    bool checkLinks = false;

    QCoreApplication app(argc, argv);
#ifndef Q_OS_WIN32
    QTranslator translator;
    QTranslator qtTranslator;
    QTranslator qt_helpTranslator;
    QString sysLocale = QLocale::system().name();
    QString resourceDir = QLibraryInfo::location(QLibraryInfo::TranslationsPath);
    if (translator.load(QLatin1String("assistant_") + sysLocale, resourceDir)
        && qtTranslator.load(QLatin1String("qt_") + sysLocale, resourceDir)
        && qt_helpTranslator.load(QLatin1String("qt_help_") + sysLocale, resourceDir)) {
        app.installTranslator(&translator);
        app.installTranslator(&qtTranslator);
        app.installTranslator(&qt_helpTranslator);
    }
#endif // Q_OS_WIN32

    for (int i = 1; i < argc; ++i) {
        arg = QString::fromLocal8Bit(argv[i]);
        if (arg == QLatin1String("-o")) {
            if (++i < argc) {
                QFileInfo fi(QString::fromLocal8Bit(argv[i]));
                compressedFile = fi.absoluteFilePath();
            } else {
                error = QHG::tr("Missing output file name.");
            }
        } else if (arg == QLatin1String("-v")) {
            showVersion = true;
        } else if (arg == QLatin1String("-h")) {
            showHelp = true;
        } else if (arg == QLatin1String("-c")) {
            checkLinks = true;
        } else {
            QFileInfo fi(arg);
            projectFile = fi.absoluteFilePath();
            basePath = fi.absolutePath();
        }
    }

    if (showVersion) {
        fputs(qPrintable(QHG::tr("Qt Help Generator version 1.0 (Qt %1)\n")
                         .arg(QT_VERSION_STR)), stdout);
        return 0;
    }

    if (projectFile.isEmpty() && !showHelp)
        error = QHG::tr("Missing Qt help project file.");

    QString help = QHG::tr("\nUsage:\n\n"
        "qhelpgenerator <help-project-file> [options]\n\n"
        "  -o <compressed-file>   Generates a Qt compressed help\n"
        "                         file called <compressed-file>.\n"
        "                         If this option is not specified\n"
        "                         a default name will be used.\n"
        "  -c                     Checks whether all links in HTML files\n"
        "                         point to files in this help project.\n"
        "  -v                     Displays the version of \n"
        "                         qhelpgenerator.\n\n");

    if (showHelp) {
        fputs(qPrintable(help), stdout);
        return 0;
    }else if (!error.isEmpty()) {
        fprintf(stderr, "%s\n\n%s", qPrintable(error), qPrintable(help));
        return -1;
    }

    QFile file(projectFile);
    if (!file.open(QIODevice::ReadOnly)) {
        fputs(qPrintable(QHG::tr("Could not open %1.\n").arg(projectFile)), stderr);
        return -1;
    }

    if (compressedFile.isEmpty()) {
        if (!checkLinks) {
            QFileInfo fi(projectFile);
            compressedFile = basePath + QDir::separator()
                             + fi.baseName() + QLatin1String(".qch");
        }
    } else {
        // check if the output dir exists -- create if it doesn't
        QFileInfo fi(compressedFile);
        QDir parentDir = fi.dir();
        if (!parentDir.exists()) {
            if (!parentDir.mkpath(QLatin1String("."))) {
                fputs(qPrintable(QHG::tr("Could not create output directory: %1\n")
                                 .arg(parentDir.path())), stderr);
            }
        }
    }

    QHelpProjectData *helpData = new QHelpProjectData();
    if (!helpData->readData(projectFile)) {
        fprintf(stderr, "%s\n", qPrintable(helpData->errorMessage()));
        return -1;
    }

    HelpGenerator generator;
    bool success = true;
    if (checkLinks)
        success = generator.checkLinks(*helpData);
    if (success && !compressedFile.isEmpty())
        success = generator.generate(helpData, compressedFile);
    delete helpData;
    if (!success) {
        fprintf(stderr, "%s\n", qPrintable(generator.error()));
        return -1;
    }
    return 0;
}
