def check_independance(feature_set, new_element):
    # r(A) = |A|
    pass


def twin_greedy(ground_set):
    S = [[], []]
    m = [[], []]

    while True:
        m1, m2 = set(ground_set), set(ground_set)
        # for i in range(ground_set):
        #     if check_independance(S1, ground_set[i]):
        #         S1.append(ground_set[i])
        #     if check_independance(S1, ground_set[i]):
        #         S1.append(ground_set[i])

        if m1 or m2:
            for i in range(2):
                x = None
                if x > 0:
                    S[i].add(x)
        else: break
