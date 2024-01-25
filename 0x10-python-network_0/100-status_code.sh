#!/bin/bash
# Sends request -> (URL)
curl -s -o /dev/null -w "%{http_code}" "$1"
