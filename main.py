import assistant

nebula =  assistant.Assistant

statement = ""
while statement == "":
    statement = nebula.listen()