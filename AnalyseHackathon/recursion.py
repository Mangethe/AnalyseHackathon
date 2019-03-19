def sum_array(array):

    """Return sum of all items in array
    Args:
        array (array): list or array-like object containing numerical values.

    Returns:
        the sum of all items in array.

    Example(s):
        >>> sum_array(np.array([2, 5, 62, 5, 42, 52, 48, 5]))
        221
    """
    sum_all = 0 #our starting point
    for item in array:
        sum_all = sum_all + item #using the for loop we add each item to the starting point
    return sum_all #return the sum of all items in the given array


def fibonacci(n):

    """Return nth term in fibonacci sequence
    Args:
        n (int): nth term in Fibonacci sequence to calculate

    Returns:
        int: nth term of Fibonacci sequence, equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
        """
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    """Return n!

    Args:
        n (int): number to run through factorial function

    Returns:
        the factorial of a given number using [n! == n(n-1)!].

    Example(s):
        >>> factorial(6)
        720
    """
    if n == 0:
        n_fact = 1 # 0! = 1, since an empty set can only be ordered one way
    else:
        n_fact = n * factorial(n-1) #[n! == n(n-1)! if n!=0]
    return n_fact #returns the factorial of the given value


def reverse(word):
    """Return a given word in reverse'''

    Args:
        word (str): string to be returned in reverse

    Returns:
        string in reverse order.

    Example(s):
        >>> reverse('Nqobile')
        'eliboqN'
        >>> reverse('12345')
        '54321'
    """
    reversed_word = ''
    start = len(word)-1
    stop = -1
    step = -1
    #range --- range(start,stop,step)
    for letter in range(start,stop,step):
        reversed_word  = reversed_word + word[letter]

    return reversed_word #return reversed word
