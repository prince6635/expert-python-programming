# !!! based on iterators
# Based on the yield directive, they allow you to pause a function and return an intermediate result.
# The function saves its execution context and can be resumed later if necessary.
def create_generator_without_yield():
    # a shortcut to write simple generators over a sequence with ()
    iter = (x**2 for x in range(10) if x % 2 == 0)
    for it in iter:
        print it

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def test_generators():
    fib = fibonacci()
    print(fib.next())
    print(fib.next())
    print(fib.next())
    results = [fib.next() for i in range(10)]
    print(results)

# generators can also help in breaking the complexity,
# and raising the efficiency of some data transformation algorithms that are based on several suites.
def logic1_power(values):
    for val in values:
        print('powering %s' % val)
        yield val
def logic2_adder(values):
    for val in values:
        print('adding to %s' % val)
        if val % 2 == 0:
            yield val + 3
        else:
            yield val + 2
def all_logics():
    # no need to put all the logic in the same place
    values = [1, 4, 7, 9, 12, 19]
    print(values)
    generator = logic2_adder(logic1_power(values))
    results = [generator.next() for i in range(len(values))]
    print(results)

# generators is the ability to interact with the code called with the next method.
# yield becomes an expression, and a value can be passed along with a new method called send
def psychologist():
    # send acts like next, but makes yield return the value passed.
    # The function can, therefore, change its behavior depending on the client code.
    print 'Print tell me your problems'
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much question.")
            elif 'good' in answer:
                print("A that's good, go on.")
            elif 'bad' in answer:
                print("Don't be so negative.")

def send_to_psychologist():
    gen = psychologist()
    gen.next()
    gen.send("I feel bad")
    gen.send("Why I shouldn't?")
    gen.send("Ok then I should find what is good for me.")

if __name__ == '__main__':
    create_generator_without_yield()
    test_generators()
    all_logics()
    send_to_psychologist()
