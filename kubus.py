from pbr import Pbr
from pbr import Hit


class Kubus(Hit):
    
    def hitung_keliling(self, pbr: Pbr)-> float:
        return (12*pbr.get_sisi())