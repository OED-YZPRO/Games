import random
word_list = [
             'nigga', 'arata', 'ayden', 'ninja', 'viles', 
             'vital', 'monks', 'beast', 'myths', 'cynic', 
             'shits', 'burns', 'dalif', 'nikes', 'zhong',
             'trump', 'putin', 'games', 'trash', 'bozos',
             'hello', 'trace', 'grace', 'crush', 'death',
             'lives', 'cruel', 'delta', 'crypt', 'lymph',
             'lynch', 'bunch', 'shyly', 'pound', 'tiers'
                                                ]

word = random.choice(word_list)


cword = list(word)
stack = [
          ['_', '_', '_', '_', '_',],
          ['_', '_', '_', '_', '_',], 
          ['_', '_', '_', '_', '_',],
          ['_', '_', '_', '_', '_',],
          ['_', '_', '_', '_', '_',],
          ['_', '_', '_', '_', '_',] 
                                      ]
for line in stack:
    print(*line)
  
print('= : correct, / : wrong position, ! : not included')


for ind, item in enumerate(stack):
    ans = list(input().strip())
      
    for i, letter in enumerate(item):
      
      if ans[i] == cword[i]:
        stack[ind][i] = ans[i] + '='
      elif ans[i] in cword:
        stack[ind][i] = ans[i] + '/'
      else:
        stack[ind][i] = ans[i] + '!'
      
    
    if ans == cword:
      for line in stack:
        print(*line)
      print("Lucky guy.")
      exit()
      
    for line in stack:
      print(*line)

print("Nice try bozo.")
exit()
  
