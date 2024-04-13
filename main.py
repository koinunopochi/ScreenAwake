import random
import time
import pynput.mouse
import pynput.keyboard
import tkinter as tk
import ctypes

# スリープを防止するためのWindows APIの定数
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

# スリープを防止する関数
# def prevent_sleep():
#     ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState2(ES_CONTINUOUS | ES_SYSTEM_REQUIRED, 0, 0)
# マウスコントローラーの初期化
mouse = pynput.mouse.Controller()

# キーボードリスナーの初期化
keyboard_listener = pynput.keyboard.Listener(on_press=lambda key: False)

# マウスを動かす関数
def move_mouse():
    while keyboard_listener.running:
        # 画面のサイズを取得
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()

        # ランダムな座標を生成
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # マウスカーソルを移動
        mouse.position = (x, y)

        # ランダムな時間待機
        sleep_time = random.uniform(0.1, 1.0)
        time.sleep(sleep_time)

        # スリープを防止
        # prevent_sleep()

# スリープを防止
prevent_sleep()
# キーボードリスナーを開始
keyboard_listener.start()

# マウスを動かす
move_mouse()

# キーボードリスナーを停止
keyboard_listener.stop()

# スリープ防止を解除
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)