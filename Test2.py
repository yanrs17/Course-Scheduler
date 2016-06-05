import re, ast
doc = r"""{
        "grade": " something \"B+\" something "
    }
}
"""

#html_doc = "r"+html_doc

start, value, last = re.match(r'(\s*{\s*".*?"\s*:\s*")(.*)("\s*})', doc).groups()
fixed = value.replace('"', "") # remove quotes
fixed = value.replace("\\\"", "")
d = (start + fixed + last)
print(ast.literal_eval(d))