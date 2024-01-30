#!/usr/bin/python3
""" The variable X-Request-Id """
import sys
import requests

if __name__ == "__main__":
    """ main """
    url_data = sys.argv[1]
    b = requests.get(url_data)
    print(b.headers.get("X-Request-Id"))
