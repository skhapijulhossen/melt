# from textual.app import App, ComposeResult
# from textual.widgets import DirectoryTree


# ### visualizer
# class DirectoryTreeApp(App):
#     def compose(self) -> ComposeResult:
#         yield DirectoryTree("./")


# if __name__ == "__main__":
#     app = DirectoryTreeApp()
#     app.run()

import os
import shelve
import yaml
import shutil


assets = {
    'ml': {
        'assets_path': 4
    }
}


def get_current_module_path():
    return os.path.abspath(__file__)


def get_assets(args):
    melt_type = args.type
    melt_problem = args.problem

    # Your code logic based on the parsed arguments goes here
    pwd = get_current_module_path()[:-10]
    return os.path.join(pwd, 'assets', melt_type, melt_problem)


# Function to read YAML file
def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Function to write data to a YAML file
def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


# to copy templates from assets
def copy_file(source_path, destination_path):
    try:

        shutil.copy(source_path, destination_path)
        print(
            f"File copied successfully from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Check if you have the necessary permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")
