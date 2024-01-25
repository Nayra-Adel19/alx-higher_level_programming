#!/bin/bash
# Takes in a URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
