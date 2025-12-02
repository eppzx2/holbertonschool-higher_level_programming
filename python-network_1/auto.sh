#!/usr/bin/env bash
echo "filename please: "
read file
chmod +x $file

echo "your commit message"
read message

git add .
git commit -m "$message"
git push
