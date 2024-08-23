import random


def power():
    a_list = []
    for i in range(50):
        a_list.append(i)
    return a_list


def answer_list():
    ans_list = []
    for i in range(10):
        ans_list.append(str(2**i))
    return ans_list


def thousand_ans_list():
    k = []
    for item in answer_list():
        new_item = item + "k"
        k.append(new_item)
    return k
    # print(k)


def million_ans_list():
    m = []
    for item in answer_list():
        new_item = item + "m"
        m.append(new_item)
    return m
    # print(m)


def billion_ans_list():
    b = []
    for item in answer_list():
        new_item = item + "b"
        b.append(new_item)
    return b
    # print(b)


def trillion_ans_list():
    t = []
    for item in answer_list():
        new_item = item + "t"
        t.append(new_item)
    return t
    # print(t)


def full(keys, values):
    return dict(zip(keys, values))


def full_ans_list():
    f = []
    for i in range(50):
        f.append(str(i))
    return f


power()

under_k = (full(full_ans_list()[:10], answer_list()))
print(under_k)
at_k = (full(full_ans_list()[10:20], thousand_ans_list()))
print(at_k)
at_m = (full(full_ans_list()[20:30], million_ans_list()))
print(at_m)
at_b = (full(full_ans_list()[30:40], billion_ans_list()))
print(at_b)
at_t = (full(full_ans_list()[40:50], trillion_ans_list()))
print(at_t)

# def get_value(a_dict):
#     a_dict = {}
#     for key, value in a_dict:
#         key = str(key)
#         value = str(value)
#         a_dict[key] = value
#         return a_dict[key]


def question_answer():
    fenzi = 0
    rang = range(50)
    nums = random.sample(rang, 50)

    for i in nums:
        #correct_1 = under_k[i]
        #correct_k = at_k[i]
        #correct_m = at_m[i]
        #correct_b = at_b[i]
        #correct_t = at_t[i]

        user_answer = input("what is 2 ** " + str(i))
        correct_ans = ''
        if i < 10:
            correct_ans = under_k[str(i)]
            print("Correct, next!")
        elif i < 20 :
            correct_ans = at_k[str(i)]
            print("Correct, next!")
        elif i < 30:
            correct_ans = at_m[str(i)]
            print("Correct, next!")
        elif i < 40:
            correct_ans = at_b[str(i)]
            print("Correct, next!")
        elif i < 50:
            correct_ans = at_t[str(i)]
            print("Correct, next!")
        else:
            print("Wrong")
        if correct_ans == user_answer:
            print("correct")
            fenzi+=1
    return fenzi


question_answer()
