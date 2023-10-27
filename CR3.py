
def even_sum(n):
    '''
       Calculate the sum of even numbers that are less than or equal to n in the Fibonacci sequence.

                Parameters:
                        n (int): A positive integer

                Returns:
                        the sum of the even-valued terms which are smaller than or equal to n 
                        in the Fibonacci sequence.
    '''
    if n <= 0:
        raise ValueError("n must be a positive integer!")

    result = 0
    fibo_seq = [1,1]

    while True:
        next_item = fibo_seq[-2] + fibo_seq[-1]

        # only keep the last 2 items in Fibonacci sequence
        fibo_seq[0], fibo_seq[1] = fibo_seq[1], next_item

        # the next item is even and smaller than or equal to n, add it to the result
        if next_item % 2 == 0 and next_item <= n:
            result += next_item

        if next_item > n:
            break

    return result

print(even_sum(719236))