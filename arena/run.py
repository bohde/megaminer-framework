#!/usr/bin/env python
import sys
import os
import random
import subprocess

from itertools import count

COMPETITORS = 2

def main(path):
    for i in count(0):
        competitors = random.sample([direct for direct in os.listdir(path) if os.path.isdir(direct) and
             "run_client.sh" in os.listdir(direct)], COMPETITORS)
        procs = [subprocess.Popen([os.path.join(path, c)] + sys.argv[2:] + [i]) for c in competitors]
        for proc in procs:
            proc.wait()
        
if __name__ == "__main__":
    main(sys.argv[1])

        
