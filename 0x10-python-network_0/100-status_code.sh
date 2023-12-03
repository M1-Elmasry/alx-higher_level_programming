#!/bin/bash
# display allowed http status code for response of url
curl -sIX OPTIONS ${1} | head -n1 | cut -d " " -f2
