#!/bin/sh
DIR="$(dirname "$0")/../"

CSS_DIR="${DIR}/pitv/main/static/css"
JS_DIR="${DIR}/pitv/main/static/js"
IMG_DIR="${DIR}/pitv/main/static/images"
FONT_DIR="${DIR}/pitv/main/static/fonts"
FAVICON="${IMG_DIR}/logo2.png"

SCSS_DIR="${DIR}/pitv/style/style.scss"
JQUERY_JS="${DIR}/pitv/style/node_modules/jquery/dist/jquery.min.js"
BOOTSTRAP_JS="${DIR}/pitv/style/node_modules/bootstrap/dist/js/bootstrap.min.js"
BOOTSTRAP_JS_MAP="${BOOTSTRAP_JS}.map"

PURGECSS_BIN="${DIR}/pitv/style/node_modules/purgecss/bin/purgecss.js"
TEMPLATE_DIR="${DIR}/pitv/main/templates/**"

DOSIS_FONTS_PATH="${DIR}/pitv/style/node_modules/@fontsource/dosis/files/"
DOSIS_FONTS="dosis-all-400-normal.woff dosis-latin-400-normal.woff2"

mkdir -p ${CSS_DIR}
mkdir -p ${JS_DIR}
mkdir -p ${IMG_DIR}
mkdir -p ${FONT_DIR}

npm --prefix "${DIR}/pitv/style/" ci --save

convert -resize x32 -gravity center -crop 32x32+0+0 "${FAVICON}" -colors 256 -background transparent -flatten "${IMG_DIR}/favicon.ico"
sass ${SCSS_DIR} "${CSS_DIR}/style.min.css" --style compressed
node ${PURGECSS_BIN} --css "${CSS_DIR}/style.min.css" --content "${TEMPLATE_DIR}" --output "${CSS_DIR}/style.min.css"
cp ${JQUERY_JS} ${JS_DIR}
cp ${BOOTSTRAP_JS} ${JS_DIR}
cp ${BOOTSTRAP_JS_MAP} ${JS_DIR}

for FONT in $DOSIS_FONTS; do
    cp "${DOSIS_FONTS_PATH}${FONT}" ${FONT_DIR}
done
