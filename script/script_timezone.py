from datetime import datetime
from os import system

system('clear')


class PegaDataSistema:

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def ptz():
        print('\nLista Times Zones do Brazil - pytz')
        for zones in (pytz.all_timezones):
            if 'Brazil' in zones:
                print(zones)


PegaDataSistema.ptz()
data = PegaDataSistema.data_hora()
print(f'\n{data}')
