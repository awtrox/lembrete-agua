from plyer import notification
from threading import Thread
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import platform
import time

running = True
emoji = "\U0001F4A7"


#notificação
def notif():
    while running:
        global emoji
        notification.notify(
            title=f"{emoji}Hora de tomar água!{emoji}",
            message="Bora tomar água e conservar os rins!",
            app_name="Lembrete de Água",
            timeout=10,
        )
        sistema = platform.system()
        if sistema == "Windows":
            import winsound
            winsound.MessageBeep()
        elif sistema == "Linux":
            os.system("canberra-gtk-play -i bell")
        elif sistema == "Darwin":
            os.system("afplay /System/Library/Sounds/Glass.aiff")
        else:
            print("Sistema não reconhecido, não é possível reproduzir o som de notificação.")
        
        time.sleep(timer * 60)

def on_close():
    global running
    running = False
    main.destroy()


#interface
main = tk.Tk()
main.title("Lembrete de Água")
main.geometry("400x100")
main.resizable(False, False)


timer = None
while timer is None:
    main.update_idletasks()
    valor = simpledialog.askstring(
        "Configuração",
        "Digite o intervalo (em minutos) entre as notificações",
        parent=main,
    )
    if valor is None:
        if messagebox.askyesno("Sair", "Você não definiu um intervalo,\n deseja encerrar o programa?"):
            main.destroy()
            exit()
        else:
            continue

    if not valor.isdigit() or not (1 <= int(valor) <=180):
        messagebox.showerror("Erro", "Você precisa digitar um valor entre 1 e  180 minutos!")
    else:
        timer = int(valor)


label = tk.Label(main, text=f"Programa em execução.\n Você receberá uma notificação te lembrando de se hidratar a cada {timer} minuto{"s" if timer !=1 else ""}!", wraplength=350)
label.pack(expand=True)
main.protocol("WM_DELETE_WINDOW", on_close)

Thread(target=notif, daemon=True).start()

main.mainloop()
