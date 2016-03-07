# print [0, 2, 4, 6, 8]
def print_even_nums(nums):
    arr = []
    for i in nums:
        if i % 2 == 0:
            arr.append(i)

    print(arr)

def print_even_nums_list_comprehension(nums):
    arr = [i for i in nums if i % 2 == 0]
    print(arr)

def without_enumerate(words):
    i = 0
    word_dict = []
    for word in words:
        word_dict.append('%d: %s' % (i, words[i]))
        i += 1
    print(word_dict)

def with_enumerate(words):
    word_dict = ['%d: %s' % (i, words[i]) for i, word in enumerate(words)]
    print(word_dict)

if __name__ == "__main__":
    nums = range(10)
    print(nums)
    print_even_nums(nums)
    print_even_nums_list_comprehension(nums)

    words = ['one', 'two', 'three']
    without_enumerate(words)
    with_enumerate(words)
