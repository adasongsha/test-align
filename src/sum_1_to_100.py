# 计算1到100的和

def sum_1_to_100():
    total = 0
    for i in range(1, 101):
        total += i
    return total

if __name__ == "__main__":
    result = sum_1_to_100()
    print(f"1到100的和是: {result}")