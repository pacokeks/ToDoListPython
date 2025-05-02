import os

class TodoModel:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.__tasks = []
        
    def loadTasks (self):
        if os.path.exists(self.filePath): # gleichbedeutend mit "./tasks.txt"
            lines = []
            with open(self.filePath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line. strip()
                    if line:
                        self.__tasks.append(line)
                print(f"Tasks loaded.")
    
    def saveTasks(self, tasks: list[str]):
        with open(self.filePath, "w", encoding="utf-8") as file:
            for i in range(tasks.count()):
                file.write(tasks[i] + "\n")
        print(f"Tasks saved.")

    def getTasks(self) -> list[str]:
        return self.__tasks