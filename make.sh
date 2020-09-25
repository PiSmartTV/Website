#!/bin/sh
DIR="$(dirname "$0")"

CSS_DIR="${DIR}/pitv/main/static/css"
JS_DIR="${DIR}/pitv/main/static/js"
IMG_DIR="${DIR}/pitv/main/static/images"

SCSS_DIR="${DIR}/pitv/style/style.scss"
JQUERY_JS="${DIR}/pitv/style/node_modules/jquery/dist/jquery.min.js"
BOOTSTRAP_JS="${DIR}/pitv/style/node_modules/bootstrap/dist/js/bootstrap.min.js"

mkdir -p ${CSS_DIR}
mkdir -p ${JS_DIR}
mkdir -p ${IMG_DIR}

npm --prefix "${DIR}/pitv/style/" ci --save

sass ${SCSS_DIR} "${CSS_DIR}/style.min.css" --style compressed
cp ${JQUERY_JS} ${JS_DIR}
cp ${BOOTSTRAP_JS} ${JS_DIR}
