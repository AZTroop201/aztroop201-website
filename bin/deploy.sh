#!/bin/bash
# Run Hugo and deploy public to gh-pages branch

cd home
rm -rf public
hugo --minify
