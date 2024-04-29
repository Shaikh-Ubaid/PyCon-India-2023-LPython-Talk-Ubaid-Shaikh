# get_email is implemented in email_extractor_util.py
# which is intimated to LPython by specifiying
# the file as module in `@pythoncall` decorator

@pythoncall(module="email_extractor_util")
def get_email(text: str) -> str:
    pass

text: str = "Hello, my email id is lpython@lcompilers.org."
print(get_email(text))
