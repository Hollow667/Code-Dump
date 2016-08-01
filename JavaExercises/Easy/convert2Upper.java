public List<String> upperCase(List<String> list) {
    return list.stream()
        .map(String::toUpperCase)
        .collect(Collectors.toList());
}
