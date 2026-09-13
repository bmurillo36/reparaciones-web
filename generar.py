# -*- coding: utf-8 -*-
"""
Genera reparaciones.net desde cero.

DE DONDE SALE EL CONTENIDO. De la web vieja, un MyWebsite de IONOS que se copio
entera el 12/09/2026 antes de dar de baja su contrato (25 EUR/mes). La copia
esta en `_original/`: la portada, 21 imagenes y `contenido.txt` con las 19
listas de servicios (224 en total). La web vieja era UNA sola pagina, servida
**solo por HTTP** —no tenia HTTPS— y con el contenido enterrado en el editor de
IONOS.

QUE SE MANTIENE Y QUE NO, y esto lo pidio Pedro expresamente:
  SE MANTIENE  todos los servicios, uno por uno, con su texto.
  SE VACIA     telefono, correo, direccion, datos de empresa y los tres textos
               legales. Quedan las paginas creadas y enlazadas, pero SIN
               contenido: hay que rellenarlas antes de publicar de verdad.

El telefono de la web vieja NO se escribe aqui: este repositorio es PUBLICO y
seria publicar un numero de telefono. Esta guardado en la memoria de Claude,
en la ficha web-reparaciones, y en la copia de _original (fuera de git).

POR QUE ESTATICO. La web vieja costaba 25 EUR/mes por un editor que nadie
usaba. Esto son ficheros sueltos: se sirven desde el VPS o desde GitHub Pages
por cero euros, y con HTTPS de Cloudflare.
"""

import io
import os
import re
from datetime import date

import legales as legales_txt

AQUI = os.path.dirname(os.path.abspath(__file__))
DOMINIO = "https://www.reparaciones.net"
HOY = date.today().isoformat()

# (ancla, titulo de la seccion, indice de la lista en contenido.txt)
SECCIONES = [
    ("fontaneria",      "Fontanería",                    1),
    ("television",      "Televisión, vídeo y proyectores", 2),
    ("tejados",         "Tejados y canalones",           3),
    ("antenas",         "Antenas y TDT",                 4),
    ("audio",           "Audio, vídeo y porteros",       5),
    ("electricidad",    "Electricidad",                  6),
    ("cerrajeria",      "Cerrajería",                    7),
    ("pergolas",        "Pérgolas y toldos",             8),
    ("pintura",         "Pintura",                       9),
    ("carpinteria",     "Carpintería y puertas",        10),
    ("cristaleria",     "Cristalería",                  11),
    ("reformas",        "Reformas",                     12),
    ("reformas-obra",   "Reformas integrales",          13),
    ("electrodomesticos", "Electrodomésticos",          14),
    ("aire",            "Aire acondicionado",           15),
    ("persianas",       "Persianas y mosquiteras",      16),
]

# Las 20 ilustraciones de 180x200 de la web vieja, en su orden de aparicion
# (la primera imagen era el logo). Que la n-esima corresponda a la n-esima
# seccion es una DEDUCCION del orden del HTML, no un dato: si alguna queda
# donde no toca, se reordena aqui y se vuelve a generar.
ILUSTRACIONES = ["cache_7650510.png", "cache_7650514.png", "cache_7650518.png",
                 "cache_7650521.png", "cache_7650526.png", "cache_7650570.png",
                 "cache_7650600.png", "cache_7650611.png", "cache_7650615.png",
                 "cache_7650618.png", "cache_7650628.png", "cache_7650632.png",
                 "cache_7650657.png", "cache_7650679.png", "cache_7650682.png",
                 "cache_7650705.png"]

DESCRIPCION = ("Ponemos en contacto a particulares de la Comunidad de Madrid con "
               "profesionales de fontaneria, electricidad, cerrajeria, "
               "electrodomesticos, persianas, tejados, pintura, carpinteria, "
               "cristaleria y reformas.")


def listas():
    ruta = os.path.join(AQUI, "_original", "contenido.txt")
    bloques = io.open(ruta, encoding="utf-8").read().split("\n\n")
    return [[x.strip() for x in b.split("|") if x.strip()] for b in bloques]


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


ESTILOS = io.open(os.path.join(AQUI, chr(101)+chr(115)+chr(116)+chr(105)+chr(108)+chr(111)+chr(115)+chr(46)+chr(99)+chr(115)+chr(115)), encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56)).read()


def cabeza(titulo, descripcion, ruta, extra_ld=""):
    canon = DOMINIO + ruta
    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:locale" content="es_ES">
