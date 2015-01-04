# https://github.com/digineo/ansible-ipcalc
#
# save this file in $ansible/filter_plugins/
#
# example usage in a jinja2 template:
# {% set network = "172.16.0.1/24" | ipcalc %}
#
# {{ "192.168.0.1" | ipadd(3) }} == "192.168.0.4"
# {{ "fe80::" | ipadd("::3") }} == "fe80::3"
#

import ipcalc

class FilterModule (object):
    def filters(self):
        return {
            "ipcalc": self.ipcalc,
            "ipadd":  self.ipadd,
        }

    def ipcalc(self, value):
        net    = ipcalc.Network(value)
        result = {
            'version'   : net.version(),
            'netmask'   : str(net.netmask()),
            'subnet'    : net.subnet(),
            'size'      : net.size(),
        }

        if net.version() == 6:
            result['network']  = net.network().to_compressed()
            result['host_min'] = net.host_first().to_compressed()
            result['host_max'] = net.host_last().to_compressed()
        if net.version() == 4:
            result['network']   = str(net.network())
            result['host_min']  = str(net.host_first())
            result['host_max']  = str(net.host_last())
            result['broadcast'] = str(net.broadcast())

        return result

    # Add two addresses
    # works for IPv4 and IPv6
    def ipadd(self, one, another):
        version = 6 if (':' in one) else 4
        addr    = ipcalc.IP(ipcalc.IP(one).ip + ipcalc.IP(another).ip, version=version)
        if version == 6:
            return addr.to_compressed()
        else:
            return str(addr)
