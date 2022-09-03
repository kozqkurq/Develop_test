def make_judge(grade, points):
    result = None
    counter = 0

    # 成績による判定
    if grade in ["A", "B", "C"]:
        result = 1
    elif grade == "D":
        result = 2
    elif grade == "E":
        result = 3

    # 点数による判定
    for point in points:
        # 10点未満が存在する場合
        if point < 10 :
            result = 3
            break

        # 30点以下が3つ以上存在する場合
        elif point <= 30:
            counter += 1
            if counter >= 3:
                result = 2

    # # 点数による判定(集合)
    # set10 = {i for i in range(1,10)}
    # set30 = {i for i in range(10, 31)}
    # # 10点未満が存在する場合
    # if set10.isdisjoint(set(points)):
    #     result = 3
    # # 30点以下が3つ以上存在する場合
    # elif set30.isdisjoint(set(points)):
    #     if len(set30 & set(points)) >= 3:
    #         result = 2

    return result