
class PixelManager(object):

    def pixel(self, a, b):
        """
        :param a: list of pixels it find black on
        :param b: color to change black pixels
        :return: None
        """
        for item in a:
            if item.R == 0 and item.G == 0 and item.B == 0:
                item.R = b.R
                item.G = b.G
                item.B = b.B