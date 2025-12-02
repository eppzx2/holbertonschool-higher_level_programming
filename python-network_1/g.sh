#!/usr/bin/env bash
echo "add a message"
read message

git add .
git commit -m "$message"
git push
