import math
ARCHIVO = "envios.txt"

# Funcion creada para recibir el cp y devolver el monto total por pais y su destino
def pais_destino(cp, tipo, forma):
    n = len(cp)
    if n < 4 or n > 9:
        destino = 'Otro'

    else:
        # ¿es Argentina?
        if n == 8:
            if 'A' <= cp[0] <= 'Z' and cp[0] != 'I' and cp[0] != 'O':
                if '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                    if 'A' <= cp[5] <= 'Z' and 'A' <= cp[6] <= 'Z' and 'A' <= cp[7] <= 'Z':
                        destino = 'Argentina'
                    else:
                        destino = 'Otro'
                else:
                    destino = 'Otro'
            else:
                destino = 'Otro'

        else:
            # ¿es Bolivia?
            if n == 4:
                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                    destino = 'Bolivia'
                else:
                    destino = 'Otro'

            else:
                # ¿es Brasil?
                if n == 9:
                    if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                        if '0' <= cp[4] <= '9' and cp[5] == '-':
                            if '0' <= cp[6] <= '9' and '0' <= cp[7] <= '9' and '0' <= cp[8] <= '9':
                                destino = 'Brasil'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'
                    else:
                        destino = 'Otro'

                else:
                    # ¿es Chile?
                    if n == 7:
                        if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                            if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9' and '0' <= cp[6] <= '9':
                                destino = 'Chile'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'
                    else:
                        # ¿es Paraguay?
                        if n == 6:
                            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                                if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9':
                                    destino = 'Paraguay'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'

                        else:
                            # ¿es Uruguay?
                            if n == 5:
                                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9':
                                    if '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                                        destino = 'Uruguay'
                                    else:
                                        destino = 'Otro'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'

    # 2. Determinación de la provincia del lugar de destino.
    if destino == 'Argentina':
        p = cp[0]
        if p == 'A':
            provincia = 'Salta'
        elif p == 'B':
            provincia = 'Buenos Aires'
        elif p == 'C':
            provincia = 'Ciudad Autónoma de Buenos Aires'
        elif p == 'D':
            provincia = 'San Luis'
        elif p == 'E':
            provincia = 'Entre Ríos'
        elif p == 'F':
            provincia = 'La Rioja'
        elif p == 'G':
            provincia = 'Santiago del Estero'
        elif p == 'H':
            provincia = 'Chaco'
        elif p == 'J':
            provincia = 'San Juan'
        elif p == 'K':
            provincia = 'Catamarca'
        elif p == 'L':
            provincia = 'La Pampa'
        elif p == 'M':
            provincia = 'Mendoza'
        elif p == 'N':
            provincia = 'Misiones'
        elif p == 'P':
            provincia = 'Formosa'
        elif p == 'Q':
            provincia = 'Neuquén'
        elif p == 'R':
            provincia = 'Río Negro'
        elif p == 'S':
            provincia = 'Santa Fe'
        elif p == 'T':
            provincia = 'Tucumán'
        elif p == 'U':
            provincia = 'Chubut'
        elif p == 'V':
            provincia = 'Tierra del Fuego'
        elif p == 'W':
            provincia = 'Corrientes'
        elif p == 'X':
            provincia = 'Córdoba'
        elif p == 'Y':
            provincia = 'Jujuy'
        elif p == 'Z':
            provincia = 'Santa Cruz'
        else:
            provincia = 'No aplica'

    else:
        provincia = "No aplica"


    # 3. Determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]
    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # 4. Determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    importe_final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if forma == 1:
        importe_final = int(0.9 * inicial)

    return destino, importe_final, provincia

#Funcion para sacar el salto de linea del final
def linea_sin_salto(linea):
    if linea[-1] == "\n":
        linea = linea[:-1]

    return linea

#Funcion para obtener el tipo de control HC o SC
def obtener_tipo_control(linea):

    #Bandera H
    h = False
    hc = False

    linea_sin_salto(linea)
    for l in linea:
        if l == "H":
            h = True
        elif l == "C" and h == True:
            hc = True

        else:
            h == False

        if hc:
            tipo_control = "Hard Control"
        else:
            tipo_control = "Soft Control"

    return tipo_control

