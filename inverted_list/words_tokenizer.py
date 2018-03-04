import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import regex as re
#write a for-loop to open many files
files=[]

def word_tokenizer(files,n=1):
    pdfFileObj=[]
    pageObj=[]
    pdfReader=[]
    num_pages=[]
    count=[0]*n
    text=[]
    tokens=[]
    keywords=[]
    keywords_final=[]
    #open allows you to read the file
    print files[0]
    for val in files:
        pdfFileObj.append(open(val,'rb'))

    #The pdfReader variable is a readable object that will be parsed
    for val in pdfFileObj:
        pdfReader.append(PyPDF2.PdfFileReader(val))

    #discerning the number of pages will allow us to parse through all the pages
    for val in pdfReader:
        num_pages.append(val.numPages)

    #The while loop will read each page
    for i in range(n):
        while count[i] < num_pages[i]:
            pageObj.append(pdfReader[i].getPage(count[i]))
            count[i] +=1
        for val in pageObj:
            text.append(val.extractText())
    #This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
    for i in range(n):
        if text[i] != "":
            text[i] = text[i]

    #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

        else:
           text[i] = textract.process(fileurl, method='tesseract', language='eng')
    # Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.

    # Now, we will clean our text variable, and return it as a list of keywords.

    #The word_tokenize() function will break our text phrases into #individual words
    for val in text:
        tokens.append(word_tokenize(val))
    #we'll create a new list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',','.','-','?']

    #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

    stop_words = stopwords.words('english')

    #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
    for words in tokens:
        for i in range(len(words)):
            if (not words[i] in stop_words and not words[i] in punctuations):
                keywords.append([words[i]])
    #keywords=[word for word in tokens if not word in stop_words and not word in punctuations]
    for val in keywords:
        for v in val:
            keywords_final.append(v.encode("utf-8"))

    for val in keywords_final:
        if (not val.isalpha()) or re.search(val,"\\x+")!=None or re.search(val,"\\[a-z]+\\[a-z]+")!=None:
            keywords_final.remove(val)

    return keywords_final

    # #making a list of keywords of unique keys in first file
    # v1=[[x,keywords1_final.count(x)] for x in set(keywords1_final)]
    #
    # #making a list of keyword of unique keys in second file
    # v2=[[x,keywords2_final.count(x)] for x in set(keywords2_final)]
    #
    # #merging the lists to get the final list
