def add_time(HoraInicial, Duracao, Semana = None):

    DiasSemana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dias = 0 
    Hora = HoraInicial.split()
    AmPm = Hora[1]
    HoraCalculo1 = Hora[0].split(':')
    HoraCalculo2 = Duracao.split(':')
    Minutofinal = int(HoraCalculo1[1]) + int(HoraCalculo2[1])
    if Minutofinal > 59:
        AddHora = Minutofinal // 60
        Minutofinal = Minutofinal % 60
        HoraFinal = int(HoraCalculo1[0]) + int(HoraCalculo2[0]) + AddHora
    else:
        HoraFinal = int(HoraCalculo1[0]) + int(HoraCalculo2[0])
    if AmPm == 'PM':
        HoraFinal += 12

    
        
    dias = HoraFinal//24 
    Horaconvertida = HoraFinal % 24   
    if Horaconvertida > 11:
        AmPm = 'PM'
       
    else:
        AmPm = 'AM'
        

    
    if HoraFinal > 12:
        HoraFinal = HoraFinal % 12
         
    if HoraFinal == 0 and AmPm == 'AM':
        HoraFinal += 12
        
    endTime = str(HoraFinal) + ':' + str(Minutofinal).zfill(2) + ' ' +  AmPm
    if Semana is not None:
        Semana = Semana.lower()
        NumSemana = DiasSemana.index(Semana.title())
        novoNumSemana = (dias + NumSemana) % 7
        nSemana = DiasSemana[novoNumSemana]
        endTime += ', ' + nSemana
        

    if dias == 1:
        endTime += ' (next day)'
    if dias > 1:
        endTime += ' (' + str(dias) + ' days later)'
    return endTime