IP Calc for Ansible
===========

## Requirements

You need a recent version of ipcalc.
On Debian/Ubuntu you can install it with:

    sudo apt-get install python-pip
    sudo pip install ipcalc

## Installation

Save this file in $ansible/filter_plugins/

## Usage

Example usage in a jinja2 template:

    {% set network = "172.16.0.1/24" | ipcalc %}
    {{ network.host_min }}


    {{ "192.168.0.1" | ipadd(3) }} == "192.168.0.4"
    {{ "fe80::" | ipadd("::3") }} == "fe80::3"
