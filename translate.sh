#!/bin/bash

DIR="$(dirname $0)"
cd "${DIR}/pitv/"
django-admin makemessages -l ${1:-sr}
django-admin compilemessages