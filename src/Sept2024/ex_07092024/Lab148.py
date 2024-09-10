# static to non-static ---> Directly accessible [create obj]

class READEXCELFILE:

    def read_my_excel_file(self):
        print("Reading Excel files")


class MYSQLDBCONNECTION:
    def read_my_sql_file(self):
        print("Reading MySQL")


class TC1:
    @staticmethod
    def run_tc1():
        MYSQLDBCONNECTION().read_my_sql_file()
        READEXCELFILE().read_my_excel_file()
        # or


TC1.run_tc1()
