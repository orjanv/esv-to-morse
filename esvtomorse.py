#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  esv_to_morse.py
#  

import sys, urllib

morsetab = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': '/',               '_': '..--.-',
        '[': '-.--.',			']': '-.--.-',
        '\n': '·-·-',			'"': '.----.',
}


class ESVSession:
	def __init__(self, key='IP'):
		options = ['include-short-copyright=0',
		'output-format=plain-text',
		'include-passage-horizontal-lines=0',
		'include-heading-horizontal-lines=0',
		'include-headings=0',
		'include-footnote-links=0',
		'include-footnotes=0',
		'include-passage-references=1']
		self.options = '&'.join(options)
		self.baseUrl = 'http://www.esvapi.org/v2/rest/passageQuery?key=%s' % (key)

	def doPassageQuery(self, passage):
		passage = passage.split()
		passage = '+'.join(passage)
		url = self.baseUrl + '&passage=%s&%s' % (passage, self.options)
		page = urllib.urlopen(url)
		return page.read()

	def toMorse(self, s):
		from string import lower
		m = ''
		for c in s:
			c = lower(c)
			if morsetab.has_key(c):
				c = morsetab[c] + ' '
			else:
				c = '? '
			m = m + c
		return m
		
def main():
	
	try:
		key = sys.argv[2]
	except IndexError:
		key = 'IP'

	bible = ESVSession(key)

	try:
		text = bible.doPassageQuery(sys.argv[1])
		print '\n' + text + '\n'
		print bible.toMorse(text)
		exit(1)
	except IndexError:
		text = ''

	print "The ESV Bible passage morse translator."
	print "Enter a passage to translate to morse (ex. Ecc 3:11) or 'quit' to end."

	passage = raw_input('Enter passage: ')
	while passage != 'quit':
		text = bible.doPassageQuery(passage)
		print text + '\n'
		print bible.toMorse(text)
		passage = raw_input('Enter passage: ')
		
if __name__ == '__main__':
	main()