#Funcion que extrae los datos de las lineas
def extraer_datos(linea):
    cod = linea[0:9].strip()
    dir = linea[9:29].strip()
    tipo = int(linea[29])
    forma = int(linea[30])

    return cod, dir, tipo, forma

# Contador de envios internacionales
def contar_envios_internacionales(destino):
    global e_internacionales
    global envios_nacionales

    if destino != 'Argentina':
        e_internacionales += 1
    else:
        envios_nacionales += 1

    return e_internacionales, envios_nacionales

# Porcentaje de envios internacionales sobre el total
def porcentaje_envios(e_internacionales, total_envios):

    promedio = (e_internacionales * 100) / total_envios

    return int(promedio)

# Funcion para calcular el promedio de los envios a bs as
def promedio_bsas(monto_total_bsas, cant_bsas):
    if cant_bsas != 0:
        promedio = monto_total_bsas/cant_bsas

    else:
        promedio = 0
    
    return int(promedio)
    
# Funcion para sacar el punto final de las direcciones
def recorta_direccion(direccion):
    if direccion[-1] == ".":
        direccion = direccion[:-1]
        
    return direccion

# Funcion para definir si la direccion es valida
def validar_direccion(dir):
    caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789"
    #Banderas
    ver = True #Si esta True significa que la palabra es Valida
    
    #Recortar el punto final
    dir = recorta_direccion(dir)

    #contadores
    mayusculas = 0 
        
    for letter in dir:
        if letter != " ":
            if letter == letter.upper():
                mayusculas += 1
            if not letter in caracteres:
                ver = False
                break

        else:
            if mayusculas > 1:
                ver = False
                break
            mayusculas = 0
            
    return ver

# Funcion que recibe el tipo de envio, el monto extra por ser internacional y la forma
def importes_finales(tipoenvio, envios_internacionales, forma):
    precio = 0
    if tipoenvio == 0:
        precio = 1100
    elif tipoenvio == 1:
        precio = 1800
    elif tipoenvio == 2:
        precio = 2450
    elif tipoenvio == 3:
        precio = 8300
    elif tipoenvio == 4:
        precio = 10900
    elif tipoenvio == 5:
        precio = 14300
    else:
        precio = 17900

    if envios_internacionales == 1.20:
        total = precio * 1.20
    elif envios_internacionales == 1.25:
        total = precio * 1.25
    elif envios_internacionales == 1.30:
        total = precio * 1.30
    elif envios_internacionales == 1.50:
        total = precio * 1.50
    else:
        total = precio * 1
        
    
    if forma == 1:
        total = math.trunc(total*0.9)
    else:
        total = math.trunc(total)

    return total

# Calcular la mayor cantidad de cartas
def mayor_cartas(ccs, ccc, cce):
    mayor = None
    if ccs > ccc and ccs > cce:
        mayor = "Carta Simple"
    elif ccc > cce:
        mayor = "Carta Certificada"
    else:
        mayor = "Carta Expresa"

    return mayor

# Funcion para calcular el menor precio pagado en Brasil
def min_brasil_cp(destino,importe_final,CP):
    global min
    global acum_cp
    global acum_cp_rep
    global cont_min
    if destino == "Brasil":
        if min == None or min > importe_final:
            min = importe_final
            acum_cp = CP
            cont_min = 0

        elif min == importe_final:
            if cont_min == 0:
                cont_min += 1
                acum_cp_rep = acum_cp

            elif cont_min >= 1:
                acum_cp = acum_cp_rep

    return min, acum_cp

