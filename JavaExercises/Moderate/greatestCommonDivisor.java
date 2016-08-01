public Integer gdc(Integer p, Integer q) {
    if (q == 0) {
        return p;
    }
    return gdc(q, p % q);
}
