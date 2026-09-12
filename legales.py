# -*- coding: utf-8 -*-
"""
Los textos legales de reparaciones.net.

QUE ES ESTA WEB, y de esto depende todo lo demas: **un intermediario**. Conecta
a profesionales de varios oficios —fontaneros, electricistas, cerrajeros,
tecnicos de electrodomesticos, pintores, carpinteros...— con particulares que
necesitan una reparacion. NO presta el servicio: lo presta el profesional. Lo
dijo Pedro el 12/09/2026: «no tiene nada que ver con la prevencion».

ESO CAMBIA LAS LEGALES DE ARRIBA ABAJO, y no es un matiz de redaccion:

- En el **aviso legal** hay que decir que el contrato de la reparacion es entre
  el usuario y el profesional, no con el titular de la web. Sin esa clausula,
  el titular responde de trabajos que no ha hecho.
- En la **privacidad** hay DOS grupos de interesados (quien pide el servicio y
  quien lo presta) y, sobre todo, **hay una comunicacion de datos**: para que
  te arreglen el grifo, tu telefono tiene que llegarle al fontanero. Eso hay
  que declararlo; es el tratamiento principal de esta web.

DE DONDE VIENE EL ARMAZON. Se miro `prevencionsiglo21.es`, que es lo que pidio
Pedro. Su politica de privacidad esta al dia (RGPD 2016/679 + LOPDGDD 3/2018) y
de ahi se toma el marco; su aviso legal citaba la **LOPD 15/1999, derogada en
2018**, asi que esa parte NO se copia. Se comprobo tambien el aviso legal de
`curso-tpc.es` (no cita ninguna norma) y el de `prevencionmadrid.es` (solo la
LSSI): **ninguno estaba mejor**, asi que este acaba siendo el mas actual de
todas sus webs.

LOS DATOS DE LA EMPRESA VAN VACIOS, que es lo que pidio Pedro. No se inventa
ninguno: donde falta un dato hay un hueco que lo dice. Un dato inventado en un
aviso legal es peor que uno que falta — el que falta se ve y se arregla.
"""

FALTA = '<p class="vacio"><strong>Pendiente de rellenar:</strong> %s</p>'


AVISO_LEGAL = """
<p>En cumplimiento del artículo 10 de la <strong>Ley 34/2002, de 11 de julio,
de servicios de la sociedad de la información y de comercio electrónico
(LSSICE)</strong>, se exponen a continuación los datos identificativos del
titular de este sitio web.</p>

<h2>Titular del sitio web</h2>
""" + FALTA % ("razón social o nombre, NIF, domicilio, dirección de correo "
               "electrónico, teléfono y, si procede, datos de inscripción en el "
               "Registro Mercantil.") + """

<h2>Qué es este sitio y qué no es</h2>
<p>Reparaciones.net es un <strong>servicio de intermediación</strong>: pone en
contacto a particulares que necesitan una reparación con profesionales
independientes de distintos oficios —fontanería, electricidad, cerrajería,
electrodomésticos, carpintería, pintura, cristalería, persianas, tejados, aire
acondicionado y reformas, entre otros—.</p>
<p><strong>El titular de este sitio no ejecuta los trabajos.</strong> La
reparación la presta el profesional, y el contrato de esa reparación —precio,
plazo, garantía y responsabilidad— se establece <strong>entre el usuario y el
profesional</strong>, sin que el titular sea parte de él.</p>
<p>El titular no responde, por tanto, de la ejecución de los trabajos, de su
resultado ni de los daños que pudieran derivarse de ellos, sin perjuicio de las
responsabilidades que le correspondan como prestador del servicio de
intermediación.</p>

<h2>Obligaciones de los profesionales</h2>
<p>Los profesionales que se dan de alta son responsables de contar con las
autorizaciones, titulaciones, certificados y seguros que exija la normativa de
su actividad, así como de emitir la factura correspondiente. Su alta en este
sitio no supone acreditación ni certificación por parte del titular.</p>

<h2>Uso del sitio</h2>
<p>El acceso a este sitio web es responsabilidad exclusiva de los usuarios y no
supone entablar ninguna relación comercial con el titular.</p>
<p>El acceso y la navegación suponen conocer y aceptar las advertencias legales,
condiciones y términos de uso contenidos en él.</p>
<p>El usuario se compromete a facilitar información veraz y a no utilizar el
sitio con fines ilícitos o que puedan dañar los derechos de terceros.</p>

<h2>Contenidos y disponibilidad</h2>
<p>El titular se reserva el derecho a modificar sin previo aviso la información
de este sitio, así como su configuración y presentación.</p>
<p>No se garantiza la inexistencia de interrupciones o errores en el acceso, si
bien se adoptan las medidas técnicas al alcance para evitarlos.</p>

<h2>Propiedad intelectual e industrial</h2>
<p>Los contenidos de este sitio —textos, imágenes, diseño y código— están
protegidos por la normativa de propiedad intelectual e industrial. Queda
prohibida su reproducción, distribución o transformación sin autorización
expresa del titular.</p>

<h2>Enlaces</h2>
<p>Este sitio puede contener enlaces a páginas de terceros. El titular no se
responsabiliza de sus contenidos ni de sus prácticas de privacidad.</p>

<h2>Protección de datos</h2>
<p>El tratamiento de los datos personales recogidos a través de este sitio se
rige por el <strong>Reglamento (UE) 2016/679 (RGPD)</strong> y por la
<strong>Ley Orgánica 3/2018 (LOPDGDD)</strong>. La información detallada está en
la <a href="/privacidad/">política de protección de datos</a>.</p>

<h2>Legislación aplicable</h2>
<p>Estas condiciones se rigen por la legislación española.</p>
"""


