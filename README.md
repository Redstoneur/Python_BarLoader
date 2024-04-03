# Python_BarLoader

![License](https://img.shields.io/github/license/Redstoneur/Python_BarLoader)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/Python_BarLoader)
![Build Status](https://img.shields.io/github/actions/workflow/status/Redstoneur/Python_BarLoader/build-and-publish.yml)
![Latest Release](https://img.shields.io/github/v/release/Redstoneur/Python_BarLoader)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/Python_BarLoader)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/Python_BarLoader)

Python_BarLoader is a simple package that allows you to display the loading of a process in percentage. It is designed
to be easy to use and integrate into your Python projects.

## Installation

To install Python_BarLoader, you can use pip:

```bash
pip install BarLoader
```

## Local Installation

If you want to install Python_BarLoader locally without using pip, you can follow the steps below:

1. Clone the GitHub repository on your local machine. You can do this using the following git command:
    ```bash
    git clone https://github.com/Redstoneur/Python_BarLoader.git
    ```
2. Navigate to the cloned project directory:
    ```bash
    cd Bar-Loader
    ```
3. nstall the package using the `setup.py` command:
    ```bash
    python setup.py install
    ```

This will install Python_BarLoader on your local machine. You can now use it like any other Python package.

## Usage

Here is a basic example of how to use Python_BarLoader:

```python
from time import sleep
from Bar_Loader import BarLoader, IterativeBarLoader, UniqueProcessBarLoader

def demo_bar_loader():
    """
    Demonstrate the usage of BarLoader
    """
    # Create a BarLoader object with a total of 100
    bar = BarLoader(total=100, task_name="Loading", enable_value=True)
    
    # Start the BarLoader
    bar.start()
    
    # Simulate a process by sleeping for 0.1 seconds and incrementing the BarLoader
    for i in range(100):
        sleep(0.1)
        bar.next()
    
    # End the BarLoader
    bar.end()

def demo_iterative_bar_loader():
    """
    Demonstrate the usage of IterativeBarLoader
    """
    # Create an IterativeBarLoader object with a total of 100
    iterative_bar = IterativeBarLoader(total=100, task_name="Iterative Loading")
    
    # Start the IterativeBarLoader
    iterative_bar.start()
    
    # Simulate a process by sleeping for 0.1 seconds and incrementing the IterativeBarLoader
    for i in range(100):
        sleep(0.1)
        iterative_bar.next()
    
    # End the IterativeBarLoader
    iterative_bar.end()

def demo_unique_process_bar_loader():
    """
    Demonstrate the usage of UniqueProcessBarLoader
    """
    # Create a UniqueProcessBarLoader object with a total of 100
    unique_bar = UniqueProcessBarLoader(total=100, task_name="Unique Process Loading")
    
    # Start the UniqueProcessBarLoader
    unique_bar.start()
    
    # Simulate a long process by sleeping for 3 seconds
    sleep(3)
    
    # End the UniqueProcessBarLoader
    unique_bar.end()

def main():
    """
    Main function
    """
    # Demonstrate the usage of BarLoader
    demo_bar_loader()
    
    # Demonstrate the usage of IterativeBarLoader
    demo_iterative_bar_loader()
    
    # Demonstrate the usage of UniqueProcessBarLoader
    demo_unique_process_bar_loader()

if __name__ == "__main__":
    main()
```

In this example, we create a BarLoader object with a total of 100. We start the timer, then we process 100 lines (
simulated by a sleep), calling `bar.next()` after each line. Finally, we end the timer with `bar.end()`.

## License

Python_BarLoader is under the MIT license. For more information, please refer to the `LICENSE` file.