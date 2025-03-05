import os
from tkinter import Tk, filedialog
from spleeter.separator import Separator

def separate_audio(input_audio_paths, output_dir):
    """
    分离音频中的人声和伴奏
    :param input_audio_paths: 输入音频文件路径列表
    :param output_dir: 输出目录
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    separator = Separator('spleeter:2stems')

    for input_audio_path in input_audio_paths:
        print(f"正在分离音频: {input_audio_path}，请稍候...")
        separator.separate_to_file(input_audio_path, output_dir)
        print(f"分离完成！结果已保存到目录：{output_dir}")

def select_audio_files():
    """
    弹出文件选择对话框，让用户选择多个音频文件
    :return: 用户选择的音频文件路径列表
    """
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="选择音频文件",
        filetypes=[("音频文件", "*.mp3 *.wav *.mp4"), ("所有文件", "*.*")]
    )

    return file_paths

if __name__ == "__main__":
    input_audio_paths = select_audio_files()

    if input_audio_paths:
        output_dir = "output"
        separate_audio(input_audio_paths, output_dir)
    else:
        print("未选择音频文件，程序退出。")