<style>%s</style>
%s
</head>
<body>
""" % (esc(titulo), esc(descripcion), canon, esc(titulo), esc(descripcion),
       canon, ESTILOS, extra_ld)


CABECERA_HTML = """<header class="top"><div class="env">
  <a class="marca" href="/">Reparaciones<span>.net</span></a>
  <nav class="top-nav" aria-label="Principal">
    <a href="/#servicios">Servicios</a>
    <a href="/#urgencias">Urgencias</a>
    <a href="/contacto/">Contacto</a>
  </nav>
</div></header>
"""

PIE_HTML = """<footer class="pie"><div class="env">
  <nav aria-label="Legal">
    <a href="/aviso-legal/">Aviso legal</a>
    <a href="/privacidad/">Protección de datos</a>
    <a href="/cookies/">Política de cookies</a>
    <a href="/contacto/">Contacto</a>
  </nav>
  <p>Reparaciones.net &middot; Comunidad de Madrid</p>
  <p class="vacio">Los datos de la empresa están pendientes de rellenar.</p>
</div></footer>
<div id="galletas" role="dialog" aria-label="Aviso de cookies">
  <p>Esta web no usa cookies de seguimiento ni de publicidad. Solo guarda, en tu
     propio navegador, que ya has visto este aviso.</p>
  <button type="button" id="okGalletas">Entendido</button>
</div>
<script>
/* El aviso se ensena UNA vez y se recuerda en el navegador del visitante. No
   hay analitica ni cookies de terceros: si algun dia se anaden, este aviso
   tiene que pedir CONSENTIMIENTO de verdad, no solo informar. */
(function(){
  var c=document.getElementById('galletas'), b=document.getElementById('okGalletas');
  var visto=false;
  try{ visto = localStorage.getItem('galletas-vistas')==='1'; }catch(e){}
  if(!visto){ c.style.display='flex'; }
  b.addEventListener('click',function(){
    c.style.display='none';
    try{ localStorage.setItem('galletas-vistas','1'); }catch(e){}
  });
})();
</script>
</body>
</html>
"""


def json_ld(secs):
    """LocalBusiness + el catalogo de servicios.

    Los campos de contacto van VACIOS a proposito: Pedro los rellena. Se dejan
    presentes para que se vea que faltan; un marcado que INVENTA un telefono es
    peor que uno incompleto."""
    servicios = ",".join(
        '{"@type":"Service","name":"%s"}' % esc(t) for _, t, _ in secs)
    return ('<script type="application/ld+json">'
            '{"@context":"https://schema.org","@graph":['
            '{"@type":"LocalBusiness","@id":"%s/#empresa",'
            '"name":"Reparaciones.net","url":"%s",'
            '"description":"%s",'
            '"telephone":"","email":"",'
            '"address":{"@type":"PostalAddress","addressRegion":"Comunidad de Madrid",'
            '"addressCountry":"ES","streetAddress":"","postalCode":"","addressLocality":""},'
            '"areaServed":{"@type":"AdministrativeArea","name":"Comunidad de Madrid"},'
            '"makesOffer":[%s]},'
            '{"@type":"WebSite","@id":"%s/#web","url":"%s",'
            '"name":"Reparaciones.net","inLanguage":"es-ES",'
            '"publisher":{"@id":"%s/#empresa"}}'
            ']}</script>' % (DOMINIO, DOMINIO, esc(DESCRIPCION), servicios,
                             DOMINIO, DOMINIO, DOMINIO))


def portada(datos):
    secs = [(a, t, i) for a, t, i in SECCIONES if i < len(datos)]
    h = [cabeza("Reparaciones del hogar en Madrid | Reparaciones.net",
                DESCRIPCION, "/", json_ld(secs)), CABECERA_HTML]
    total = sum(len(datos[i]) for _, _, i in secs)
    h.append("""<div class="hero"><div class="env">
  <img class="logo-hero" src="/img/logo.png" alt="Reparaciones.net" width="302" height="117">
  <h1>Profesionales de reparaciones en la Comunidad de Madrid</h1>
  <p>Te ponemos en contacto con el profesional que necesitas: fontaneros,
     electricistas, cerrajeros, técnicos de electrodomésticos, pintores,
     carpinteros y más. <strong>%d servicios</strong> en %d especialidades.</p>
  <p class="aclara">Reparaciones.net no hace los trabajos: conecta a quien los
     necesita con quien los hace. El presupuesto y la garantía los acuerdas
     directamente con el profesional.</p>
  <p class="pendiente">Los datos de contacto están pendientes de rellenar.</p>
