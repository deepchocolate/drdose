import re
from .num import isNumeric
# Remove repeated spaces
def rmExtraSpace(txt):
	while txt.find('  ') != -1: txt = txt.replace('  ', ' ')
	return txt

def polish(txt, chars='.?*=-+"!,\n'):
	"""
	Remove "unnecessary" characters at tails of words and extra whitespace.
	"""
	words = [x.strip(chars) for x in txt.split(' ')]	
	return ' '.join(words)

# Regular expressions used by separatechars()
RE_SEPLEADINTFROMSTR = re.compile('[0-9]+[A-Za-z]')
RE_SEPWORDS = re.compile('[a-z][\.,][a-z]')

def separateChars(txt, regExpr):
	"""
	Separate characters in string txt depending on the regular expression regExpr. 
	"""
	found = regExpr.search(txt)
	if found != None:
		st = found.start()
		ed = found.end() - 1
		return separateChars(txt[0:ed] + ' ' + txt[ed:], regExpr)
	else: return txt

def separateLeadIntFromStr(txt):
	return separateChars(txt, RE_SEPLEADINTFROMSTR)

def separateWords(txt):
	return separateChars(txt, RE_SEPWORDS)

def simplify(txt, stripChars=')(.?*=-+"!,\n'):
	"""
	Lowercase, remove extra whitespace and "unnecessary" characters at
	tails of words in string txt.
	"""
	return polish(rmExtraSpace(txt.lower()), stripChars)


def replaceNumbers(txt, replacement='#'):
	"""
	Replace numbers in string txt with replacement.
	"""
	return ' '.join(['#' if isNumeric(x) else x for x in txt.split(' ')])

INPUT_FILTERS = {
	'standard':[rmExtraSpace, separateWords, separateLeadIntFromStr, polish]
}
#samp = '1word word.word 2word word.words'
#print(separateChars(separateChars(samp, RE_SEPWORDS),RE_SEPLEADINTFROMSTR))