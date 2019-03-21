from Lib.DbUtil import DbUtil


class MainTest(object):

    def __init__(self):
        self.dbUtil = DbUtil();


    def getList(self):

        sql = "select * from abitree.tbl_test order by idx desc";
        data = self.dbUtil.exeQuery(sql);


        return data;

    def putData(self, txt):
        sql = "insert into abitree.tbl_test set txt = %s";
        self.dbUtil.exeQuery(sql, (txt));

    def setData(self, txt, idx):
        sql = "update abitree.tbl_test set txt = %s where idx = %s";
        self.dbUtil.exeQuery(sql, (txt, idx));

