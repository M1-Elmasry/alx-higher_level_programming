#!/bin/bash
# sent a json with post request to url
curl -sX POST -H "Content-Type: application/json" --data "@$2" "$1"