# Programa principal
def main():

    #Banceras:
    pcpb = False

    #Contadores:
    #Total envios
    total_envios = 0
    #Envios internacionales
    global e_internacionales
    global envios_nacionales
    e_internacionales = 0
    envios_nacionales = 0
    #Monto de envios a Buenos Aires
    monto_total_bsas = 0
    cant_bsas = 0
    #Menor monto Brasil
    global min, acum_cp, acum_cp_rep, cont_min
    min, acum_cp, acum_cp_rep, cont_min = None, 0, 0, 0

    #Envios validos e invalidos
    cedvalid, cedinvalid = 0,0

    #Tipo de carta enviada
    ccs, ccc, cce = 0,0,0

    #Importe de envios totales
    imp_acu_total = 0
    
    #Mayor cantidad de cartas
    tipo_mayor = None

    #Primer codigo postal
    primer_cp = ""

    #Repeticion
    cant_primer_cp = 0
    
    #Paso 1 abrir el archivo
    archivo = open(ARCHIVO, "rt", encoding="utf-8")
    #Paso 2 leer
    linea = archivo.readline()
    linea = linea_sin_salto(linea)
    control = obtener_tipo_control(linea)
    # print(f"Tipo de control {control}")
    #Paso 3 leer contenido de archivo
    linea = archivo.readline()
    while linea != "":
        linea = linea_sin_salto(linea)
        #Paso 4 procesar informacion de la linea
        #Se le aplica laz funcion extraer datos para sacar 4 variables
        cod_pos, dir, tipo, forma = extraer_datos(linea)

        #Destino del envio, monto extra internacional
        destino, pais_destino_monto, provincia = pais_destino(cod_pos, tipo, forma)

        #Contro HC O SC
        if control == "Hard Control":
            #Contar el total de envios
            total_envios += 1
            #Validar direccion
            val_dir = validar_direccion(dir)
            #Si la direccion es valida
            if val_dir:
                # Sumamos los importes para tener el total
                imp_acu_total += pais_destino_monto
                e_internacionales, envios_nacionales = contar_envios_internacionales(destino)
                cedvalid += 1

                # Si es Bs As y tiene direccion valida se suman los montos y cuantas veces hubo Bs As
                if provincia == 'Buenos Aires':
                    monto_total_bsas += pais_destino_monto
                    cant_bsas += 1
                
                # Tipos de cartas enviadas segun el tipo ingresado
                if 0<= tipo <=2:
                    ccs += 1
                elif 3 <= tipo <= 4:
                    ccc += 1
                else: 
                    cce += 1

            else: 
                cedinvalid += 1


        #Si el tipo de control es Soft Control
        else:
            # Suma todos los envios a la variable total_envios
            total_envios += 1
            # Divide los envios en internacionales y nacionales
            e_internacionales, envios_nacionales = contar_envios_internacionales(destino)
            imp_acu_total += pais_destino_monto
            cedvalid += 1

            if provincia == 'Buenos Aires':
                monto_total_bsas += pais_destino_monto
                cant_bsas += 1

            if 0<= tipo <=2:
                ccs += 1
            elif 3 <= tipo <= 4:
                ccc += 1
            else: 
                cce += 1
        
        # Menor importe de Brasil, y su CP
        menimp, mencp = min_brasil_cp(destino,pais_destino_monto,cod_pos)

        #Importes finales
        tipo_mayor = mayor_cartas(ccs, ccc, cce)
        
        #Primer codigo postal y si se repite
        if pcpb == False:
            primer_cp = cod_pos
            pcpb = True
        
        if cod_pos == primer_cp:
            cant_primer_cp += 1

        porc = porcentaje_envios(e_internacionales, total_envios)
        prom = promedio_bsas(monto_total_bsas, cant_bsas)


        linea = archivo.readline()
        

    archivo.close()

    return control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom


control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom = main()


print(' (r1) - Tipo de control de direcciones:', control)
print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
print(' (r4) - Total acumulado de importes finales:', imp_acu_total) 
print(' (r5) - Cantidad de cartas simples:', ccs) 
print(' (r6) - Cantidad de cartas certificadas:', ccc) 
print(' (r7) - Cantidad de cartas expresas:', cce) 
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor) 
print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp) 
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp) 
print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc) 
print('(r14) - Importe final promedio de los envios Buenos Aires:', prom) 