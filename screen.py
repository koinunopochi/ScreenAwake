import ctypes

# WindowsのAPIを呼び出すための定数
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_CONTINUOUS_DISPLAY_REQUIRED = 0x80000002
# スリープとスクリーンセーバーを防止する関数
def disable_sleep_and_screensaver():
  ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_CONTINUOUS_DISPLAY_REQUIRED)

def enable_screensaver():
  ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)