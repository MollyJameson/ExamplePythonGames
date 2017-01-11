
#Wiki version: https://en.wikipedia.org/wiki/Mad_Libs

#In a real game maybe read several of thse from a file
requests = ["exclamation","adverb","noun","adjective"]
responses = []
end_phrase = "{}! he said {} as he jumped into his convertible {} and drove off with his {} wife."


for i in range(len(requests)):
  responses.append( raw_input("Enter a " + requests[i] + ": "))

#See more magic of formatting here: https://docs.python.org/2/library/string.html
# For example, the things in the curly brackets could be named instead
print end_phrase.format(*responses)