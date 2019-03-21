from django.views import View

from Lib.Common import Common
from Model.MainTest import MainTest

import json


class MainView(View):



    def __init__(request):
        # print("TestView __init__ ");
        pass;


    def get(self, request):
        print("get");

        mainTest = MainTest();

        resResult = True
        resMessage = "";
        # resData = None;

        resData = mainTest.getList();

        return Common.response(self, result=resResult, message=resMessage, data=resData);
        # return None;






    def post(self, request):
        print("post");

        reqBody = request.body;
        dataJson = ((reqBody).decode('utf-8'));
        dataObj = json.loads(dataJson);

        txtText = dataObj.get("txt");

        mainTest = MainTest();
        mainTest.putData(txtText);

        resResult = True
        resMessage = "";

        resData = mainTest.getList();

        return Common.response(self, result=resResult, message=resMessage, data=resData);


    def put(self, request, idx):
        print("put");

        reqBody = request.body;
        dataJson = ((reqBody).decode('utf-8'));
        dataObj = json.loads(dataJson);

        txtText = dataObj.get("txt");
        strIdx = str(idx);


        print(txtText);
        print(idx);


        mainTest = MainTest();
        mainTest.setData(txtText, idx);

        resResult = True
        resMessage = "";

        resData = mainTest.getList();

        return Common.response(self, result=resResult, message=resMessage, data=resData);