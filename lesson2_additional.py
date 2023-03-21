# - є функція:
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# функцию pr менять не можно


def replacement_with_spaces(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner



def pr():
    return 'Hello_boss_!!!'


print(' '.join(''.join(pr().split('_'))))

l = ['ggg', 'ggggg']

n = ''.join(l)

print(n)