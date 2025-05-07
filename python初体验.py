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
        "过去的每一步，都是未来奇迹的种子。"
    ],
    "2": [
        "未来的你，正在某个地方微笑着等你。",
        "别着急，每一个慢慢走的夜晚都很有力量。",
        "未来也许不完美，但一定值得你走下去。"
    ],
    "3": [
        "黑夜里总有人为你点一盏灯。",
        "世界很大，但你的光也很远。",
        "走累了，就在这里歇歇吧。明天又是新的冒险。"
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
