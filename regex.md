# Regular Expressions (Reg ex)

### Exact string match

```
['tugboat', 'tugboats']
Regex: 'tugboat'
Found: once, exact match.
```

### Wild character match

```
'.' Will match any single character in a regex.
['tugboat', 'tugboats']
Regex: 'tugboat.'
Found: 'tugboats'

```

### Match character if it exists, but do no require it

##### '?' Matches the character that appears before it, zero or one time.

```
['tugboat', 'tugboats']
Regex: 'tugboats?'
Found: 'tugboat', 'tugboats'

['tugboat', 'tugbots']
Regex: 'tugboa?ts?'
Found: 'tugboat', 'tugbots'
```

##### You can make a character set optional.
```
['toyboat', 'toyboats', 'toy boats', 'Toy boats', 'joy boats', 'toy-boats', 'toy-Boat']
Regex: [Ttj]oy[ -]?boats?
Note: The '?' before a character set makes a character set optional.
Found: 'toyboat', 'toyboats', 'toy boats', 'Toy boats', 'joy boats', 'toy-boats'
Excluded: 'toy-Boat'
```

### Capital Case and lower case matching of characters

```
['tugboat', 'tugboats', 'toy boats', 'Toy boats']
Regex: '[Tt]oy ?boats?'
Found: 'toy boats', 'Toy boats'
```
##### '[]' No matter how many characters we put in the set, the set will only match the position of the character we put it in. It also makes no difference how you order the characters.

```
['tugboat', 'tugboats', 'toy boats', 'Toy boats', 'joy boats']
Regex: '[Ttj]oy[ -]?boats?'
Found: 'toy boats', 'Toy boats', 'joy boats'
```

### Ranges of characters

##### If you want to find a range of characters such as 'A' thru 'Z'.

```
['toyboat', 'toyboats', 'toy boats', 'Toy boats', 'joy boats', 'toy-boats', 'toy-Boat']
Regex: '[A-Z]oy ?boats?'
Found: All upper case
```

##### If you want to find a range of characters such as 'A' thru 'Z' in both capital and lower case you can put the range of character right next to each other in the set.

```
['toyboat', 'toyboats', 'toy boats', 'Toy boats', 'joy boats', 'toy-boats', 'toy-Boat']
Regex: '[A-Za-z]oy[ -]?boats?'
Results: All
```

### Regular Expression Wildcards

##### Matches more than one character in a string

```
[0-9] --> \d
[A- Za-z0-0] --> \w
[ \t\r\n\f] --> \s
Any Character --> .
```

### Repeating Character Matches

```
Matched Pattern --> Character
Zero or More --> '*' --> None or all characters
One or more --> '+' --> Must have at least one character
Zero or one --? '?' --> May have none or one character.
```

##### Using '*'

```
['toy', 'toyboat', 'toycar']
Regex: 'toy\w*'
Result: Returns anything that starts with 'toy', has a letter or number after and has any number of characters after that. In this case, the whole array of strings is returned.
```

##### Using '+'

```
['toy', 'toyboat', 'toycar']
Regex: 'toy\w+'
Result: Returns anything that starts with 'toy' and has at least one character afterward.
```

##### Exact Number of Character Matches

```
Mattched Pattern --> Character
Three --> {3} --> Exactly three
Three or more --> {3, } --> Three or greater
Between 3 and 5 --> {3, 5}
```

##### Social security number example

```
\d{3}-\d{2}-\d{4}
000-23-7674
000-45-8792
```

### Negated Characters

```
Matched Pattern --> Character
Negated character set --> [^]
Match and character except '@' --> [^@]
Match any character except '@' and '.' --> [^@.]
```

### Opposite Characters

```
Character --> Opposite
\s White Space --> \S Not white space
\d Digit --> \D Not digit
\w Word --> \W not word
\s Whitespace --> \S Not whitespace
```

### Alternation / Pipes

```
['toy boat', 'sail boat', 'steam boat', 'tug boat']
toy|sail|tug boat
```

### Wildcard Group Matching

```
Matched Pattern --> Character
Matches 'subsub' --> (sub){2}
Macthes 'pat' and 'subpat' --> (sub)?pat
```

##### Matches three substraights
```
['toy boat', 'sail boat', 'steam  boat', 'tug boat']
Regex: (toy|sail|tug) boat
Match: Returns all except 'steam boat'
```

### Partial Matches

```
Matched Pattern --> Character
Beginning of a string -- > '^'
End of a string --> '$'
```

### Regex In Python

##### Opening a txt file to parse
```python
"""

"""
import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

print(re.match(r'Love', data))  # The 'r' in front of a string indicates that we are using a raw string; we can avoid using character escaping this way.
print(re.search(r'Kenneth', data))  # Use 'match' to find text at the beginning of a string. Use 'search' to find text anywhere in the string.
```