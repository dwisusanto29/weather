if [ -z "`git branch | grep builds`" ]; then
  git co -b builds
else
  git co builds
fi

git add .
git commit -a -m "`date +'Build on %F at %r'`"
# ignore git-commit exiting >0, since nothing to commit is fine
git push
exit 0
