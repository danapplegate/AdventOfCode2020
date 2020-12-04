def num_valid_passports(passport_iterator, validation_function):
    num_valid = 0
    for passport in passport_iterator:
        if validation_function(passport):
            num_valid += 1
    return num_valid


def passport_parser(line_iterator):
    current_passport = {}
    for line in line_iterator:
        cleaned = line.strip()
        if cleaned == "":
            yield current_passport
            current_passport = {}
        else:
            parse_line(line, current_passport)
    # Apparently, reading the file omits the final, empty line, so
    # we also have to yield the final passport
    yield current_passport


def missing_fields(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return set(required_fields) - set(passport)


def parse_line(line, passport):
    fields = line.split()
    for field in fields:
        field, value = field.split(":")
        passport[field] = value
