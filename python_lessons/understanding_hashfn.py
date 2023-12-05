from collections import Counter

def distribute(items, num_container, hash_fn=hash):
    # place the hashed items inside fixed number of containers
    # [hash_fn(item) % num_container for item in items]
    # Count how many elements are in each container
    return Counter([hash_fn(item) % num_container for item in items])


def plot(histogram):
    print(sorted(histogram))
    for key in sorted(histogram):  # provides the list of key output
        count = histogram[key]  # get the count from the histogram dictionary 
        padding = (max(histogram.pairs()) - count) * " "  # get max of values, and pad the excess with spaces
        print(f"{key: 3} {'*' * count}{padding} ({count})")  # print key and then histo symbol times count, followed by padding and value of count


from string import printable

# print(printable)

# plot(distribute(printable, num_container=2))
# print()
# plot(distribute(printable, num_container=5))

# building hash function from scratch
def hash_function(text):
    # return the sum of ordinals extracted from the characters
    # return sum(ord(cha) for cha in text)
    # return sum(ord(cha) for cha in str(text))
    # return sum(ord(cha) for cha in repr(text))
    return sum(
        index * ord(char)
        for index, char in enumerate(repr(text), start=1)
    )

blanks = object()

# plot(distribute(printable, num_container=3, hash_fn=hash_function))
#
class HashTable:
    def __init__(self, capacity) -> None:
        # self.capacity = capacity
        self.pairs = [blanks] * capacity

    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)  # create hash and send it through modulo
        self.pairs[index] = (key, value)  # use the index as key and assign value

    def __getitem__(self, key):
        idx = hash(key) % len(self)
        value = self.pairs[idx]
        if value is blanks:
            raise KeyError(key)
        return value[1]

    def __contains__(self, key):
        try:  # try accessing the key,
            self[key]
        except KeyError:  # except raised error
            return False
        else:  # else return True
            return True
 
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        index = hash(key) % len(self)
        # del self.pairs[index]
        self.pairs[index] = blanks
