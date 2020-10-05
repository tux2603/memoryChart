#!/usr/bin/env python
import plotly.graph_objects as go
import subprocess

if __name__ == '__main__':
    psData = subprocess.run(['ps', '--ppid', '2', '-p', '2', '--deselect', '-o', 'pid,ppid,rss,comm', '--no-headers'], capture_output=True).stdout.decode('utf-8')
    
    # First, read through the dictionary and a make a tree
    pids = []
    processNames = []
    parentPIDs = []
    processMemUsages = []

    for line in psData.splitlines():
        words = line.split()

        pids.append(words[0])
        parentPIDs.append(words[1] if words[1] != '0' else '')
        processMemUsages.append(int(words[2]))
        processNames.append(' '.join(words[3:]))

    print(pids)
    print(parentPIDs)
    print(processMemUsages)
    print(processNames)

    fig = go.Figure(go.Sunburst(ids=pids, labels=processNames,values=processMemUsages, parents=parentPIDs,))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    fig.show()