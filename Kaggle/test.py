import sys
import pandas as pd
import torch

print("Python解释器：", sys.executable)
print("Pandas版本：", pd.__version__)
print("PyTorch版本：", torch.__version__)
print("CUDA是否可用：", torch.cuda.is_available())