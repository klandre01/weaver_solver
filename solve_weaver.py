import string

def word_bank():
    dictionary = open("word_bank.txt", "r")
    word_bank = dictionary.read().splitlines()
    return word_bank

def isWord(word):
    if word.lower() in word_bank:
        return True
    return False

def create_graph():
    for w in Adj:
        for i in range(4):
            word = list(w)
            for char in alphabet:
                if word[i] == char:
                    continue
                word[i] = char
                new_word = ''.join(word)
                if not(new_word == w) and isWord(new_word) and new_word not in Adj[w]:
                    Adj[w].append(new_word)

def bfs(Adj, start, finish):
    parent = {child: None for child in Adj}
    parent[start] = start
    visited = [start]
    queue = [start]
    while queue:
        for u in Adj[queue[0]]:
            if u not in visited:
                queue.append(u)
                parent[u] = queue[0]
                visited.append(u)
        queue.pop(0)
    
    if parent[finish] == None:
        return None
    
    i = finish
    path = [finish]
    while i != start:
        i = parent[i]
        path.append(i)
    return path[::-1]

def solve():
    start = input('Starting word: ')
    if start.lower() not in word_bank:
        print(f"{start} is not in the dictionary")
        return
    finish = input('Finish word: ')
    if finish.lower() not in word_bank:
        print(f"{finish} is not in the dictionary")
        return
    create_graph()
    print(bfs(Adj, start, finish))

word_bank = word_bank()
alphabet = list(string.ascii_lowercase)
Adj = {w: [] for w in word_bank}
solve()