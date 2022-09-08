#!/bin/sh
runex() {
    echo "Running $1"
    echo ""
    QSG_RHI_BACKEND=opengl QSG_CORE_PROFILE=1 /home/jonas/Coding/install/qt-dev/bin/qmlscene "$1"
    #ls $NAME
}

#runex ./3d_input/main.qml
#runex ./blendmodes/main.qml
#runex ./cameralookat/main.qml
#runex ./dynamic3DTest/main.qml
#runex ./instancing/main.qml
#runex ./lightmap/main.qml
#runex ./loader2/main.qml
#runex ./loader/main.qml
#runex ./modelparticles/main.qml
runex ./multicubetest/main.qml
#runex ./principledmaterial/main.qml
#runex ./projectionmodes/main.qml
#runex ./repeater3d/main.qml
#runex ./shadowCasting/main.qml
#runex ./sourceitem/main.qml
#runex ./stereoscopic/main.qml
#runex ./vertexAttributes/main.qml
#runex ./view3DDeleteTest/main.qml
