import data_generation as dg
import user_interface as ui
import logger as lg
import modul

# dg.start()  # Для создания рандомной базы контактов из N строк раскоменнтировать строку
lg.logging.info('Start')
modul.init_data_base('base_phone.csv')
ui.ls_menu()
