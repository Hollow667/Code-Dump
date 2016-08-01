public Boolean packageRice(Integer big, Integer small, Integer goal) {
    boolean result = false;
    if (big * 5 >= goal) {
        if (small >= goal % 5)
            result = true;
    } else {
        if (small >= goal - big * 5) {
            result = true;
        }
    }
    return result;
}
