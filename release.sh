#!/bin/bash
if [ -z "$1" ]; then
    echo "Version not specified"
    exit 1
elif [ -z "$GITHUB_API_TOKEN" ]; then
    echo "Github key must be set in GITHUB_API_TOKEN env variable"
    exit 1
else
    git checkout develop && \
    git pull && \
    git pull --tags -f
    git branch -d $(git branch | grep release)
    git flow release start $1 && \
    echo -n $1 > VERSION && \
    git tag -a $1 -m "Release $1" && \
    git push origin --tags && \
    git add --all && \
    git commit -n -m "Release $1" && \
    git flow release publish $1 && \
    gh pr create --base develop --title "Release $1 to develop" --body '' && \
    gh pr create --base master --title "Release $1 to production" --body ''
fi
