import os
import matplotlib
matplotlib.rc('font', family = 'NanumGothic')
# matplotlib.use('tkAgg')
import matplotlib.pyplot as plt

from data_manager import asset_name_dict

savefig_dir = ''

def init_visualizer():

    # 결과 그래프 저장할 폴더 지정
    save_dir = 'result_plot'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    i = 1
    while True:
        new_dir_name = '{:02}'.format(i)
        if new_dir_name not in os.listdir(save_dir):
            break
        i += 1

    global savefig_dir
    savefig_dir = os.path.join(save_dir, new_dir_name)
    os.mkdir(savefig_dir)  # e.g. ./result_plot/01

def plot_dfs(dfs: list, df_title: list):

    for fig_idx, (df, title) in enumerate(zip(dfs, df_title)):
        asset_code_list = df.columns.levels[0]
        plt.figure(fig_idx)
        plt.figtext(0.5, 0.93, title, size=16, ha='center')

        plt.subplot(1,2,1)
        plt.grid()
        plt.xticks(rotation=50)
        for i, asset_code in enumerate(asset_code_list):
            asset_df = df[asset_code]
            if i == 7:
                plt.subplot(1, 2, 2)
                plt.grid()
                plt.xticks(rotation=50)

            plt.plot(asset_df.index, asset_df['close']/asset_df['close'].iloc[0],
                     label=str(i)+asset_name_dict[asset_code])
            plt.legend()


    plt.show()

def plot_pv(episode, test_pv, mkt):

    fig = plt.figure()
    plt.title("{} episode portfolio value".format(episode))
    plt.plot(mkt, label='market return')
    plt.plot(test_pv, label='test pv')
    plt.legend()
    # e.g. ./result_plot/01/step01.png
    plt.savefig(os.path.join(savefig_dir, 'episode_pv{:02}.png'.format(episode)))
    plt.close(fig)

def plot_ensemble_pv(agents_pv, ensemble_pv, mkt):

    fig = plt.figure()
    plt.title("Ensemble of top {} agents".format(len(agents_pv)))
    plt.plot(mkt, label='market return')
    plt.plot(ensemble_pv, label='Ensemble pv')
    for i, agent_pv in enumerate(agents_pv):
        plt.plot(agent_pv, label='agent {}'.format(i))
    plt.legend()

    plt.savefig(os.path.join(savefig_dir, 'ensemble_pv.png'))
    plt.close(fig)

def plot_reward(episode, train_reward, val_reward, test_reward):
    fig = plt.figure()
    plt.title("{} episode reward".format(episode))
    plt.plot(train_reward, label='train')
    plt.plot(val_reward, label='validation')
    plt.plot(test_reward, label='test')
    plt.legend()

    # e.g. ./result_plot/01/step01.png
    plt.savefig(os.path.join(savefig_dir, 'episode_reward{:02}.png'.format(episode)))
    plt.close(fig)