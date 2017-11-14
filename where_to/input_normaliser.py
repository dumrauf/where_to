class InputNormaliser(object):
    def normalise_string(self, s):
        return s.lower()

    def normalise_list_of_strings(self, lst):
        normalised_list = []
        for item in lst:
            normalisted_item = self.normalise_string(s=item)
            normalised_list.append(normalisted_item)
        return normalised_list
