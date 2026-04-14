def Ind_fav(fruit, fruits):
    def Aswr():
        return f"I love eating {fruit()}"
    return Aswr

@Ind_fav
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())