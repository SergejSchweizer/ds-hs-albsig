


def nansum(a): return sum([x for x in a if not np.isnan(x) ])
def nanmax(a): return max([x for x in a if not np.isnan(x) ])
def nanmin(a): return min([x for x in a if not np.isnan(x) ])


np.sum(a[~np.isnan(a)])  # Eigentlich viel effizienter. 