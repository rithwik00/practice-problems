# given targetWord and array of words(wordbank)
# find if targetword can be generated/concatinated by using the array elements(repeated  allowed)

def canConstruct(targetWord, wordbank):
    # print(visited) 
    if targetWord in visited:
        return visited[targetWord]

    if targetWord == '':
        return True

    for word in wordbank:
        try:
            if  targetWord.index(word) == 0:
                suffix = targetWord[len(word):]
                if canConstruct(suffix, wordbank):
                    visited[word] = True 
                    return True
        except:
            pass

    visited[targetWord] = False
    return False
 
visited = {}
print(canConstruct('abcdef', ['abc', 'def', 'c']))
visited = {}
print(canConstruct('abcdefdef', ['abc', 'def', 'c']))