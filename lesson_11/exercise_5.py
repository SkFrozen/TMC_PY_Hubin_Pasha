class SuperStr(str):

    def is_repeatance(self, s):
        if not self:
            return False
        repeat = self * (len(s) // len(self))
        return repeat == s

    def is_palindrom(self):
        if not self:
            return True
        return self == self[::-1]


s = SuperStr("")

print(s.is_repeatance("abcabc"))
print(s.is_palindrom())
