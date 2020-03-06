# nome: Vinicius Tertuliano da silva Ra:1901646
# nome: Adalberto gonçalves lira junior RA:1901584

import Func


func_dev_alt = ["Marcílio dos Santos",
                "marcilio@email.com", 5000.00, "DESENVOLVEDOR"]
func_anali_alt = ["Abner", "abner@email.com", 3000.00, "ANALISTA"]
func_geren_alt = ["vinicius ", "vinicius@email.com", 8000.00, "GERENTE"]
func_dev_baix = ["Caique dos Santos", "caique@email.com",
                 2500.00, "DESENVOLVEDOR"]
func_anali_baix = ["amanda", "amanda@email.com", 1400.00, "ANALISTA"]

func_geren_baix = ["cecilia ", "cecilia@email.com", 3600.00, "GERENTE"]


try:
    t = Func.salar(func_dev_alt)
    assert t == 4000
    print('Salário liquido do',
          func_dev_alt[3], func_dev_alt[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 4000)


try:
    t = Func.salar(func_anali_alt)
    assert t == 2250
    print('Salário liquido do',
          func_anali_alt[3], func_anali_alt[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 2250)

try:
    t = Func.salar(func_geren_alt)
    assert t == 5600
    print('Salário liquido do',
          func_geren_alt[3], func_geren_alt[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 5600)


try:
    t = Func.salar(func_dev_baix)
    assert t == 2250
    print('Salário liquido do',
          func_dev_baix[3], func_dev_baix[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 2250)


try:
    t = Func.salar(func_anali_baix)
    assert t == 1190
    print('Salário liquido do',
          func_anali_baix[3], func_anali_baix[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 1190)

try:
    t = Func.salar(func_geren_baix)
    assert t == 2880
    print('Salário liquido do',
          func_geren_baix[3], func_geren_baix[0], 'Esta Correto')
except AssertionError:
    print('Erro')
    print('Retorno:', t)
    print('Esperado', 2880)
