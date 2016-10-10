# Regex Query Tool
# A tool that allows the user to enter a text string and then in a separate control enter a regex pattern. It will run the regular expression against the source text and return any matches or flag errors in the regular expression.

import re # for ease of regex

# Investigate why function call fails
"""
def regexQuery(txtStr, ptrn):
    result = re.search(ptrn, txtStr)
    print(result)
"""

print("\n\t\tRegex query tool")
txtStr = input("\nEnter your text string: ")
ptrn = input("\nEnter your regex pattern: ")
# regexQuery(txtStr, ptrn)

rs = re.search(ptrn, txtStr)
print(rs.group())


