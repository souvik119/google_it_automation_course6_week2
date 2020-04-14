#! /usr/bin/env python3

import os
import requests

for filename in os.listdir('/data/feedback'):
        if filename.endswith('.txt'):
                with open(os.path.join('/data/feedback/', filename)) as f:
                        review = {}
                        fields = ["title", "name", "date", "feedback"]
                        n = 0
                        for line in f:
                                review[fields[n]] = line.rstrip("\n")
                                n += 1
                        print(review)
                        response = requests.post("http://34.69.203.175/feedback/", json=review)
                        print(response.status_code)
