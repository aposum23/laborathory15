def hello_world():
    print('hello wordl!')

type(hello_world)
#<class 'function'>
class Hello:
    pass
type(Hello)
#<class 'type'>
type(10)
#<class 'int'>

def wrapper_function():
    def hello_world():
        print('hello world!')
    hello_world()

wrapper_function()
#hello world!
