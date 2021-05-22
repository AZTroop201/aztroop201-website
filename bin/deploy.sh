#!/bin/bash
# Run Hugo and deploy public to gh-pages branch

cd home
rm -rf public

#HUGO_ENV sets up anake theme to allow indexing
HUGO_ENV=production hugo --minify
