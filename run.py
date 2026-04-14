def Ind_fav(fruit):
    def Aswr():
        pronoun = 'I' if fruit.__name__ == 'mine' else 'You'
        return f"{pronoun} love eating {fruit()}"
    return Aswr

@Ind_fav
def mine():
    return 'Banana'

@Ind_fav
def yours():
    return 'Apple'

print(mine())
print(yours())