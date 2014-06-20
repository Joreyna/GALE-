#making a gene dictionary that contains all of the genes
#and the lines that are associated with them.
def getGeneDictionary():
    with open('ABRCsent.csv', 'r') as salkLinesReader: 
        geneDict = {}
        for line in salkLinesReader:
            details = line.strip().split(',')
            if details[3] in geneDict:
                geneDict[details[3]].append(details[1])
            else: 
                geneDict[details[3]] = [details[1]]
    return geneDict


#making the sif 
with open('SalkLineInteractions.sif','w') as sliWriter, open('Data.csv','r') as ppiReader:
    geneDict = getGeneDictionary() 
    ppiReader.readline()
    for line in ppiReader:
        details = line.strip().split(',')
        if details[0] in geneDict and details[1] in geneDict:
            firstGeneList = geneDict[details[0]]
            for salk1 in firstGeneList:
                secondGeneList = geneDict[details[1]]
                for salk2 in secondGeneList: 
                    sliWriter.write('\t'.join([salk1, details[2],salk2]) + '\n')