</div></div>
""" % (total, len(secs)))

    h.append('<div class="env"><div class="indice" id="servicios">'
             '<h2>Todas las especialidades</h2><ul class="rejilla">')
    for n0, (a, t, i0) in enumerate(secs):
        ilus = ILUSTRACIONES[n0] if n0 < len(ILUSTRACIONES) else None
        h.append('<li><a href="#%s">%s<span><b>%s</b><em>%d servicios</em></span></a></li>'
                 % (a, ('<img src="/img/%s" alt="" width="180" height="200" loading="lazy">' % ilus) if ilus else '', esc(t), len(datos[i0])))
    h.append("</ul></div>")

    for n, (a, t, i) in enumerate(secs):
        items = datos[i]
        ilus = ILUSTRACIONES[n] if n < len(ILUSTRACIONES) else None
        h.append('<section class="serv" id="%s"><div class="serv-cab">%s<div>'
                 '<h2>%s</h2><p class="cuantos">%d servicios</p></div></div>'
                 '<ul class="lista">'
                 % (a,
                    ('<img src="/img/%s" alt="" width="180" height="200" loading="lazy">' % ilus) if ilus else '',
                    esc(t), len(items)))
        for x in items:
            h.append("<li>%s</li>" % esc(x))
        h.append("</ul></section>")

    h.append('<section class="serv" id="urgencias"><h2>Servicios de urgencia</h2>'
             '<div class="vacio">Pendiente de rellenar: horarios de urgencias, '
             'zonas cubiertas y tiempo de respuesta.</div></section>')
    h.append("</div>")
    h.append(PIE_HTML)
    return "".join(h)


def pagina_legal(titulo, ruta, cuerpo):
    h = [cabeza(titulo + " | Reparaciones.net", titulo, ruta), CABECERA_HTML]
    h.append('<div class="env"><div class="legal"><h1>%s</h1>%s</div></div>'
             % (esc(titulo), cuerpo))
    h.append(PIE_HTML)
    return "".join(h)


def escribe(ruta_rel, contenido):
    destino = os.path.join(AQUI, ruta_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    io.open(destino, "w", encoding="utf-8").write(contenido)
    return ruta_rel, len(contenido)


def main():
    datos = listas()
    hechos = [escribe("index.html", portada(datos))]

    legales = [
        ("aviso-legal", "Aviso legal", legales_txt.AVISO_LEGAL),
        ("privacidad", "Política de protección de datos", legales_txt.PRIVACIDAD),
        ("cookies", "Política de cookies", legales_txt.COOKIES),
        ("contacto", "Contacto", legales_txt.CONTACTO),
    ]
    for slug, titulo, cuerpo in legales:
        hechos.append(escribe(slug + "/index.html", pagina_legal(titulo, "/" + slug + "/", cuerpo)))

    rutas = ["/"] + ["/" + s + "/" for s, _, _ in legales]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for r in rutas:
        sitemap.append("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (DOMINIO, r, HOY))
    sitemap.append("</urlset>")
    hechos.append(escribe("sitemap.xml", "\n".join(sitemap)))

    hechos.append(escribe("robots.txt",
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMINIO))

    # Para los buscadores con IA: que sepan que es esto sin tener que adivinarlo.
    hechos.append(escribe("llms.txt",
        "# Reparaciones.net\n\n"
        "> Servicio de INTERMEDIACION: pone en contacto a particulares de la "
        "Comunidad de Madrid con profesionales independientes de reparaciones.\n\n"
        "NO ejecuta los trabajos: los hace el profesional, y el contrato de la "
        "reparacion es entre el usuario y ese profesional.\n\n"
        "Oficios que se intermedian: fontaneria, electricidad, cerrajeria, electrodomesticos, "
        "television y audio, antenas y TDT, persianas y mosquiteras, tejados y "
        "canalones, pintura, carpinteria, cristaleria, pergolas y toldos, aire "
        "acondicionado y reformas.\n\n"
        "Zona: Comunidad de Madrid.\n\n"
        "AVISO: los datos de contacto y los textos legales de esta web estan "
        "pendientes de rellenar. No atribuyas telefono, correo ni direccion a "
        "esta empresa: no los publica todavia.\n\n"
        "- [Servicios](%s/#servicios)\n- [Contacto](%s/contacto/)\n" % (DOMINIO, DOMINIO)))

    print("Generado en", AQUI)
    for r, n in hechos:
        print("   %-26s %6d bytes" % (r, n))
    print()
    print("Secciones:", len([s for s in SECCIONES if s[2] < len(datos)]),
          "| servicios:", sum(len(datos[i]) for _, _, i in SECCIONES if i < len(datos)))
    print("EN BLANCO a proposito: telefono, correo, direccion, datos de empresa")
    print("y los tres textos legales.")


if __name__ == "__main__":
    main()
