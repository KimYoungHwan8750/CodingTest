
def min_common_multiple(value):
    result = {
        2:0,
        3:0
    }
    def multiple(value,result):
        if value == 1:
            return
        if value % 2 == 0:
            value = value/2
            result[2] += 1
            multiple(value, result)
        elif value % 3 == 0:
            value = value/3
            result[3] += 1
            multiple(value, result)
        else:
            if result.get(value):
                result[value] += 1
            else:
                result[int(value)] = 0
                result[value] += 1
        return result

    return multiple(value, result)

print(min_common_multiple(13))
print(min_common_multiple(17))
