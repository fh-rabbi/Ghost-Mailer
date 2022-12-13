#!/bin/bash

git add .
read -p '[*] Type Commit Message:' msg
git commit -m "$msg"
echo '[*] Pushing ...'
sleep 1
git push
