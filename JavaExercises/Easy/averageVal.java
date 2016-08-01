public Double average(List<Integer> list) {
    return list.stream()
        .mapToInt(i -> i)
        .average()
        .getAsDouble();
}
