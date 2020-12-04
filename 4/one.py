from typing import Optional


class Passport:
    byr: Optional[int] = None
    iyr: Optional[int] = None
    eyr: Optional[int] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[int] = None
    cid: Optional[str] = None

    def __repr__(self):
        representation = "\n"
        if self.byr is not None:
            representation += f"byr {self.byr} \n"
        if self.iyr is not None:
            representation += f"iyr {self.iyr} \n"
        if self.eyr is not None:
            representation += f"eyr {self.eyr} \n"
        if self.hcl is not None:
            representation += f"hcl {self.hcl} \n"
        if self.hgt is not None:
            representation += f"hgt {self.hcl} \n"
        if self.ecl is not None:
            representation += f"ecl {self.ecl} \n"
        if self.pid is not None:
            representation += f"pid {self.pid} \n"
        if self.cid is not None:
            representation += f"cid {self.cid} \n"
        return representation

    def is_valid(self):
        if self.byr is not None and \
                self.iyr is not None and \
                self.eyr is not None and \
                self.hgt is not None and \
                self.hcl is not None and \
                self.ecl is not None and \
                self.pid is not None:
            return True
        else:
            return False


def create_passport(lines):
    passport = Passport()
    for line in lines:
        fields = line.split(" ")
        for field in fields:
            k, v = field.split(":")
            setattr(passport, k, v)

    return passport


def read_input():
    passports = []
    with open("input_one.txt", "r") as f:
        lines = f.readlines()
    passport_lines = []
    for line in lines:
        if line == "\n":
            passport = create_passport(passport_lines)
            passports.append(passport)
            passport_lines = []
        else:
            line = line.strip()
            passport_lines.append(line)
    passport = create_passport(passport_lines)
    passports.append(passport)
    return passports


def main():
    passports = read_input()
    valid_passports = 0
    for passport in passports:
        if passport.is_valid():
            valid_passports += 1

    print(valid_passports)

if __name__ == "__main__":
    main()