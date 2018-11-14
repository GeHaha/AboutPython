# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:17:55 2018

@author: Gehaha
"""

from os import path
import logging

class ZIPModel:
    "ZIPZ模块，负责zip文件的压缩与解压"
    def compress(self,srcFilePath,dstFilePath):
        print("ZIP模块正在进行'" + srcFilePath + "'文件的压缩....")
        print("文件压缩成功，以保存至 '" + dstFilePath + "'")
        
    def decompress(self,srcFilePath,dstFilePath):
        print("ZIP 模块正在进行'" + srcFilePath + "'文件的解压....")
        print("文件压缩成功，以保存至 '" + dstFilePath + "'")
        
class RARModel:
    "RAR模块，负责zip文件的压缩与解压"
    
    def compress(self,srcFilePath,dstFilePath): 
        print("RAR模块正在进行'" + srcFilePath + "'文件的压缩....")
        print("文件压缩成功，以保存至 '" + dstFilePath + "'")
        
    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行 '" + srcFilePath + "' 文件的解压......")
        print("文件解压成功，已保存至 '" + dstFilePath + "'")

class ZModel:    
    
    "7Z模块，负责7Z文件的压缩与解压"
    def compress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 '" + srcFilePath + "' 文件的压缩......")
        print("文件压缩成功，已保存至 '" + dstFilePath + "'")

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 '" + srcFilePath + "' 文件的解压......")
        print("文件解压成功，已保存至 '" + dstFilePath + "'")

class CompressionFacade:
    "压缩系统的外观类"
    
    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()
        
    def compress(self,srcFilePath,dstFilePath,type):
        "根据不同的压缩类型，压缩成不同的格式"
        #获取新的文件名
        extName = '.' + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath,fullName)
        elif (type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath,fullName)
        elif (type.lower() == "7z"):
            self.__zModel.compress(srcFilePath,fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return  False
        return True
    def decompress(self,srcFilePath,dstFilePath):
        "从srcFilePath中获取后缀，根据不同的后缀名（拓展名），进行不同格式的压缩"
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() =='zip'):
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True
    
def testCompression():
    facade = CompressionFacade()
    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "zip")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.zip",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()

    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "rar")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.rar",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()

    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "7z")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.7z",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()          
























