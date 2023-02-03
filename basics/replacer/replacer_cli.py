import replacer
import sys

#print(sys.argv)

old = " "
if len(sys.argv) >= 2:
    old = sys.argv[1]

new = "🐹"
if len(sys.argv) >= 3:
    new = sys.argv[2]

for line in sys.stdin.readlines():
    replaced = replacer.replace_content(line, old, new)
    #print(replaced.strip())
    print(replaced, end="")
