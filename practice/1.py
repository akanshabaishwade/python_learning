x = {1 : 'one', 2: 'two', 3:'three', 'phone': 'samsung', 'laptop':'Dell'}
y = {'one': 1, 'two': 2, 'three': 3}

def main(input_dict):

    x1 = {}
    for anshu in input_dict.items():

        x1[anshu[1]] = anshu[0]
    return x1

if __name__ == '__main__':
    changed_key_dict= main(x)
    print(changed_key_dict)
