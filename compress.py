import os
import re

class Compressor:
    def __init__(self, path):
        self.file = open(path, 'r')
        temp = os.path.basename(path)
        self.name = os.path.splitext(temp)[0]
    
    @staticmethod
    def dict_format(words):
        output = ""
        for word in words:
            output += word + ','
        return output[:-1]

    def compress(self):
        frecv = []
        output = ""
        compressed = open(f"compressed_{self.name}.comp",'w+')
        for line in self.file:
            for word in re.split("(\W)", line):
                if word == '\n':
                        word = 'n'
                if word not in frecv:
                    frecv.append(word)
                output+=str(frecv.index(word))+','
        compressed.write(f"{self.dict_format(frecv)}\n")
        compressed.write(output)

    def decompress(self):
        decompressed = open(f"{self.name}.dtxt", 'w+')
        dict_string = self.file.readline()
        dic = dict_string.replace(',n,',',\n,').split(',')
        output = ""
        for line in self.file:
            indexes = line.split(',')
            for i in indexes:
                output += dic[int(i)]

        decompressed.write(output[:-1])
        
