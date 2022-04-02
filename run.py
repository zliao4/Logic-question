
def q1(ans):
    return True

def q2(ans):
    vec = [2, 3, 0, 1]

    return vec[ans[1]] == ans[4]

def q3(ans):
    vec = [ans[2], ans[5], ans[1], ans[3]]
    dif = ans[vec[ans[2]]]
    same = -1
    for i in range(4):
        if i != ans[2]:
            if vec[i] == dif:
                return False
            if same == -1:
                same = vec[i]
            else:
                if same != vec[i]:
                    return False

    return True

def q4(ans):
    vec = [[0, 4], [1, 6], [0, 8], [5, 9]]
    pair = vec[ans[3]]

    return ans[pair[0]] == ans[pair[1]]

def q5(ans):
    vec = [7, 3, 8, 6]

    return ans[4] == ans[vec[ans[4]]]

def q6(ans):
    vec = [[1, 3], [0, 5], [2, 9], [4, 9]]
    pair = vec[ans[5]]

    for n in pair:
        if ans[n] != ans[7]:
            return False

    return True

def q7(ans):
    dic = {0:0, 1:0, 2:0, 3:0}
    for i in ans:
        dic[i] += 1
    
    res = min(list(dic.values()))

    vec = [2, 1, 0, 3]
    for i in dic:
        if dic[i] == res:
            return vec[i] == ans[6]

def q8(ans):
    vec = [6, 4, 1, 9]

    return abs(ans[vec[ans[7]]] - ans[0]) != 1

def q9(ans):
    vec = [5, 9, 1, 8]
    s1 = (ans[0] == ans[5])
    s2 = (ans[vec[ans[8]]] == ans[4])

    return s1 != s2

def q10(ans):
    dic = {0:0, 1:0, 2:0, 3:0}
    for i in ans:
        dic[i] += 1
    
    res = max(list(dic.values())) - min(list(dic.values()))
    vec = [3, 2, 4, 1]

    return res == vec[ans[9]]

if __name__ == "__main__":
    ans = []
    res = []
    letter_chart = ["A", "B", "C", "D"]
    for a1 in range(4):
        for a2 in range(4):
            for a3 in range(4):
                for a4 in range(4):
                    for a5 in range(4):
                        for a6 in range(4):
                            for a7 in range(4):
                                for a8 in range(4):
                                    for a9 in range(4):
                                        for a10 in range(4):
                                            ans = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
                                            s1 = q1(ans)
                                            s2 = q2(ans)
                                            s3 = q3(ans)
                                            s4 = q4(ans)
                                            s5 = q5(ans)
                                            s6 = q6(ans)
                                            s7 = q7(ans)
                                            s8 = q8(ans)
                                            s9 = q9(ans)
                                            s10 = q10(ans)
                                            # print(ans, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
                                            # if ans == [1, 2, 0, 2, 0, 2, 3, 0, 1, 0]:
                                            #     input()

                                            if s1 and s2 and s3 and s4 and s5 and s6 and s7 and s8 and s9 and s10:
                                                for i in ans:
                                                    res.append(letter_chart[i])
    print(res)


    
