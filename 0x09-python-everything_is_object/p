#!/bin/bash

for file in $@
do 
  echo "push fil: ${file}"
  chmod +700 ${file}
  git add ${file} && git commit -m "add task ${file:0:1}"
done
git push
