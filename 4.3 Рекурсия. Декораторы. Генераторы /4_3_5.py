def result_accumulator(func):
    results = {}
    def nums(*args, method='accumulate', **kwargs):
        func_name = func.__name__
        if func_name not in results:
            results[func_name] = []
        if method == 'accumulate':
            result = func(*args, **kwargs)
            results[func_name].append(result)
        elif method == 'drop':
            accumulated_results = results[func_name]
            results[func_name] = []
            return accumulated_results
    return nums






