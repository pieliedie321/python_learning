def maskify(cc):
    if len(cc) > 4:
        z = len(cc) - 4
        x = z*'#' + cc[-4:]
        return x
    elif len(cc) < 4 or len(cc) == 4:
        return cc
