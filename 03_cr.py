class CR(object):

    def oftrc(self, fp, d=';'):
        with open(fp, 'r') as f:
            lines = f.readlines()
            lab = lines[0].split(d)
            data = [x.split(d) for x in lines[1:]]
        return lab, data
