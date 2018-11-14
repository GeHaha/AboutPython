# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:29:28 2018

@author: Administrator
"""

class Page:
    "电子书一页的内容"
    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getContent(self):
        return "第 " + str(self.__pageNum) + " 页的内容..."

class Catalogue:
    "目录结构"

    def __init__(self, title):
        self.__title = title
        self.__chapters = []
        self.setChapter("第一章")
        self.setChapter("第二章")

    def setChapter(self, title):
        self.__chapters.append(title)

    def showInfo(self):
        print("标题：" + self.__title)
        for chapter in self.__chapters:
            print(chapter)

class IBook:
    "电子书文档的接口类"

    def parseFile(self, filePath):
        pass

    def getCatalogue(self):
        pass

    def getPageCount(self):
        pass

    def getPage(self, pageNum):
        pass

class TxtBook(IBook):
    "TXT解析类"

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__pageCount = 500
        return True

    def getCatalogue(self):
        return Catalogue("TXT电子书")

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)

class EpubBook(IBook):
    "TXT解析类"

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        return Catalogue("Epub电子书")

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    "第三方PDF解析库的目录类"
    pass


class PdfPage:
    "PDF页"

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    "第三方PDF解析库"

    def __init__(self):
        self.__pageSize = 0

    def open(self, filePath):
        print("第三方解析PDF文件：" + filePath)
        self.__pageSize = 1000
        return True

    def getOutline(self):
        return Outline()

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)

class PdfAdapterBook(ThirdPdf, IBook):
    "TXT解析类"

    def parseFile(self, filePath):
        # 模拟文档的解析
        rtn = super().open(filePath)
        if(rtn):
            print(filePath + "文件解析成功")
        return rtn

    def getCatalogue(self):
        outline = super().getOutline()
        print("将Outline结构的目录转换成Catalogue结构的目录")
        return Catalogue("PDF电子书")

    def getPageCount(self):
        return super().pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print("将PdfPage的面对象转换成Page的对象")
        return Page(page.getPageNum())


# 导入os库
import os

class Reader:
    "阅读器"

    def __init__(self, name):
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if(extName.lower() == ".epub"):
            self.__curBook = EpubBook()
        elif(extName.lower() == ".txt"):
            self.__curBook = TxtBook()
        elif(extName.lower() == ".pdf"):
            self.__curBook = PdfAdapterBook()
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if(self.__curBook is not None):
            rtn = self.__curBook.parseFile(filePath)
            if(rtn):
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print("关闭 " + self.__filePath + " 文件")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        return self.gotoPage(self.__curPageNum - 1)

    def nextPage(self):
        return self.gotoPage(self.__curPageNum + 1)

    def gotoPage(self, pageNum):
        if(pageNum < 1 or pageNum > self.__curBook.getPageCount()):
            return None

        self.__curPageNum = pageNum
        print("显示第" + str(self.__curPageNum) + "页")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getContent()
        return page

"""测试代码："""

def testReader():
    reader = Reader("阅读器")
    if(not reader.openFile("平凡的世界.txt")):
        return
    reader.showCatalogue()
    reader.gotoPage(1)
    reader.nextPage()
    reader.closeFile()
    print()

    if (not reader.openFile("平凡的世界.epub")):
        return
    reader.showCatalogue()
    reader.gotoPage(5)
    reader.nextPage()
    reader.closeFile()
    print()

    if (not reader.openFile("平凡的世界.pdf")):
        return
    reader.showCatalogue()
    reader.gotoPage(10)
    reader.nextPage()
    reader.closeFile()
