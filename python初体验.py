import random
import time
import os
import pygame

# 初始化pygame
pygame.mixer.init()

# 定义你的音乐文件路径
music_directory = r"C:\Users\lenovo\Music\VipSongsDownload"  # 你的音乐目录
background_music_files = [
    "怪就怪天气.mp3",  # 这里是你下载的音乐文件名
    "会魔法的老人.mp3"
]


def play_random_music():
    music = random.choice(background_music_files)  # 随机选择一个音乐文件
    music_path = f"{music_directory}\\{music}"  # 构建完整的音乐文件路径

    print(f"\n🎶 酒馆背景音乐：{music_path}")

    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
    else:
        print(f"⚡ 找不到音乐文件：{music_path}")


def create_log_file():
    """检查是否有日志文件，如果没有则创建"""
    if not os.path.exists("酒馆日志.txt"):
        with open("酒馆日志.txt", "w", encoding="utf-8") as f:
            f.write("【虚拟酒馆日志】\n\n")
# 调用函数，确保日志文件已准备好
create_log_file()
# 然后是你原本的程序逻辑……
play_random_music()
# 欢迎进入虚拟酒馆
print("\n🍷 欢迎来到【虚拟酒馆】\n今天，和谁聊聊呢？\n")

# 定义角色
dialogue_targets = {
    "1": "过去的自己",
    "2": "未来的自己",
    "3": "虚拟朋友：灯塔"
}

# 随机回应句子库
responses = {
    "1": [
        "记得那个夜晚你也这样迷茫，但你熬过来了。",
        "别忘了，你曾经为自己许下的那些小小的愿望。",
        "过去的每一步，都是未来奇迹的种子。",
        "那些看似不起波澜的日复一日，会在某天让你看到坚持的意义。",
        "你已经从所有你认为不会过去的事情中幸存下来了。",
        "过去的你，现在已经是你自己的一部分。",
        "你已经拥有了过去的回忆，并且在未来的日子里，你会继续努力地向前。",
        "回头看，轻舟已过万重山。",
    ],
    "2": [
        "未来的你，正在某个地方微笑着等你。",
        "别着急，每一个慢慢走的夜晚都很有力量。",
        "未来也许不完美，但一定值得你走下去。",
        "生活就像骑自行车，为了保持平衡，你必须继续前进。",
        "未来的你，正在等待那个让你满意的时刻。",
        "别让过去的你成为你的包袱，让未来的你成为你的垫脚石。",
        "今天很残酷，明天更残酷，后天很美好，但绝大多数人死在明天晚上。",
        "你未来的样子，藏在你现在的努力里。",
        "世界上只有一种真正的英雄主义，那就是认清生活的真相后依然热爱生活。",
    ],
    "3": [
        "黑夜里总有人为你点一盏灯。",
        "世界很大，但你的光也很远。",
        "走累了，就在这里歇歇吧。明天又是新的冒险。",
        "你并不孤单，世界上有无数人和你一样在努力着。",
        "生活不会辜负每一个认真努力的人。",
        "你是这个世界的一部分，不要被生活的压力所打败。",
        "当你觉得为时已晚的时候，恰恰是最早的时候。",
        "不是看到了希望才坚持，而是坚持了才看到希望。",
        "所有光芒，都需要时间才能被看到。",
        "黑夜无论怎样悠长，白昼总会到来。",
        "生活就像一场盛大的音乐会，每个人都有自己的声音。",
    ]
}

while True:
    print("选择一个聊天对象：")
    for key, value in dialogue_targets.items():
        print(f"  {key}. {value}")
    print("  q. 离开酒馆")

    choice = input("\n输入你的选择 (1/2/3/q): ").strip()

    if choice == 'q':
        print("\n🌙 酒馆的灯慢慢熄灭了，期待你下次再来。晚安。\n")
        break
    elif choice in dialogue_targets:
        user_input = input(f"\n📝 对{dialogue_targets[choice]}说点什么吧：\n").strip()
        print("\n🍷 倾听中...")
        time.sleep(1.5)

        # 先选出随机回复，并保存到变量
        random_response = random.choice(responses[choice])

        print(f"\n{dialogue_targets[choice]} 回复你：")
        print(f"✨ {random_response}\n")

        # 保存对话到日志
        with open("酒馆日志.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"你对{dialogue_targets[choice]}说：{user_input}\n")
            log_file.write(f"{dialogue_targets[choice]} 回复你：{random_response}\n")
            log_file.write("-" * 40 + "\n")

    else:
        print("\n⚡ 输入错误，请重新选择。\n")
