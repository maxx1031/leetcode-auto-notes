#!/usr/bin/env python3
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from main_script import generate_notes

class SolutionFileHandler(FileSystemEventHandler):
    def __init__(self, output_dir="notes"):
        self.output_dir = output_dir
        self.processed_files = set()
    
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return
        
        if event.src_path in self.processed_files:
            return
        
        file_path = Path(event.src_path)
        problem_slug = file_path.stem.replace('_', '-')
        
        print(f"\n检测到文件变更: {file_path}")
        print(f"自动生成笔记: {problem_slug}")
        
        try:
            if generate_notes(problem_slug, str(file_path), self.output_dir):
                self.processed_files.add(event.src_path)
                print(f"✅ 自动生成完成")
            else:
                print(f"❌ 自动生成失败")
        except Exception as e:
            print(f"❌ 自动生成时出错: {e}")

def main():
    event_handler = SolutionFileHandler()
    observer = Observer()
    observer.schedule(event_handler, "solutions", recursive=False)
    
    observer.start()
    print("🔍 开始监控 solutions/ 目录...")
    print("保存Python文件时将自动生成笔记")
    print("按 Ctrl+C 停止监控")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n👋 监控已停止")
    
    observer.join()

if __name__ == "__main__":
    main()