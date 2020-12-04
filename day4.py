#!/usr/bin/env python3
import subprocess
from marshmallow import Schema, fields, validates, EXCLUDE
from marshmallow.validate import OneOf, Range, Regexp, Length
from marshmallow.exceptions import ValidationError


def main1():
    p = subprocess.run("tr ' ' '\n' < inputs/day4.txt", capture_output=True, shell=True)
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    presented_fields = set()
    cnt = 0
    for line in p.stdout.split(b'\n') + [b'']:
        if len(line) == 0:  # separator reached

            score = 0
            for field in presented_fields:
                if field in required_fields:
                    score += 1

            cnt += score >= len(required_fields)
            presented_fields = set()
            continue

        field = line.split(b':')[0].decode()
        presented_fields.add(field)

    print(cnt)


class PassportValidator(Schema):
    byr = fields.Int(required=True, validate=Range(min=1920, max=2002))
    iyr = fields.Int(required=True, validate=Range(min=2010, max=2020))
    eyr = fields.Int(required=True, validate=Range(min=2020, max=2030))
    hgt = fields.Str(required=True)
    hcl = fields.Str(required=True, validate=Regexp("^#[0-9a-f]{6}$"))
    ecl = fields.Str(required=True, validate=OneOf(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']))
    pid = fields.Str(required=True, validate=[Regexp('^[0-9]*$'), Length(equal=9)])

    @validates('hgt')
    def validate_hgt(self, value, **kwargs):
        unit = value[-2:]
        if unit not in ['cm', 'in']:
            raise ValidationError("Unit invalid")

        try:
            v = int(value[:-2])
        except ValueError:
            raise ValidationError("Not a number")

        if unit == 'cm':
            if v < 150 or v > 193:
                raise ValidationError("out of range")
        else:
            if v < 59 or v > 76:
                raise ValidationError("out of range")


def main2():
    p = subprocess.run("tr ' ' '\n' < inputs/day4.txt", capture_output=True, shell=True)
    content_provided = {}
    validator = PassportValidator(many=False, unknown=EXCLUDE)
    cnt = 0
    for line in p.stdout.split(b'\n') + [b'']:
        if len(line) == 0:  # separator reached
            try:
                validator.load(content_provided)
                cnt += 1
            except ValidationError as e:
                pass

            content_provided = {}
            continue

        field_name, field_value = line.decode().split(':')
        content_provided[field_name] = field_value

    print(cnt)


if __name__ == '__main__':
    main2()
