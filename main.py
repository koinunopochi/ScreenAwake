from move_mouse import move_mouse
import pynput.keyboard
import screen
from timeUtils import now_time
import argparse

def main(use_move_mouse=True):
  keyboard_listener = pynput.keyboard.Listener(on_press=lambda key: False)
  
  # キーボードリスナーが動作している間、マウスカーソルを移動し続ける
  keyboard_listener.start()
  while keyboard_listener.running:
    if use_move_mouse:
      move_mouse()
  keyboard_listener.stop()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="マウスを動かすかどうかを設定するスクリプト")
  parser.add_argument("--move-mouse", action="store_true", help="マウスを動かすかどうか")
  args = parser.parse_args()

  print(now_time(), "Start")
  try:
    screen.disable_sleep_and_screensaver()
    main(use_move_mouse=args.move_mouse)
  finally:
    screen.enable_screensaver()
  print(now_time(), "End")