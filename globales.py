import gradio as gr

#MAIN
version = "1.0.3"
env = "prod"
aplicacion = "superheroes" #como se llama en tu repo y tu dominio.

seleccion_api = "eligeQuotaOCosto" #eligeQuotaOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/InstantID2", "quota")
api_cost = ("Moibe/InstantID2-B", "costo")
#A o B
api_a = ("Moibe/sampler", "gratis") #Para music-sampler en particular aquí la diferencia será el formato: mp3
api_b = ("Moibe/music-separation", "gratis") #wav
#Gratis o Costo
api_gratis = ("Moibe/image-blend", "gratis")
api_costo = ("Moibe/image-blend", "costo")
process_cost = 25

seto = "splashmix"
work = "picswap"
app_path = "/superheroes" #Muy importante para que cargue bien app.py
server_port=7888
tema = gr.themes.Default()
flag = "auto"
