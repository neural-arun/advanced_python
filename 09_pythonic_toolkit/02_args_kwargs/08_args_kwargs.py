def demo(*args,**kwargs):
    print(args)
    print(kwargs)

demo(1,2,4,5,6,name="arun",subject="args and kwargs", is_studying=True)