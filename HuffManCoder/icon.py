import win32com.client
import os

def create_shortcut(target_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.IconLocation = target_path
    shortcut.Save()

if __name__ == '__main__':
    target_path = os.path.abspath('dist/file_processor.exe')
    shortcut_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'File Processor.lnk')

    create_shortcut(target_path, shortcut_path)
