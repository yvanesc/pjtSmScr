#!/bin/bash
# declare 
git add --all
git status
echo "------------------------------"
echo "Comments to add for the commit"
read cmt
git commit -am '$cmt'
