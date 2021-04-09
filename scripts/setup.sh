#!/bin/bash

DIR="$(dirname "$0")"

eval "${DIR}/manage.sh migrate"
eval "${DIR}/manage.sh createsuperuser"
eval "${DIR}/make.sh"
eval "${DIR}/manage.sh collectstatic"
eval "${DIR}/translate.sh"