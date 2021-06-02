name_dict = ['priya', 'suman', 'pooja', 'rani', 'nilu', 'barsha', 'anshu']
quality_dict = ['smart', 'hard_working', 'chatter_box', 'slim', 'burning_woman', 'cute', 'pretty']

def boy(name_dict, quality_dict):
    print("ye dono key and value hai, 1st key and 2ed value")
    n1 = {}


    for girl in range(len(name_dict)):
        print("name_dict ka length nikale h")
        n1[name_dict[girl]] = quality_dict[girl]
        print("ek ek vlaue ko choos kre")
        print(n1, "key aur value loop hoke aare")
        print(girl, "yhe pe count ho ra h ")

        print("==================")


    return n1

    # res = {}
    # for key in name_dict:
    #     print(name_dict)
    #     print("ye key hoga-",key)
    #     print("ye dusre loop se phele quality dict hai-", quality_dict)
    #     for value in quality_dict:
    #         print("andar ke loop me value-", value)
    #
    #         res[key] = value
    #         quality_dict.remove(value)
    #         break
    #     print("ye andar ka loop khatam hone ke bad result dict hai ", res)
    #     print("=========================================")
    # return res

if __name__ == '__main__':
    changed_hello_dict= boy(name_dict, quality_dict)
    print("function se return hua value", changed_hello_dict)
    print(changed_hello_dict)