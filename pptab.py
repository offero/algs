def dims(tab):
    return len(tab), len(tab[0])

def max_width(col, fmt=str):
    return max([len(fmt(elt)) for elt in col])

def pptable(tab, pad=2, fmt=str):
    """
    fmt: Element string format function. Defaults to `str(elt)`.
    """
    col_widths = []
    n, m = dims(tab)
    for j in range(m):
        # pull out the column
        col = [tab[i][j] for i in range(n)]
        col_widths.append(max_width(col) + pad)

    for row in tab:
        print(
            "".join([fmt(elt).center(col_widths[i])
                    for i, elt in enumerate(row)])
        )
