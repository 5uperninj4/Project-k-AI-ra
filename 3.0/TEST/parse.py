import unicodedata
import codecs
infile = codecs.open('C:/Users/logan/Documents/Coding/Python/KAIra/3.0/Main/dialogues_text.txt','r',encoding='utf-8',errors='ignore')
outfile = codecs.open('C:/Users/logan/Documents/Coding/Python/KAIra/3.0/Main/dialogues.txt','w',encoding='utf-8',errors='ignore')


for line in infile.readlines():
    for word in line.split():
        outfile.write(word+" ")
    outfile.write("\n")

infile.close()
outfile.close()