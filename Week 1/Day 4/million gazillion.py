class Trie(object):
    def __init__(self,):
        self.node = {}

    def add_word(self, word):
        node = self.node
        for c in word:
            if c in node:
                node = node[c]
            else:
                node[c] = {}
                node = node[c]
        if '$' in node:
            return False
        node['$'] = {}
        return True

# Test Cases

trie = Trie()

result = trie.add_word('catch')
expected = True
print(expected == result)

result = trie.add_word('cakes')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = True
print(expected == result)

result = trie.add_word('cake')
expected = False
print(expected == result)

result = trie.add_word('caked')
expected = True
print(expected == result)

result = trie.add_word('catch')
expected = False
print(expected == result)

result = trie.add_word('')
expected = True
print(expected == result)

result = trie.add_word('')
expected = False
print(expected == result)