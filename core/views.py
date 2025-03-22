# pylint: disable=import-error
"""Vistas principales para el portafolio personal de Ángel."""
from datetime import datetime
import os
import smtplib
from django.shortcuts import render
from analytics.log_stats import get_log_statistics
from django.core.mail import send_mail

# Create your views here.
def home(request):
    """Analytics"""
    stats = get_log_statistics()
    """Registra visitas y envía notificaciones por correo"""
    # Obtener IP del usuario
    ip_address = get_client_ip(request)

    # Obtener datos de última visita
    last_visit = request.session.get("last_visit")
    last_ip = request.session.get("last_ip")

    if last_visit and last_ip == ip_address:
        last_visit_time = datetime.strptime(last_visit, "%Y-%m-%d %H:%M:%S")
        diff = (datetime.now() - last_visit_time).total_seconds() / 60
        if diff < 10:
            return render(request, "core/home.html", {
                "locations": stats["locations"],
                "browsers": stats["browsers"],
            })

    # Enviar correo
    try:
        send_mail(
            "Nueva visita en tu sitio",
            f"Alguien ha visitado tu sitio web.\nIP del visitante: {ip_address}",
            os.getenv("EMAIL_HOST_USER"),
            ["149angel@hotmail.com"],  # Cambia este correo si lo deseas
            fail_silently=False,
        )
    except (smtplib.SMTPException, ConnectionError) as email_error:
        print(f"Error al enviar correo: {email_error}")

    # Actualizar sesión
    request.session["last_visit"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request.session["last_ip"] = ip_address

    return render(request, "core/home.html", {
        "locations": stats["locations"],
        "browsers": stats["browsers"],
    })

def about(request):
    """Vista de la página Acerca de."""
    return render(request, "core/about.html")


def contact(request):
    """Vista de la página de contacto."""
    return render(request, "core/contact.html")

def get_client_ip(request):
    """Intenta obtener la IP real del cliente, incluso si está detrás de un proxy."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip
