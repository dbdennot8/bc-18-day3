
"""count the words in a phrase"""



def word_counter(phrase):
	phrase_list = phrase.split()
	word_count = {}

	for word in phrase_list:

		if word in word_count:
			word_count[word] += 1

		else:
			word_count[word] = 1

	for keys, values in word_count.items():
		print str(keys) + ":" + str(values)



#word_counter("olly olly in come free")
#word_counter("word")
#word_counter("car : carpet as java : javascript!!&@$%^&")
#word_counter("testing 1 2 testing")
#word_counter("go Go GO")
