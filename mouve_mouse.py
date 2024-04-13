import pyautogui
import random
import time
import pynput.keyboard

import ctypes

# スクリーンセーバーを無効にする
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

keyboard_listener = pynput.keyboard.Listener(on_press=lambda key: False)

def move_mouse():
    while keyboard_listener.running:
        # 画面のサイズを取得
        screen_width, screen_height = pyautogui.size()

        # ランダムな座標を生成
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # マウスカーソルを移動
        pyautogui.moveTo(x, y)

        # ランダムな時間待機
        sleep_time = random.uniform(0.1, 1.0)
        time.sleep(sleep_time)

def now_time():
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))

# ja時間で表示
print("start_time:", now_time())

# キーボードリスナーを開始
keyboard_listener.start()
move_mouse()
keyboard_listener.stop()
# 終了時刻を表示 
print("end_time:", now_time())