import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Shapes 1.12
import QtQuick.Dialogs 1.3
import QtQuick.Controls.Material 2.12
import Hulkster 1.0

ApplicationWindow {
    id: app
    Material.theme: Material.System
    Material.primary: Material.Red
    Material.accent: Material.Yellow
    visible: true
    minimumWidth: 1280
    minimumHeight: 720
    title: "Hulkamaniac"
    Extractor {
        id: extractor
        Component.onCompleted: listview.model = extractor.model
        // Component.onDestroyed: extractor.close()
        Component.onDestruction: extractor.close()
    }
    Rectangle {
        id: rte
        anchors.centerIn: parent
        anchors.fill: parent
        color: "#2D3037"
        opacity: 0.9

            property bool validFileName
            ColumnLayout {
                anchors.centerIn: parent
                anchors.fill: parent
                Rectangle {
                    id: contentmain
                    color: "transparent"
                    Layout.alignment: Qt.AlignHCenter
                    Layout.fillHeight: true;
                    Layout.fillWidth: true;

                    Component {
                        id: moditem
                        RowLayout {
                            spacing: 25
                            width: parent.width
                            Rectangle {
                                color: "transparent"
                                Layout.fillWidth: true
                                Layout.fillHeight: true
                            }
                            //                    UICalendarIcon { date: year }
                            Rectangle {
                                id: trect
                                width: 400
                                Text {
                                    font.pointSize: 14
                                    Material.theme: Material.Dark
                                    color: Material.foreground
                                    text: modelData
                                    anchors.centerIn: parent
                                    anchors.alignWhenCentered: false
                                    horizontalAlignment: Text.AlignHCenter
                                    verticalAlignment: Text.AlignVCenter
                                }
                            }
                            Button {
                                font.pointSize: 12
                                flat: true;
                                Material.background: Material.Yellow
                                Material.theme: Material.Light
                                text: "Extract";
                                onClicked: {
                                    extractor.extract(index)
                                }
                            }
                            Rectangle {
                                color: "transparent"
                                Layout.fillWidth: true
                                Layout.fillHeight: true
                            }
                        }
                    }

                    ColumnLayout {
                        anchors.fill: parent
                        spacing: 25
                        Rectangle {
                            color: "transparent"
                            height: 25 }
                        Rectangle {
                            color: "transparent"
                            x: x + 50
                            Layout.fillWidth: true
                            Layout.fillHeight: contentlist.visible ? false : true
                            Layout.alignment: Qt.AlignCenter
                            Text {
                                color: Material.color(Material.Red, Material.ShadeA200)
                                text: extractor.busy ? qsTr("Please Wait...") : qsTr("Choose a Database to Extract")
                                font.capitalization: Font.AllUppercase
                                font.bold: true
                                font.pointSize: 16
                                anchors.centerIn: parent
                                anchors.alignWhenCentered: false
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                        Rectangle {
                            id: contentlist
                            color: "transparent"
                            visible: !extractor.busy
                            Layout.fillHeight: true
                            Layout.fillWidth: true
                            Layout.alignment: Qt.AlignHCenter
                            ListView {
                                id: listview
                                clip: true
                                width: parent.width
                                anchors.fill: parent
                                anchors.centerIn: parent
                               // anchors.alignWhenCentered: true
                                model: extractor.model
                                delegate: moditem
                            }
                        }
                    }
                }
                Rectangle {
                    id: contentfooter
                    width: parent.width
                    height: 64
                    color: Material.accentColor
                    border.color: Qt.darker(Material.accentColor)
                    border.width: 1
                    Layout.fillWidth: true
                    RowLayout {
                        anchors.fill: parent
                        //rightMargin: 25
                        Rectangle {
                            color: "transparent"
                            Layout.fillHeight: true
                            Layout.fillWidth: true
                        }
                        Text {
                            font.pointSize: 12
                            Layout.alignment: Qt.AlignVCenter
                            Layout.leftMargin: 25
                            Layout.rightMargin: 25
                            text: app.title + " " + extractor.extractorVersion()
                        }
                        ProgressBar {
                            //Layout.fillWidth: true
                            Layout.rightMargin: 25
                            id: control
                            value: extractor.progress
                            padding: 2

                            background: Rectangle {
                                implicitWidth: 200
                                implicitHeight: 6
                                color: Material.accentColor
                                radius: 3
                            }

                            contentItem: Item {
                                implicitWidth: 200
                                implicitHeight: 4

                                Rectangle {
                                    width: control.visualPosition * parent.width
                                    height: parent.height
                                    radius: 2
                                    color: Material.primaryColor
                                }
                            }
                        }
                    }
                }

            //    FileDialog {
            //        id: fileDialog
            //        title: "Please choose a file"
            //        folder: shortcuts.home
            //        nameFilters: [ "TEW(TEW2013.mdb; TEW2016.mdb; TEW2020.mdb)" ]
            //        onAccepted: {
            //            console.log("You chose: " + fileDialog.fileUrls)
            //            close()
            //            extractor.setFile(fileDialog.fileUrl)
            //            alertblock: true
            //        }
            //        onRejected: {
            //            console.log("Canceled")
            //            close()
            //        }
            //    }

            //    Extractor {
            //        id: extractor
            //        onReady: {
            //            root.showAlert("Please Wait")
            //            extractor.run()
            //        }
            //        onProgressChanged: root.alertmsg = extractor.progress
            //        onFinished: dialog.close()
            //    }


            // Converter / Importer

            //    Converter {
            //        id: converter
            //        onProcess: converter.run()
            //        onFinished: {
            //            $pwp.send(Event.DBSave)
            //            dialog.close()
            //            list.setup()
            //        }
            //        onProgressChanged: root.alertmsg = converter.progress
            //    }


            //    Importer { id: importer
            //        onReady: root.showAlert("Please Wait")
            //        onProcess: importer.run()
            //        onFinished: converter.start()
            //        onProgressChanged: root.alertmsg = importer.progress
            //    }

        }
    }
}
