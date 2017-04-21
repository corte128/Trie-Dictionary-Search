import Trie

def main():
	patternSearcher = Trie.Trie('words.txt')

	while(True):
		pattern = input("Enter the pattern: ")
		patternSearcher.matchPattern(pattern)
		
main()