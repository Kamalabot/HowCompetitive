# reviewing generators

# generators are objects that return a value when called with next
# generators are created using functions, that yields a value

import logging

genlog = logging.getLogger('genlog')
genlog.setLevel(logging.INFO)
hndlr = logging.FileHandler(filename='gen.log', mode='w')
hndlr.setLevel(logging.INFO)
genf = logging.Formatter(fmt='%(message)s')
hndlr.setFormatter(genf)
genlog.addHandler(hndlr)


def inf_gen():
    # declare num
    num = 0
    # start a loop
    while True:
        # yield b4 operating
        yield num
        # operate
        num += 1


# loop on generator
for i in inf_gen():
    # log result
    genlog.warning(i)
    if i > 5:
        break

genlog.info(f"New next value of generator after for loop: {next(inf_gen())}")

# if creating an object and assigning it to variable, then we can access next values

genx = inf_gen()

genlog.info(next(genx))
genlog.info(next(genx))
genlog.info(next(genx))
genlog.info(next(genx))
genlog.info(next(genx))
genlog.info(next(genx))

# generators can be created using comprehensions
try_gent = (i for i in 'a very long string')

genlog.info(next(try_gent))
genlog.info(next(try_gent))
genlog.info(next(try_gent))
genlog.info(next(try_gent))
genlog.info(next(try_gent))
genlog.info(next(try_gent))

# there can be multi-yield functions 


def mul_yld():
    # declare first variable 
    var1 = 8
    yield var1  # will yield 8
    # operate on var 1
    var1 += 1
    yield var1  # call to next will yield 9 
    # the generator will stop


mulx = mul_yld()


try:
    genlog.info(next(mulx))
    genlog.info(next(mulx))
    genlog.info(next(mulx))

except Exception:
    genlog.exception('caught stop iteration')

genlog.info("Now moving on to send, throw and close")

# you can modify the variables inside the generator
nexmulx = mul_yld()

try:
    nexmulx.send(25)  # Throws a typeError stating non-None value cannot be sent
except TypeError:
    genlog.info('caught error with send')

genlog.info(next(nexmulx))
# nexmulx.send(25)  # send cannot be used between nexts like so
genlog.info(next(nexmulx))


# create a function that yields "good_value", where the value is a number
def iter_yld():
    # have a marker variable
    num = 0
    # start a loop
    while True:
        yield f"good_"
        # increment marker 
        num += 3
        # if marker above 100
        if num > 1000:
            # break
            break

"""
iter_var = iter_yld()

for i in iter_var:  # Wasn't sure will this work, but it will work
    genlog.info(i)  # expecting good_ 4 times
    iter_var.send(50) # expecting good_ 2 times, as i value is > 10
"""

# making generators to throw error and close is straight forward
new_iter = iter_yld()
genlog.info('new_itr created...')
for ind, i in enumerate(new_iter):
    genlog.info(ind)
    if ind > 50:
        try:
            new_iter.throw(ValueError("enough nexting me..."))
        except ValueError:
            genlog.info('catching thrown error')
        genlog.info('Now this ends')
        new_iter.close()
