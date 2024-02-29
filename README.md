# Python_BarLoader

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
from Bar_Loader import BarLoader
from time import sleep

# Create a BarLoader object
bar = BarLoader(total=100, task_name="Loading", enable_value=True)

# Start the timer
bar.start()

# Increment the number of processed lines
for i in range(100):
    sleep(0.1)
    bar.next()

# End the timer
bar.end()
```

In this example, we create a BarLoader object with a total of 100. We start the timer, then we process 100 lines (
simulated by a sleep), calling `bar.next()` after each line. Finally, we end the timer with `bar.end()`.

## License

Python_BarLoader is under the MIT license. For more information, please refer to the `LICENSE` file.