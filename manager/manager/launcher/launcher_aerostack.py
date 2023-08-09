import os
import subprocess
from src.manager.manager.launcher.launcher_interface import ILauncher, LauncherException
from src.manager.manager.docker_thread.docker_thread import DockerThread
from typing import List, Any
import psutil
import threading

class LauncherAerostack(ILauncher):
    exercise_id: str
    type: str
    module: str
    parameters: List[str]
    launch_file: str
    process: Any = None
    thread: Any = None

    def run(self, callback: callable = None):
        self.launch_file = os.path.expandvars(self.launch_file)

        # Start the process in a separate thread
        self.thread = DockerThread(f'ros2 launch {self.launch_file}')
        self.thread.start()

    def is_running(self):
        return True

    def terminate(self):
        self.thread.terminate()
        self.thread.join()
        self.running = False

    def died(self):
        pass
