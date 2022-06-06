import sys


def pasrse_args(args):
    if all(i.isdigit() for i in args):
        return sum(int(i) for i in args)
    elif all(i.isalpha() for i in args):
        return ",".join(i for i in args)
    else:
        raise (Exception("Enter either all numbers or all letters."))


if __name__ == '__main__':
    print(pasrse_args(sys.argv[1:]))
