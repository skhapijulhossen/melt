from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree
import os

# ### visualizer
# class DirectoryTreeApp(App):
#     def compose(self) -> ComposeResult:
#         yield DirectoryTree("./")


# if __name__ == "__main__":
#     app = DirectoryTreeApp()
#     app.run()

# print(os.path.abspath(os.path.dirname(__file__)))
###
class Melty:
    """
    Class to wrap all functionalities.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def flash(name: str = "melt", project_dir: str = ".") -> str:
        if project_dir == ".":
            path = os.getcwd()
            os.mkdir(os.path.join(path, '.meltconfigure'))






        
        
