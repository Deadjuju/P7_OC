import time


def execution_time(funct):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        funct(*args, **kwargs)
        end_time = time.time()
        print(f"EXECUTION: {(end_time - start_time):.3f}s\n")

        return funct(*args)
    return wrapper
