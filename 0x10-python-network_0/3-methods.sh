#!/bin/bash
# display allowed http method for input url
curl -sIX OPTIONS ${1} | grep "Allow" | cut -d: -f2 | cut -c 2-
