#!/bin/sh

rm -fr $(find $(dirname $0) -name "__pycache__" -o -name ".sass-cache")