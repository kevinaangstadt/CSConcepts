#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
lines = list(map(lambda a: a.rstrip("\r\n"), lines))


nodes = list(set(lines))

adj = dict((a, []) for a in range(len(nodes)))

for i in range(int(len(lines)/2)):
  adj[nodes.index(lines[i*2])].append(nodes.index(lines[i*2+1]))
  
print(len(nodes))

for src, dst_list in adj.items():
  # remove duplicates
  dst_list = list(set(dst_list))
  
  print("{0} {1}".format(str(src), " ".join(str(i) for i in dst_list)))