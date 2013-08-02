from libs.dect.rfp import Dect_Sip_Rfp

__author__ = 'amucci'

dect_connection = Dect_Sip_Rfp('10.150.13.118', 'juan', 'Aastra400')
dect_connection.authorize()
dect_connection.close()