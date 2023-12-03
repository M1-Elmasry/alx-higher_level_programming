#!/bin/bash
# display the size of the url response
echo -n $(curl -s ${1}) | wc -c
