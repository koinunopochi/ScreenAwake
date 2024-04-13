import pyautogui
import random
import time

# フェイルセーフ機能を無効にする
pyautogui.FAILSAFE = False
def move_mouse():
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