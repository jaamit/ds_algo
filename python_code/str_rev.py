# python string reversed


def str_rev(src_str):
    return src_str[::-1]

src_str = 'hello world'
rev_str = str_rev(src_str)

print(rev_str)
# string are immutable in python so new str is created

hex(id(rev_str))
hex(id(str_rev))

