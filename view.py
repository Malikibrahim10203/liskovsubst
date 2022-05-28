from pbr import Pbr
from kubus import Kubus

class View:
    
    def show_keliling(self, pbr: Pbr, kubus: Kubus):
        print (kubus.hitung_keliling(pbr))