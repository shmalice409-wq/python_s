import random

import torch
features=torch.tensor([1,23,4,5,6,7,8,9])   
num_examples=len(features)
indices =list(range(num_examples))
random.shuffle(indices)  # 样本的读取顺序是随机的
for i in range(0, num_examples, 4):
    batch_indices = torch.tensor(
        indices[i: min(i + 4, num_examples)])
    print(batch_indices)
    print(features[batch_indices])