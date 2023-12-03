#!/bin/bash
# send a get request to url with an extra header key
curl -s -X POST --data "email=test@gmail.com&subject=I will always be here for PLD" ${1}
