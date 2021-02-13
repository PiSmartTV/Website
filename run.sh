#!/bin/sh

DIR="$(dirname $0)"

. "${DIR}/make.sh"
find "${DIR}/pitv/style" -maxdepth 1 -type f | entr -p "${DIR}/make.sh" &
python3 "${DIR}/pitv/manage.py" "runserver" "${@:2}"