from mysql.connector import connect
import psutil
import time
import datetime
import platform
import smtplib
import email.message

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

corpo1 = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alerta da Trackware</title>
    </head>
    <body style="
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;">
        <div style="
        max-width: 90%;
        margin: 0 auto;
        padding: 2%;">
            <div style="
                background-color: #6b3e98;
                color: #ffffff;
                text-align: center;
                padding: 3%;">
                <img style="
                max-width: 10%;
                height: auto;
                " src="https://i.imgur.com/NIBLx6a.png" alt="Logotipo da Trackware">
                <h1>Alerta da Trackware</h1>
            </div>
            <div style="
                background-color: #ffffff;
                padding: 3%;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 18px; margin-bottom: 20px;">Prezado Cliente,</p>
                <p style="font-size: 18px; margin-bottom: 20px;">Verificamos que seu dispositivo atingiu 80% de uso da sua CPU agora, """

corpo2 = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alerta da Trackware</title>
    </head>
    <body style="
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;">
        <div style="
        max-width: 90%;
        margin: 0 auto;
        padding: 2%;">
            <div style="
                background-color: #6b3e98;
                color: #ffffff;
                text-align: center;
                padding: 3%;">
                <img style="
                max-width: 10%;
                height: auto;
                " src="https://i.imgur.com/NIBLx6a.png" alt="Logotipo da Trackware">
                <h1>Alerta da Trackware</h1>
            </div>
            <div style="
                background-color: #ffffff;
                padding: 3%;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 18px; margin-bottom: 20px;">Prezado Cliente,</p>
                <p style="font-size: 18px; margin-bottom: 20px;">Verificamos que seu dispositivo atingiu 80% de uso da sua memoria usada agora, """

corpo3 = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alerta da Trackware</title>
    </head>
    <body style="
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;">
        <div style="
        max-width: 90%;
        margin: 0 auto;
        padding: 2%;">
            <div style="
                background-color: #6b3e98;
                color: #ffffff;
                text-align: center;
                padding: 3%;">
                <img style="
                max-width: 10%;
                height: auto;
                " src="https://i.imgur.com/NIBLx6a.png" alt="Logotipo da Trackware">
                <h1>Alerta da Trackware</h1>
            </div>
            <div style="
                background-color: #ffffff;
                padding: 3%;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 18px; margin-bottom: 20px;">Prezado Cliente,</p>
                <p style="font-size: 18px; margin-bottom: 20px;">Verificamos que seu dispositivo atingiu 80% de uso de disco agora, """


def enviar_email(corpo):
    dia = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    end_corpo = dia + """</p>
                <p style="font-size: 18px; margin-bottom: 20px;">Por favor, clique no retangulo abaixo para acessar nosso site e acompanhar o dispositivo.</p>
                <a style="
                display: inline-block;
                background-color: #6b3e98;
                color: #ffffff;
                padding: 2% 4%;
                text-decoration: none;
                border-radius: 5px;" href="#">Acessar Trackware System</a>
            </div>
        </div>
    </body>
    </html>
    """

    
    msg = email.message.Message()
    msg['Subject'] = "Alerta"
    msg['From'] = 'nathanraoliveira@gmail.com'
    msg['To'] = 'alertas-aaaak42km6rgih2za6nkswurre@trackware-workspace.slack.com'
    password = 'empmruelvcjsbreg' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo+end_corpo)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

resposta = (input('Gostaria de começar o monitoramento? ("S" ou "N"): '))
if(resposta == "S" or resposta == "s"):
    maquina = (input('Qual é o id do seu hardware?'))
    
    while(True):
        
        cpu = psutil.cpu_percent()

        mem_used = psutil.virtual_memory()[2]

        disk = psutil.disk_usage('C:\\')[3]

        print("\n- CPU(%):",cpu, "\n- RAM(%):", mem_used, "\n- DISCO(%):", disk)
        
 # -----------------------------------------------------------------------------------------------------------------------------------
 
        info = psutil.disk_partitions()
        dia = datetime.datetime.now()
            
        if(cpu > 80):
            enviar_email(corpo1)
        if(mem_used > 80):
            enviar_email(corpo2)
        if(disk > 80):
            enviar_email(corpo3)
    
        
        connection = mysql_connection('localhost', 'testes', '12345678', 'trackware')

        cpu = str(cpu)
        mem = str(mem_used)
        disk = str(disk)
        maquina = str(maquina)

        c = str(1)
        m = str(2)
        d = str(3)
        query = '''
            INSERT INTO monitoramento(dadoCapturado, fkComponente, fkDispositivo) VALUES
                (
        '''
        
        dados = disk + ',' + d + ',' + maquina + " )"
        dados2 = cpu + ',' + c + ',' + maquina + " )"
        dados3 = mem + ',' + m + ',' + maquina + " )"

        cursor = connection.cursor()
        
        cursor.execute(query+dados)
        connection.commit()
        cursor.execute(query+dados2)
        connection.commit()
        cursor.execute(query+dados3)
        connection.commit()

        time.sleep(5)


connection.close()

