spam = ['apple','bananas','tofu','cat']
def cooma(spam):
    lenth = len(spam)
    for index,item in enumerate(spam):
        if index == lenth-1:
            print(f'and {item}')
        else:
            print(f"{item}",end=', ')

cooma(spam)