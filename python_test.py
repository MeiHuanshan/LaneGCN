from tqdm import tqdm
lt=range(100)
for i,item in enumerate(tqdm(lt)):
    print(i, item)
    if i > 10:
        exit()
import torch
import numpy as np

num_nodes = 7
lane_idcs = torch.from_numpy(np.array(range(num_nodes)))
hi = torch.arange(num_nodes).long().view(-1, 1).repeat(1, num_nodes).view(-1)
wi = torch.arange(num_nodes).long().view(1, -1).repeat(num_nodes, 1).view(-1)
row_idcs = torch.arange(num_nodes).long()


pre = [ [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]]

suc = [ [0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

left =[ [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]]

rigt =[ [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

pre = np.array(pre)
suc = np.array(suc)
left = np.array(left)
rigt = np.array(rigt)

x = np.matmul(left, pre) + np.matmul(left, suc) + left
print(lane_idcs[hi])
print(lane_idcs[wi])
mask = left[lane_idcs[hi], lane_idcs[wi]]
print(mask)
