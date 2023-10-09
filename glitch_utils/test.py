from numpy import array
from auto_lgr import auto_log_factory, set_flags

set_flags(debug=False)


@auto_log_factory(["numpy"])
def main():
    d = array([1, 2])
    d.max()
    x = 15
    print(x)


if __name__ == "__main__":
    main()
