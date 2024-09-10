# Real time example
from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def read_from_excel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass


class TC1(Browser):
    def start_browser(self):
        print("Starting the Browser")

    def stop_browser(self):
        print("Stopping the Browser")

    def read_from_excel(self):
        print("Read TC from excel")

    def run_test_case1(self):
        self.start_browser()
        self.read_from_excel()
        self.stop_browser()


tc1 = TC1()
tc1.run_test_case1()
