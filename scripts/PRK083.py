completion = []
completion.append(('11','60', '01', '1.0', '*OPEN'))
completion.append(('11','60', '02', '1.0', '*OPEN'))
completion.append(('11','60', '03', '1.0', '*OPEN'))
completion.append(('11','60', '04', '1.0', '*OPEN'))
completion.append(('11','60', '05', '1.0', '*OPEN'))
completion.append(('11','60', '06', '1.0', '*OPEN'))
completion.append(('11','60', '07', '1.0', '*OPEN'))
completion.append(('11','60', '08', '1.0', '*OPEN'))
completion.append(('11','60', '09', '1.0', '*CLOSED'))
completion.append(('11','60', '10', '1.0', '*CLOSED'))
completion.append(('11','60', '11', '1.0', '*OPEN'))
completion.append(('11','60', '12', '1.0', '*OPEN'))
completion.append(('11','60', '13', '1.0', '*OPEN'))
completion.append(('11','60', '14', '1.0', '*OPEN'))
completion.append(('11','60', '15', '1.0', '*OPEN'))
completion.append(('11','60', '16', '1.0', '*OPEN'))
completion.append(('11','60', '17', '1.0', '*CLOSED'))
completion.append(('11','60', '18', '1.0', '*CLOSED'))
completion.append(('11','60', '19', '1.0', '*OPEN'))
completion.append(('11','60', '20', '1.0', '*OPEN'))
completion.append(('11','60', '21', '1.0', '*OPEN'))
completion.append(('11','60', '22', '1.0', '*OPEN'))
completion.append(('11','60', '23', '1.0', '*OPEN'))
completion.append(('11','60', '24', '1.0', '*OPEN'))
completion.append(('11','60', '25', '1.0', '*OPEN'))
completion.append(('11','60', '26', '1.0', '*OPEN'))
completion.append(('11','60', '27', '1.0', '*OPEN'))
completion.append(('11','60', '28', '1.0', '*OPEN'))
completion.append(('11','60', '29', '1.0', '*OPEN'))
completion.append(('11','60', '30', '1.0', '*OPEN'))

layerclump = []
layerclump.append('11 60 01:08')
layerclump.append('11 60 11:16')
layerclump.append('11 60 19:30')

operate = []
operate.append(('*MAX','*STL',3000.0,'*CONT *REPEAT'))
operate.append(('*MIN','*BHP', 295.0,'*CONT *REPEAT'))

monitor = []
monitor.append(('*WCUT', 0.95, '*SHUTIN'))

group = 'PRODUCTION'

geometry = ('*K', 0.108, 0.370, 1.0, 0.0)

perf = '*GEOA'

openn = 1431

on_time = 1.0

icv_nr = 3

icv_start = (2008, 183, 200)

icv_control = [(('*ON_CTRLLUMP __LAYER__ *GOR > 750','AND','*ON_CTRLLUMP _LAYER_ *GOR < 1250',0.0),('*ON_CTRLLUMP __LAYER__ *WCUT > 0.95',0.0))]*icv_nr