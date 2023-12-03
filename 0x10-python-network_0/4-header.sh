#!/bin/bash
# send a get request to url with an extra header key
curl -s --header "X-School-User-Id: 98" ${1}