PRIVACIDAD = """
<p>En cumplimiento del <strong>Reglamento (UE) 2016/679 (RGPD)</strong> y de la
<strong>Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos
Personales y garantía de los derechos digitales (LOPDGDD)</strong>, se informa
sobre el tratamiento de los datos personales en este sitio.</p>

<h2>Responsable del tratamiento</h2>
""" + FALTA % ("razón social o nombre, NIF, domicilio, correo electrónico de "
               "contacto y, si procede, datos del Delegado de Protección de "
               "Datos.") + """

<h2>De quién se tratan datos</h2>
<p>Este sitio es un servicio de intermediación, de modo que se tratan datos de
<strong>dos grupos distintos</strong>:</p>
<ul>
  <li><strong>Particulares</strong> que solicitan una reparación: los datos
      necesarios para localizarles y para que el profesional pueda atender el
      aviso.</li>
  <li><strong>Profesionales</strong> que se dan de alta para recibir avisos: sus
      datos identificativos, de contacto, de actividad y los documentos que
      acrediten su habilitación.</li>
</ul>

<h2>Con qué finalidad</h2>
<ul>
  <li><strong>Poner en contacto a ambas partes</strong>: trasladar la solicitud
      al profesional o profesionales adecuados para que puedan atenderla. Ésta
      es la finalidad principal del servicio.</li>
  <li>Atender consultas, solicitudes de información y presupuestos.</li>
  <li>Gestionar el alta y el mantenimiento de los profesionales dados de alta.</li>
  <li>Cumplir las obligaciones legales, fiscales y administrativas exigibles.</li>
</ul>

<h2>A quién se comunican los datos, y esto es lo importante</h2>
<p><strong>Para que el servicio funcione, los datos de contacto y la
descripción del aviso se comunican al profesional</strong> que vaya a atenderlo.
Sin esa comunicación no es posible prestar el servicio: es su razón de ser, y el
usuario la conoce y la acepta al enviar su solicitud.</p>
<p>El profesional trata esos datos como <strong>responsable independiente</strong>
para prestar su servicio y emitir su factura, y responde de ese tratamiento
conforme a su propia política.</p>
<p>Fuera de eso, no se ceden datos a terceros salvo obligación legal o salvo a
los proveedores necesarios para el funcionamiento del sitio, que actúan como
encargados del tratamiento con el contrato correspondiente.</p>

<h2>Base jurídica</h2>
<ul>
  <li><strong>Ejecución de un contrato o medidas precontractuales</strong>
      (art. 6.1.b RGPD): para tramitar la solicitud y ponerla en manos de un
      profesional, y para la relación con los profesionales dados de alta.</li>
  <li><strong>Consentimiento</strong> (art. 6.1.a RGPD): para el envío de
      comunicaciones informativas o comerciales, cuando se preste.</li>
  <li><strong>Cumplimiento de obligaciones legales</strong> (art. 6.1.c RGPD):
      para las obligaciones fiscales y administrativas.</li>
  <li><strong>Interés legítimo</strong> (art. 6.1.f RGPD), cuando proceda y
      previa ponderación.</li>
</ul>

<h2>Durante cuánto tiempo</h2>
<p>Los datos se conservan mientras se mantenga la relación y, después, durante
los plazos legalmente exigidos para atender posibles responsabilidades.</p>

<h2>Qué derechos tiene</h2>
<p>Puede ejercer los derechos de <strong>acceso, rectificación, supresión,
oposición, limitación del tratamiento y portabilidad</strong>, así como retirar
el consentimiento prestado, dirigiéndose al responsable del tratamiento.</p>
""" + FALTA % ("dirección postal o de correo electrónico a la que dirigir el "
               "ejercicio de derechos.") + """
<p>Si considera que sus derechos no han sido atendidos, puede reclamar ante la
<strong>Agencia Española de Protección de Datos</strong>
(<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>

<h2>Seguridad</h2>
<p>Se aplican las medidas técnicas y organizativas necesarias para garantizar la
seguridad de los datos y evitar su alteración, pérdida o acceso no
autorizado.</p>
"""


COOKIES = """
<p><strong>Esta web no utiliza cookies de seguimiento, de analítica ni de
publicidad.</strong> No hay Google Analytics, ni píxeles, ni servicios de
terceros que rastreen su navegación.</p>

<h2>Lo único que se guarda</h2>
<p>Al aceptar el aviso que aparece la primera vez, se guarda en su propio
navegador una marca (<code>galletas-vistas</code>) para no volver a mostrarlo.
Esa marca no sale de su dispositivo, no identifica a nadie, y puede borrarla
vaciando los datos del sitio desde su navegador.</p>
<p>Técnicamente no es una cookie sino almacenamiento local y, por su finalidad,
está exenta de consentimiento. Se informa igualmente por transparencia.</p>

<h2>Si esto cambia</h2>
<p>Si en el futuro se incorpora analítica, publicidad o cualquier otro servicio
de terceros, esta página se actualizará y el aviso dejará de ser informativo
para pasar a <strong>pedir consentimiento antes de cargar nada</strong>.</p>
"""


CONTACTO = FALTA % ("teléfono, dirección de correo electrónico, dirección "
                    "postal y horario de atención.") + """
<p>Tampoco hay todavía formulario de solicitud de avisos ni alta de
profesionales. Cuando se añadan, habrá que revisar la
<a href="/privacidad/">política de protección de datos</a>: son los dos
formularios que recogen los datos de las dos partes.</p>
"""
