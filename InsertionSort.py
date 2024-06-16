import numpy as np
from random import randrange
from PlanePlot import plot

samples = 100
ran = 10**3

def insSortRec(seq, i=None):
    if i == None: i = len(seq) - 1
    if i == 0: return
    insSortRec(seq, i-1)
    j=i
    while j>0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


seq = np.array([randrange(ran) for i in range(samples)])
newseq = np.array([i for i in seq])
dom = np.array([i for i in range(samples)])

insSortRec(newseq)

plot(dom, seq, newseq)
