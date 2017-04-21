#a node type to build the Trie with
class TrieNode:
	
	def __init__(self):
		self.EndOfWord = False #determines if the node ends a sequence of nodes that make up a word
		self.allChildrenCharacters = [] #keep track of the valid characters that can be accepted be the node
		self.children = {} #list of children nodes of the node
	
	#creates a child node with the parameter character associated
	def addChild(self, character, childNode):
		self.allChildrenCharacters.append(character)
		self.children[character] = childNode
	
	def getChild(self, character):
		return self.children[character]
		
	#if the trie building algorithm determines that this node ends a word then this flag is set
	def setAsEndOfWord(self):
		self.EndOfWord = True
		
	def isEndOfWord(self):
		return self.EndOfWord
		
	def getAllChildrenCharacters(self):
		return self.allChildrenCharacters

#trie built using specified input text file
class Trie:

	def __init__(self, dictionaryFileName):
		self.root = TrieNode() #root of the trie
		self.dictionaryReader = open(dictionaryFileName)
		self.buildTrie() #initialize trie with dictionary dataset from text file
		
	def buildTrie(self):
		#get every line in the text file and add them al to the trie
		for line in self.dictionaryReader:
			line = line.strip('\n')
			if(line == ""):
				continue
			self.addWord(line)
		self.dictionaryReader.close()
			
	def addWord(self, line):
		self.createChild(self.root, 0, line)
		
	def createChild(self, curNode, curWordIndex, line):
		#check if node is already in the trie to avoid overriding nodes with children
		#if the node is not found, it is created
		try:
			curNode.getChild(line[curWordIndex])
		except KeyError:
			curNode.addChild(line[curWordIndex], TrieNode())
			
		#if the index has reached the end of string line, the current node marks the end of a word
		if(curWordIndex+1 == len(line)):
			curNode.setAsEndOfWord()
		else:
			self.createChild(curNode.getChild(line[curWordIndex]), curWordIndex+1, line)
				
	def matchPattern(self, pattern):
		curNode = self.root
		resultsExist = True
		
		#obtain the node that designates the pattern string
		#set a flag to skip the recursive step if a node doesn't exist for the pattern
		for character in pattern:
			try:
				curNode = curNode.getChild(character)
			except KeyError:
				resultsExist = False
				break
				
		if(resultsExist):
			self.printAllChildren(curNode, pattern, "")

	def printAllChildren(self, curNode, pattern, addedCharacters):
		#if an EndOfWord flag is found, out put the pattern concatinated with the recorded characters used to get to the node
		if(curNode.isEndOfWord()):
			print(pattern + addedCharacters)
		#repeat for the entire subtree
		for character in curNode.getAllChildrenCharacters():
			self.printAllChildren(curNode.getChild(character), pattern, addedCharacters+character)