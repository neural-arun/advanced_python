class MyCustomError(TypeError):
    # main ek naya error bana raha hoon.
    # jo typeerror jaisa behave karega.
    def __init__(self,message,code):
        super().__init__(f"code message {code}: {message}")  # ye bta raha hai parent class ko ki tum apna kaam karlo pahle

        self.code = code  # this is an attribute of class my custom error.

raise MyCustomError("ouch",500)