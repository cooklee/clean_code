
class PixelMenager(object):

    def Pixel(self, a, b):
        for item in a:
            if item.R == 0 and item.G == 0 and item.B == 0:
                item.R = b.R
                item.G = b.G
                item.B = b.B


class CustomerAccount(object):

    def __init__(self ):
        self.str_name_of_account_define_by_customer = ''
        self.str_name_of_account_define_by_corporation = ''

    def add_information_by_customer(self, data):
        self.str_name_of_account_define_by_customer = data

    def name_by_corporation(self, name):
        """

        :param name:
        :return:
        """
        return self.str_name_of_account_define_by_corporation


class CR(object):

    def oftrc(self, fp, d=';'):
        with open(fp, 'r') as f:
            lines = f.readlines()
            lab = lines[0].split(d)
            data = [x.split(d) for x in lines[1:]]
        return lab, data



