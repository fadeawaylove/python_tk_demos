import requests
from tkinter import *


def youdao(words):
    # 构建url
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # 构建请求头
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0'
    }

    # 构建请求体
    format_data = {
        'i': words,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1526368137702',
        'sign': 'f0cd13ef1919531ec9a66516ceb261a5',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'true'
    }

    # 打开请求文件
    response = requests.post(url, headers=headers, data=format_data)

    # 读取文件内容
    content = response.json()
    print(content)
    ret = content["translateResult"][0][0]['tgt']

    return ret


# 主程序
root = Tk()
# 设置标题
root.title("呆瓜词典")
# 设置主窗口大小
root.geometry("320x150")
# 可变大小
root.resizable(width=False, height=True)

# 第一排输入框 输入查询的内容
# 左边是一个标签
l1 = Label(root, text='查询内容', bg="yellow", font=(12), height=1, width=8)
l1.place(x=20, y=20)
var1 = StringVar()
input_text = Entry(root, textvariable=var1)
input_text.place(x=100, y=20)

# 第二排显示框 显示查询的结果
# 左边是一个标签
l2 = Label(root, text='查询结果', bg="yellow", font=(12), height=1, width=8)
l2.place(x=20, y=60)
var2 = StringVar()
output_text = Entry(root, textvariable=var2)
output_text.place(x=100, y=60)


# 调用youdao函数，传进要翻译的内容
def func():
    words = var1.get()
    if words:
        # print(words)
        result = youdao(words)
        var2.set(result)

    # 添加一个按钮


b = Button(root, text="查询", command=func)
b.place(x=170, y=100)

# 运行主程序
root.mainloop()
