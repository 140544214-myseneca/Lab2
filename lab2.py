import sys

def print_script_and_vars():
    script = sys.argv[0]
    vars = sys.argv[1:]
    print("Script:", script)
    print("Variables:", vars)

print_script_and_vars()

def helloWorld():
    print('Hello World')

helloWorld()
