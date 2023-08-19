import matplotlib.pyplot as plt

__all__ = ['plot_loss_acc']


def plot_loss_acc(loss_list, acc_list, model_name, dpi=300):
    fig = plt.figure(dpi=dpi)
    ax = fig.add_subplot(111)
    ax.set_xlabel('epoch')
    ax.set_ylabel('loss')
    ax2 = ax.twinx()
    ax2.set_ylabel('acc')
    l1, = ax.plot(loss_list, ls='--', color='red', lw=1, label='loss')
    l2, = ax2.plot(acc_list, ls='--', color='lightgreen', lw=1, label='acc')
    ax.set_title(model_name)
    plt.legend(handles=[l1, l2])
    plt.show()


if __name__ == '__main__':
    import numpy as np

    plot_loss_acc(np.linspace(0, 1, 50), np.linspace(0.5, 1, 70), 'Transformer')
