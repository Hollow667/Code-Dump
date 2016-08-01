public String getString(List<Integer> list) {
    return list.stream()
    .map(i -> i % 2 == 0 ? "e" + i : "o" + i)
    .collect(joining(","));
}
