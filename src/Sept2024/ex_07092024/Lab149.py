# non-static to non-static ---> Directly accessible [create obj]
class READEXCELFILE:

    def read_my_excel_file(self):
        print("Reading Excel files")


class MYSQLDBCONNECTION(READEXCELFILE):
    def read_my_sql_file(self):
        print("Reading MySQL")


class TC1(MYSQLDBCONNECTION):
    def run_tc1(self):
        # we can create objects for each class, or we can use inheritance and access members
        MYSQLDBCONNECTION().read_my_sql_file()
        READEXCELFILE().read_my_excel_file()


tc = TC1()
tc.run_tc1()
