

categories = ["Terrain", "Portal", "Unit", "Building"]#, "UnitType", "BuildingType"]

timePeriodConversion = {0:"farPast", 1:"past", 2:"present"}

unitTypeConversion = {0:'civE', 1:'art', 2:'spear', 3:'artil', 4:'cav', 5:'pig'}

class statusParser:
    #takes a status message, which is a string.
    def __init__(self, statusMessage):
        self.message = statusMessage
        self.messageType = self.findType()
        self.messageDict = {}

    
    def parse(self):
        if self.messageType == "changed":
            self.categorize()
        else:
            """
            TODO: animiation parsing
            """
            pass
        return self.messageDict
        
    
    #Determines type of message
    def findType(self):
        type = ""
        if self.message.find("changed")!=-1:
            type = "changed"
        elif self.message.find("animations")!=-1:
            type = "animations"
        else:
            raise Exception('Message was not "changed" or "animations"' )
        return type
    
    #parses a "changed" status message into a status Dictionary
    def categorize(self):
        indices = {}
        
        for cat in categories:
            indices[cat]=self.message.find('("'+cat+'"')

        
        parens = self.parenthesize(self.message)
        
        for cat in categories:
            if indices[cat] != -1:
                print "Parsing Category: ", cat
                self.messageDict[cat] = self.parseCategory(self.message, parens, indices[cat])
                print "Parsing InfoList for: ", cat
                self.messageDict[cat] = self.parseInfoList(self.messageDict[cat], self.parenthesize(self.messageDict[cat]))
                print "Parsing Lists to Dictionaries for: ", cat
                self.messageDict[cat] = self.parseStringtoDict(cat, self.messageDict[cat])

            else:
                print "Category not present: ", cat
                self.messageDict[cat] = None
        print "Sorting according to time periods..."
        #self.messageDict = self.sortByPeriod()
                        
        
    #changes a whole status string into smaller categories (Terrain, Unit, etc)
    def parseCategory(self, message, parenlist, startIndex):
        done = False
        index = parenlist.index(startIndex)
        parenCount = 0
        
        while not done:
            #print "Index", index, " Paren: ", parens[index], " Status: ", self.message[parens[index]]
            
            temp = message[parenlist[index]]
            
            #if temp == " ":
            #   temp = self.message[parens[index]-1]
            
            if temp == "(":
                parenCount +=1
            elif temp == ")":
                parenCount -=1
            if parenCount == 0:
                done = True
            index +=1
        
        return message[startIndex:parenlist[index]]
    #Parses a particular category from one long string into a list of strings containing information    
    def parseInfoList(self, message, parenlist):
        done = False
        index = 1
        parenCount = 0
        retList = []

        
        while not done:
            #print "Index", index, " Paren: ", parenlist[index], " Status: ", self.message[parenlist[index]]
            #print "   Paren List: ", parenlist[index]
            #print "   Message at index: ", message[parenlist[index]]
            temp = message[parenlist[index]]
            
            
            if temp == "(":
                parenCount +=1
                start = index
            elif temp == ")":
                parenCount -=1
                stop = index
            
            if parenCount == 0:
                retList.append(message[parenlist[start]:parenlist[stop]+1])
                print "   Message: ", message[parenlist[start]:parenlist[stop]+1]
            
            index +=1
            
            
            if index >= parenlist.__len__():
                done = True
                #print "***************************************"
        
        return retList
        
        
    #returns an array of all parentheses in the order they appear. so "(bleh)((cheese))" would be [0,5,6,7,14,15]
    def parenthesize(self, message):
        parens = []
        
        #find open parentheses      
        temp = message.find("(")
        while(temp != -1):
            parens.append(temp)
            temp = message.find("(", temp+1)
        
        #find close parentheses
        temp = message.find(")")
        while(temp!= -1):
            parens.append(temp)
            temp = message.find(")", temp+1)
            
        parens.sort()
        
        #print "*******************PAREN SIZE: ", parens.__len__()
    
        return parens
    
    #parses a category's list of strings into a list of dictionaries for the visualzier
    def parseStringtoDict(self, categoryName, categoryList):
        retDict = {}
        retList = []
        
        listofLists = []
        
        for item in categoryList:
            listofStrings = item.strip("(").strip(")").split(" ")
            listofValues = []
        
            for item in listofStrings:
                try:
                    listofValues.append(int(item))
                except:
                    listofValues.append(item)
            
            listofLists.append(listofValues)
            #print "List of Lists: ", listofLists

            
        if categoryName == "Terrain":
            for item in listofLists:
                retDict['objectID'] = item[0]
                retDict['location'] = (item[1], item[2])
                retDict['period'] = timePeriodConversion[item[3]]
                retDict['blockMove'] = item[4]
                retDict['blockBuild'] = item[5]
                retList.append(retDict)
                #print "retDict: ", retDict


        if categoryName == "Portal":
            for item in listofLists:
                retDict['objectID'] = item[0]
                retDict['location'] = (item[1], item[2])
                retDict['period'] = timePeriodConversion[item[3]]
                retDict['direction'] = item[4]
                retDict['fee'] = item[5]
                retList.append(retDict)
                #print "retDict: ", retDict

                
        if categoryName == "Unit":
            for item in listofLists:
                retDict['objectID'] = item[0]
                retDict['location'] = (item[1], item[2])
                retDict['period'] = timePeriodConversion[item[3]]
                retDict['hp'] = item[4]
                retDict['level'] = item[5]
                retDict['unitType'] = item[6]
                retDict['ownderIndex'] = item[7]
                retDict['actions'] = item[8]
                retDict['moves'] = item[9]                
                retList.append(retDict)
                #print "retDict: ", retDict

                
        if categoryName == "Building":
            for item in listofLists:
                retDict['objectID'] = item[0]
                retDict['location'] = (item[1], item[2])
                retDict['period'] = timePeriodConversion[item[3]]
                retDict['hp'] = item[4]
                retDict['level'] = item[5]
                retDict['buildingType'] = item[6]
                retDict['ownderIndex'] = item[7]
                retDict['inTraining'] = item[8]
                retDict['progress'] = item[9]
                retDict['linked'] = item[10]
                retDict['complete'] = item[11]                
                retList.append(retDict)
                #print "retDict: ", retDict
        for item in retList:
            print "retList's objID: ", item['objectID']

        return retList
    
    def sortByPeriod(self):
        farPastDict = {}
        pastDict = {}
        presentDict = {}
        
        for key in self.messageDict.keys():
            farPastDict[key]=[]
            pastDict[key]=[]
            presentDict[key] = []
        
        for key, list in self.messageDict.iteritems():
            for dict in list:
                if dict['period']=="farPast":
                    farPastDict[key].append(dict)
                if dict['period'] == "past":
                    pastDict[key].append(dict)
                if dict['period'] == "present":
                    presentDict[key].append(dict)
        
        return {"farPast":farPastDict, "past":pastDict, "present":presentDict}
            
            
            
            
            