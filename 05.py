import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

with urllib.request.urlopen(url) as f:
    result = pickle.load(f)
    for line in result:
        print("".join([k * v for k, v in line]))