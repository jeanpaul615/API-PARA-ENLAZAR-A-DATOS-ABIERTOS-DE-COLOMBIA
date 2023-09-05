from api import API
from ui import interfaz
from ui import filtro_de_datos

if name == 'main':
registers_limit, departament_name = interfaz.menu()
data = API.get_data(registers_limit, departament_name)
filtered_data = filtro_de_datos.filter_columns(data)
print(filtered_data)
