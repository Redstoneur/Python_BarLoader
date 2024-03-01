from time import time


class BarLoader:
    """
    Class that contains the function to display the loading of a process in percentage
    """

    # Variable that contains the bar
    start_time = time()
    task_name = ""
    nb: int = 0
    total: int
    full_time = True
    enable_value = False
    debug_mode = False

    def __init__(
            self, total: int,
            task_name: str = "",
            full_time: bool = True,
            enable_value: bool = False,
            debug_mode: bool = False
    ) -> None:
        """
        Constructor
        :param total: the total number of lines
        :param task_name: the name of the task (Default : "")
        :param full_time: if we should display all time information (Default : True)
        :param enable_value: if we should display the value (Default : False)
        :param debug_mode: the debug mode (Default : False)
        """
        self.total = total
        self.task_name = task_name
        self.full_time = full_time
        self.enable_value = enable_value
        self.debug_mode = debug_mode

    def start(self) -> None:
        """
        Function that starts the timer
        :return: None
        """
        self.start_time = time()
        self.nb = 0
        self._display_loading(
            nb=self.nb, total=self.total, task_name=self.task_name,
        )

    def next(self) -> None:
        """
        Function that increments the number of lines processed
        :return: None
        """
        self.nb += 1
        self._display_loading(
            nb=self.nb, total=self.total,
            task_name=self.task_name,
            elapsed_time=time() - self.start_time,
            full_time=self.full_time, enable_value=self.enable_value,
            debug_mode=self.debug_mode
        )

    def end(self, force: bool = False) -> None:
        """
        Function that ends the timer
        :param force: if we should force the end (Default : False)
        :return: None
        """
        if force:
            self.nb = self.total
        self._display_loading(
            nb=self.nb, total=self.total,
            task_name=self.task_name,
            elapsed_time=time() - self.start_time,
            final=True, full_time=self.full_time,
            enable_value=self.enable_value, debug_mode=self.debug_mode
        )

    @staticmethod
    def _display_loading(
            nb: int, total: int,
            task_name: str = "", elapsed_time: float = None,
            final: bool = False, full_time: bool = True,
            enable_value: bool = False, debug_mode: bool = False
    ) -> None:
        """
        Function that displays the loading of a process in percentage
        :param nb: the number of lines processed
        :param total: the total number of lines
        :param task_name: the name of the task (Default : "")
        :param elapsed_time: elapsed time (Default : None)
        :param final: if it's the last line (Default : False)
        :param full_time: if we should display all time information (Default : True)
        :param enable_value: if we should display the value (Default : False)
        :param debug_mode: the debug mode (Default : False)
        :return: None
        """
        progress_per_data = 100 / total

        def format_time(separator: str = " ") -> str:
            if elapsed_time is None:
                return ""
            if elapsed_time < 0:
                raise ValueError("elapsed_time must be positive")
            rate = (total if final else nb) / elapsed_time if elapsed_time != 0 else 0
            if final:
                return (separator + (
                    f"[{elapsed_time:.6f} seconds - ({rate:.6f}/s)]" + " " * 10 if enable_value
                    else f"[{elapsed_time:.6f} seconds]" + " " * 20
                ) + " " * 10)
            if enable_value:
                if full_time and elapsed_time != 0:
                    remaining_time = (total - nb) / rate
                    return (
                            separator +
                            f"[{elapsed_time:.6f}s < {remaining_time:.6f}s remaining - ({rate:.6f}/s)]"
                            + " " * 10
                    )
                return separator + f"({rate:.6f}/s)" + " " * 10
            if elapsed_time != 0:
                remaining_time = (total - nb) / rate
                return separator + f"[{elapsed_time:.6f}s < {remaining_time:.6f}s remaining]" + " " * 10
            return ""

        display_values = (f" {nb}/{total}" if enable_value else "") + format_time()
        end = "\n" if debug_mode else "\r"

        if task_name != "":
            task_name = "{@} ".replace("@", task_name)

        if nb == total:
            (
                print(task_name + "|" + "=" * 99 + ">>" + "| 100%" + display_values) if final
                else print(task_name + "|" + "=" * 100 + ">" + "| 100%" + display_values, end=end)
            )
        else:
            print(
                task_name +
                "|" + "=" * int(progress_per_data * nb) + ">" + " " * (100 - int(progress_per_data * nb)) +
                f"| {int(progress_per_data * nb)}%" + display_values,
                end=end
            )
        return None


class IterativeBarLoader(BarLoader):
    """
    Class that contains the function to display the loading of a process in percentage for iterative process
    """

    def __init__(
            self, total: int,
            task_name: str = "",
            full_time: bool = True,
            debug_mode: bool = False) -> None:
        """
        Constructor
        :param total: the total number of lines
        :param task_name: the name of the task (Default : "")
        :param full_time: if we should display all time information (Default : True)
        :param debug_mode: the debug mode (Default : False)
        """
        super().__init__(
            total=total, task_name=task_name,
            full_time=full_time, enable_value=True,
            debug_mode=debug_mode
        )


class UniqueProcessBarLoader(BarLoader):
    """
    Class that contains the function to display the loading of a process in percentage for unique process
    """

    def __init__(
            self, total: int,
            task_name: str = "",
            full_time: bool = True,
            debug_mode: bool = False) -> None:
        """
        Constructor
        :param total: the total number of lines
        :param task_name: the name of the task (Default : "")
        :param full_time: if we should display all time information (Default : True)
        :param debug_mode: the debug mode (Default : False)
        """
        super().__init__(
            total=total, task_name=task_name,
            full_time=full_time, enable_value=False,
            debug_mode=debug_mode
        )

    def end(self) -> None:
        """
        Function that ends the timer
        :return:
        """
        super().end(force=True)


if __name__ == "__main__":
    # Demonstration of the Bar_Loader class with the display_loading function

    # import for testing
    from time import sleep

    # Create a Bar_Loader object
    bar = BarLoader(total=100, task_name="Loading", enable_value=True)
    # Start the timer
    bar.start()
    # Increment the number of lines processed
    for i in range(100):
        sleep(0.1)
        bar.next()
    # End the timer
    bar.end()

    # Create a Bar_Loader object
    bar = BarLoader(total=100, task_name="Loading2")
    # Start the timer
    bar.start()
    # Sumulate a long process
    sleep(3)
    # End the timer
    bar.end(force=True)

    # Create a Bar_Loader object
    bar = IterativeBarLoader(total=100, task_name="Loading3")
    # Start the timer
    bar.start()
    # Increment the number of lines processed
    for i in range(100):
        sleep(0.1)
        bar.next()
    # End the timer
    bar.end()

    # Create a Bar_Loader object
    bar = UniqueProcessBarLoader(total=100, task_name="Loading4")
    # Start the timer
    bar.start()
    # Sumulate a long process
    sleep(3)
    # End the timer
    bar.end()
