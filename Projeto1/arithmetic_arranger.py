def arithmetic_arranger(problemas, executar=False):
    problemas_organizados = ''
    if len(problemas) > 5:
        problemas_organizados = "Error: Too many problems."
        return problemas_organizados

    
  
    operadores = list(map(lambda x: x.split()[1], problemas))
    if set(operadores) != {'+','-'}  and len(set(operadores)) != 2 and len(set(operadores)) != 1:
        problemas_organizados = "Error: Operator must be '+' or '-'."
        return problemas_organizados

    num = [] 
    for i in problemas:
        p = i.split()
        num.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), num)):
        problemas_organizados = "Error: Numbers must only contain digits."
        return problemas_organizados

    if not all(map(lambda x: len(x) < 5, num)):
        problemas_organizados = "Error: Numbers cannot be more than four digits."
        return problemas_organizados

    linha1 = ''
    linha2 = ''
    linha3 = ''
    valores = list(map(lambda x: eval(x), problemas))
    respostas = ''
    for i in range(0, len(num), 2):
        espaco = max(len(num[i]), len(num[i+1])) + 2
        linha1 += num[i].rjust(espaco)
        linha3 += '-' * espaco
        respostas += str(valores[i // 2]).rjust(espaco)
        if i != len(num) - 2:
            linha1 += ' ' * 4
            linha3 += ' ' * 4
            respostas += ' ' * 4

    
    for i in range(1, len(num), 2):
        espaco = max(len(num[i - 1]), len(num[i])) + 1
        linha2 += operadores[i // 2]
        linha2 += num[i].rjust(espaco)
        if i != len(num) - 1:
            linha2 += ' ' * 4

    if executar:
        arranged_problems = '\n'.join((linha1, linha2, linha3, respostas))
    else:
        arranged_problems = '\n'.join((linha1, linha2, linha3))
    return arranged_problems