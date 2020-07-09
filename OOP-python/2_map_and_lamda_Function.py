cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    def fibonacci(n):
        if n == 0:
            return [0]
        prev = 0
        cur = 1
        out = [prev, cur]

        for _ in range(n-2):
            prev, cur = cur, prev + cur
            out.append(cur)

        return out

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))