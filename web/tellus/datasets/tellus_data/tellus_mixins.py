class generic_mixin():
    def decodedata(self, filebytes):
        """
        The csv can be in UTF-8 or LATIN- 1, 2, or 3 depending on the producing
        machine.

        :param filebytes:
        :return: decoded string
        """
        encodings = ('UTF-8', 'LATIN-1', 'LATIN-2', 'LATIN-3')
        stringdata = None
        for encode in encodings:
            try:
                stringdata = filebytes.decode(encode)
                break
            except UnicodeDecodeError:
                pass
        if not stringdata:
            raise UnicodeDecodeError
        return stringdata
