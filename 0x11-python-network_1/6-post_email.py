#!/usr/bin/python3
""" packages requests and sys """
import sys
import requests

if __name__ == "__main__":
    """ main """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
