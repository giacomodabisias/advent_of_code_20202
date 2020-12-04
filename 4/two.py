from typing import Optional
import re


class Passport:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
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

    def is_valid_byr(self):
        if len(self.byr) != 4:
            return False
        if 1920 <= int(self.byr) <= 2002:
            return True
        else:
            print(f"invalid byr {self.byr}")
            return False

    def is_valid_iyr(self):
        if len(self.iyr) != 4:
            return False
        if 2010 <= int(self.iyr) <= 2020:
            return True
        else:
            print(f"invalid iyr {self.iyr}")
            return False

    def is_valid_eyr(self):
        if len(self.eyr) != 4:
            return False
        if 2020 <= int(self.eyr) <= 2030:
            return True
        else:
            print(f"invalid eyr {self.eyr}")
            return False

    def is_valid_hgt(self):
        unit = self.hgt[len(self.hgt) - 2:len(self.hgt)]
        if unit not in ["cm", "in"]:
            print(f"invalid hgt {self.hgt}")
            return False
        try:
            value = int(self.hgt[:len(self.hgt) - 2])
        except:
            print(f"invalid hgt {self.hgt}")
            return False
        if unit == "cm":
            return 150 <= value <= 193
        elif unit == "in":
            return 59 <= value <= 76
        else:
            raise RuntimeError(f"Can't parse hgt {unit} {value}")

    def is_valid_hcl(self):
        if self.hcl[0] == "#" and len(self.hcl) == 7 and re.match("^[a-z0-9]*$", self.hcl[1:]):
            return True
        else:
            print(f"invalid hcl {self.hcl}")
            return False

    def is_valid_ecl(self):
        if self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        else:
            print(f"invalid ecl {self.ecl}")
            return False

    def is_valid_pid(self):
        if len(self.pid) != 9:
            return False
        try:
            pid = int(self.pid)
            return True
        except:
            print(f"invalid pid {self.pid}")
            return False

    def is_valid(self):
        if self.byr is not None and \
                self.iyr is not None and \
                self.eyr is not None and \
                self.hgt is not None and \
                self.hcl is not None and \
                self.ecl is not None and \
                self.pid is not None and \
                self.is_valid_byr() and \
                self.is_valid_iyr() and \
                self.is_valid_eyr() and \
                self.is_valid_hgt() and \
                self.is_valid_hcl() and \
                self.is_valid_ecl() and \
                self.is_valid_pid():
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
    with open("input_two.txt", "r") as f:
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