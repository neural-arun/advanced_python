class UncountableError(TypeError):
    def __init__(self,wrong_value):
        self.wrong_value  = wrong_value
        super().__init__(f"Invalid value for {wrong_value}.")





def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
    
count_from_zero_to_n(-4)