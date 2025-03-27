from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .analisis_nicap import obtener_datos_y_graficos

def analisis_nicap(request):
    tabla_html, grafico_uri = obtener_datos_y_graficos()
    contexto = {
        'tabla': tabla_html,
        'grafico': grafico_uri,
    }
    return render(request, 'analytics/nicap.html', contexto)

def descargar_csv(request):
    df = pd.read_csv('G:/0Proyectos/0portafolio_python/webpersonal/analytics/NICAP/NICAP_data_limpio.csv')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="NICAP_data.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response
