#!/usr/bin/sh

QMLBENCH_DEV=/home/jonas/Code/build-qmlbench-Qt_dev-Release/src/qmlbench
QMLBENCH_515=/home/jonas/Code/build-qmlbench-Qt_5_15-Release/src/qmlbench
TEST_PATH=/home/jonas/Code/qmlbench/benchmarks/auto/
OUTPUT_PATH=/home/jonas/Code/results3

QMLBENCH_DEV_CMD="$QMLBENCH_DEV $TEST_PATH --json --shell frame-count --repeat 2"
QMLBENCH_515_CMD="$QMLBENCH_515 $TEST_PATH --json --shell frame-count --repeat 2"

mkdir $OUTPUT_PATH

echo "Running Qt 5.15 OpenGL"
QSG_INFO=1 $QMLBENCH_515_CMD --id 5_15_opengl > $OUTPUT_PATH/qt-5_15-opengl.json
echo "Running Qt dev OpenGL"
QSG_INFO=1 $QMLBENCH_DEV_CMD --id dev_opengl > $OUTPUT_PATH/qt-dev-opengl.json
echo "Running Qt dev RHI OpenGL"
QSG_INFO=1 QSG_RHI=1 QSG_RHI_BACKEND=opengl $QMLBENCH_DEV_CMD --id dev_rhi_opengl > $OUTPUT_PATH/qt-dev-rhi-opengl.json
echo "Running Qt dev RHI Vulkan"
QSG_INFO=1 QSG_RHI=1 QSG_RHI_BACKEND=vulkan $QMLBENCH_DEV_CMD --id dev_rhi_vulkan > $OUTPUT_PATH/qt-dev-rhi-vulkan.json

