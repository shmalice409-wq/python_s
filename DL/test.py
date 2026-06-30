import torch
from torch import nn
from torchvision import transforms
import torchvision
from torch.utils import data
import matplotlib.pyplot as plt
import numpy as np

# ========== 辅助类和函数 ==========

class Accumulator:
    """在n个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def accuracy(y_hat, y):
    """计算预测准确率"""
    if len(y_hat.shape) > 1 and y_hat.size(1) > 1:
        y_hat = y_hat.argmax(dim=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


def evaluate_accuracy(net, data_iter):
    """评估模型准确率"""
    if isinstance(net, nn.Module):
        net.eval()
    metric = Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]


def train_epoch_ch3(net, train_iter, loss, updater):
    """训练模型一个迭代周期"""
    if isinstance(net, torch.nn.Module):
        net.train()
    metric = Accumulator(3)
    for X, y in train_iter:
        y_hat = net(X)
        l = loss(y_hat, y)
        
        # 修正拼写：Optimizer
        if isinstance(updater, torch.optim.Optimizer):
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    return metric[0] / metric[2], metric[1] / metric[2]


def train_ch3_terminal(net, train_iter, test_iter, loss, num_epochs, updater, 
                       save_path='training_results.png', show_plot=True):
    """
    训练模型 - 终端版本，使用matplotlib显示
    
    Args:
        net: 神经网络模型
        train_iter: 训练数据迭代器
        test_iter: 测试数据迭代器
        loss: 损失函数
        num_epochs: 训练轮数
        updater: 优化器
        save_path: 图片保存路径
        show_plot: 是否显示图片（在GUI环境中）
    """
    # 记录训练历史
    train_losses = []
    train_accs = []
    test_accs = []
    
    print("="*60)
    print(f"{'Epoch':<8}{'Train Loss':<15}{'Train Acc':<15}{'Test Acc':<15}")
    print("="*60)
    
    for epoch in range(num_epochs):
        # 训练一个epoch
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        train_loss = train_metrics[0]
        train_acc = train_metrics[1]
        
        # 评估测试集
        test_acc = evaluate_accuracy(net, test_iter)
        
        # 记录历史
        train_losses.append(train_loss)
        train_accs.append(train_acc)
        test_accs.append(test_acc)
        
        # 在终端实时打印
        print(f"{epoch+1:<8}{train_loss:<15.4f}{train_acc:<15.4f}{test_acc:<15.4f}")
    
    print("="*60)
    print("训练完成！")
    
    # 绘制训练曲线
    epochs = range(1, num_epochs + 1)
    
    # 创建图形，设置大小
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 左图：训练损失
    axes[0].plot(epochs, train_losses, 'b-', linewidth=2, label='Train Loss')
    axes[0].set_xlabel('Epoch', fontsize=12)
    axes[0].set_ylabel('Loss', fontsize=12)
    axes[0].set_title('Training Loss', fontsize=14, fontweight='bold')
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)
    
    # 添加数值标注
    for i, loss_val in enumerate(train_losses):
        if i % max(1, num_epochs//5) == 0:  # 每几个epoch标注一次
            axes[0].annotate(f'{loss_val:.3f}', 
                           (epochs[i], loss_val),
                           textcoords="offset points",
                           xytext=(0,10), 
                           ha='center',
                           fontsize=8)
    
    # 右图：准确率
    axes[1].plot(epochs, train_accs, 'g-', linewidth=2, label='Train Acc')
    axes[1].plot(epochs, test_accs, 'r-', linewidth=2, label='Test Acc')
    axes[1].set_xlabel('Epoch', fontsize=12)
    axes[1].set_ylabel('Accuracy', fontsize=12)
    axes[1].set_title('Model Accuracy', fontsize=14, fontweight='bold')
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)
    
    # 添加最终准确率标注
    axes[1].annotate(f'Final Train: {train_accs[-1]:.4f}', 
                   (epochs[-1], train_accs[-1]),
                   textcoords="offset points",
                   xytext=(-10,-15), 
                   ha='center',
                   fontsize=9,
                   color='green')
    axes[1].annotate(f'Final Test: {test_accs[-1]:.4f}', 
                   (epochs[-1], test_accs[-1]),
                   textcoords="offset points",
                   xytext=(-10,10), 
                   ha='center',
                   fontsize=9,
                   color='red')
    
    plt.tight_layout()
    
    # 保存图片
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"\n训练曲线已保存为: {save_path}")
    
    # 显示图片（如果有GUI环境）
    if show_plot:
        try:
            plt.show()
        except:
            print("无法显示图形界面，请查看保存的图片文件。")
    
    return train_losses, train_accs, test_accs


def load_data_fashion_mnist(batch_size, resize=None):
    """下载并加载Fashion-MNIST数据集"""
    trans = transforms.ToTensor()
    if resize:
        trans.insert(0, transforms.Resize(resize))
    
    mnist_train = torchvision.datasets.FashionMNIST(
        root='data', 
        train=True, 
        transform=trans, 
        download=True
    )
    mnist_test = torchvision.datasets.FashionMNIST(
        root='data', 
        train=False, 
        transform=trans, 
        download=True
    )
    
    train_iter = data.DataLoader(
        mnist_train, 
        batch_size, 
        shuffle=True, 
        num_workers=0  # 在Windows下建议设为0，避免多进程问题
    )
    test_iter = data.DataLoader(
        mnist_test, 
        batch_size, 
        shuffle=False, 
        num_workers=0
    )
    
    return train_iter, test_iter


# ========== 主程序 ==========

if __name__ == "__main__":
    # 设置设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"使用设备: {device}")
    
    # 构建网络
    net = nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Linear(256, 10)
    )
    
    # 初始化权重
    def init_weight(m):
        if type(m) == nn.Linear:
            nn.init.normal_(m.weight, std=0.01)
    
    net.apply(init_weight)
    net = net.to(device)
    
    # 超参数设置
    num_epochs = 10
    lr = 0.1
    batch_size = 256
    
    # 损失函数和优化器
    loss = nn.CrossEntropyLoss(reduction='none')
    trainer = torch.optim.SGD(net.parameters(), lr=lr)
    
    # 加载数据
    print("正在加载Fashion-MNIST数据集...")
    train_iter, test_iter = load_data_fashion_mnist(batch_size)
    print("数据加载完成！\n")
    
    # 训练模型
    print("开始训练...")
    train_losses, train_accs, test_accs = train_ch3_terminal(
        net, 
        train_iter, 
        test_iter, 
        loss, 
        num_epochs, 
        trainer,
        save_path='fashion_mnist_training_results.png',
        show_plot=True  # 如果你在GUI环境中运行，设为True；纯终端环境设为False
    )
    
    # 打印最终结果
    print(f"\n最终结果:")
    print(f"  训练损失: {train_losses[-1]:.4f}")
    print(f"  训练准确率: {train_accs[-1]:.4f}")
    print(f"  测试准确率: {test_accs[-1]:.4f}")