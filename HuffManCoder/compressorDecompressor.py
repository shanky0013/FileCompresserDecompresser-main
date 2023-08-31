import heapq
import os
class BinaryTree:
    def __init__(self,value,frequency):
        self.value=value
        self.frequency=frequency
        self.right=None
        self.left=None

    def __lt__(self,temp):
        return self.frequency<temp.frequency
    
    def __eq__(self,temp):
        return self.frequency==temp.frequency

class HuffmanCode:
    def __init__(self,path):
        self.path=path# file path for upload and download
        self.__arr=[] # container for heap
        self.__binary={} # mapping between text and encodings
        self.__parent={} # mapping of code and characters
    
    def __getTextFrequency(self,text):
        freqDict={}
        for ch in text:
            if ch not in freqDict:
                freqDict[ch]=0
            freqDict[ch]+=1
        return freqDict
    
    def __buildHeap(self,freq):
        for key in freq:
            node=BinaryTree(key,freq[key])
            heapq.heappush(self.__arr,node)
        
    def __buildBinaryTree(self):
        while len(self.__arr)>1:
            node1=heapq.heappop(self.__arr)
            node2=heapq.heappop(self.__arr)
            supernode=BinaryTree(None,node1.frequency+node2.frequency)
            supernode.right=node2
            supernode.left=node1
            heapq.heappush(self.__arr,supernode)
        return
    
    def __getBinHelper(self,root,bits):
        #base case
        if root is None:
            return
        if root.value is not None:
            # leaf node is reached
            self.__binary[root.value]=bits
            self.__parent[bits]=root.value
            return
        #recursive case
        #moving left
        self.__getBinHelper(root.left,bits+'0')
        #moving right
        self.__getBinHelper(root.right,bits+'1')

    def __getBinaryCodeFromTree(self):
        root=heapq.heappop(self.__arr)
        self.__getBinHelper(root,'')

    def __encode(self,text):
        temp=''
        for ch in text:
            temp+=self.__binary[ch]
        return temp
    
    # now as the data will be stored in bits of 8 so we need to add some padding/bits of zeros towards end of the binary code so we need to add the padding and store the padding information
    def __getPaddedCode(self,encodedText):
        padding=8-(len(encodedText)%8)
        for i in range(padding):
            encodedText+='0'
        paddingInfo="{0:08b}".format(padding)
        finalCode=paddingInfo+encodedText
        return finalCode
    
    def __convertToBytes(self,paddedText):
        temp=[]
        for i in range(0,len(paddedText),8):
            byteArr=paddedText[i:i+8]
            temp.append(int(byteArr,2))
        return temp

    def fileCompress(self):
        fileName,fileExtension=os.path.splitext(self.path)
        outputPath=fileName+'.bin'
        with open(self.path,'r+') as file,open(outputPath,'wb') as output:
            text=file.read()
            text=text.rstrip()
            freq=self.__getTextFrequency(text)
            build_heap=self.__buildHeap(freq)
            self.__buildBinaryTree()
            self.__getBinaryCodeFromTree()
            encoded_text=self.__encode(text)
            padded_text=self.__getPaddedCode(encoded_text)
            byte_arr=self.__convertToBytes(padded_text)
            #padding the encoded text
            byteData=bytes(byte_arr)
            output.write(byteData)
        print("compressed Successfuly")
        return outputPath
    
    def __decode(self,text):
        temp=''
        curr=''
        for ch in text:
            curr+=ch
            if curr in self.__parent:#if substring found then map it to text value
                temp+=self.__parent[curr]
                curr=''
        return temp
            


    def __removePadding(self,text):
        paddingInfo=text[:8]
        padding=int(paddingInfo,2)
        text=text[8:]
        text=text[:-1*padding]
        return text

    
    def fileDecompress(self,inputPath):
        fileName,fileExtension=os.path.splitext(inputPath)
        outputPath=fileName+'_decompressed.txt'
        print(fileName)
        print(fileExtension)
        with open(inputPath,'rb') as file,open(outputPath,'w') as output:
            bitString=''
            byteData=file.read(1)
            while byteData:
                byteData=ord(byteData)
                bits=bin(byteData)[2:].rjust(8,'0')
                bitString+=bits
                byteData=file.read(1)
            preprocessedText=self.__removePadding(bitString)
            processedText=self.__decode(preprocessedText)
            output.write(processedText)
        return outputPath
    
# if __name__=='main':
#     path='some.txt'
#     h=HuffmanCode(path)
#     compressedFile=h.fileCompress()
#     h.fileDecompress(compressedFile)


