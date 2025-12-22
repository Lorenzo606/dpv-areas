from __future__ import annotations

from typing import Dict, List

# Definiciones de áreas y sus descripciones
area_descripciones_v2: Dict[str, str] = {
    "MESA DE ENTRADAS": """
        Mesa de Entradas gestiona el ingreso inicial de documentación,
        recibe notas y expedientes, registra la fecha de entrada,
        clasifica la información según tipo de trámite, realiza archivo
        y desarchivo, organiza anexos y deriva la documentación a las
        áreas correspondientes.
    """,

    "ADMINISTRACION": """
        Administración gestiona pagos a proveedores, controla facturas
        y comprobantes, ejecuta rendiciones de gastos, administra presupuestos,
        tramita órdenes de pago, revisa liquidaciones y valida servicios
        contratados, incluyendo servicios como Aguas Cordobesas, EPEC, Telecom,
        Gas del Centro, honorarios y materiales.
    """,

    "GESTION FINANCIERA": """
        Gestión Financiera administra el cobro de cuotas a beneficiarios,
        emite cupones y cedulones de pago, gestiona cancelaciones,
        adelantamientos y compensaciones de cuotas, maneja débitos automáticos,
        medios de pago electrónicos, cálculo y actualización de deudas,
        y emisión de certificados de libre deuda.
    """,

    "TECNICA": """
        El área Técnica realiza tareas vinculadas a obras y proyectos:
        revisión y visado de planos, inspecciones en obra, certificación
        de avances, relevamientos técnicos, valuación y depreciación de
        viviendas, informes técnicos de remodelación y construcción,
        coordinación con agrimensores y arquitectos.
    """,

    "REGULARIZACION DOMINIAL": """
        Regularización Dominial gestiona adjudicaciones y readjudicaciones,
        cambios de titularidad, refinanciaciones de deuda, planes de pago,
        regularización de cuotas, contratos, permutas, restituciones,
        situaciones de abandono o desocupación, compra y venta de viviendas,
        y actualización de documentación dominial.
    """,

    "JURIDICO": """
        El área Jurídica interviene en trámites legales: elaboración de dictámenes,
        redacción y revisión de contratos, gestión de recursos administrativos,
        juicios, amparos, pronto despacho, cartas documento, articulación con
        juzgados y asesoramiento legal integral.
    """,

    "ESCRITURACIONES": """
        Escrituraciones tramita la documentación notarial necesaria para entregar
        las escrituras a beneficiarios, gestiona firmas con escribanos, prepara
        documentación registral, coordina ventas con hipoteca, verifica requisitos
        legales para la escrituración y realiza seguimiento del proceso notarial
        hasta la inscripción definitiva.
    """
}

def get_area_labels() -> List[str]:
    return list(area_descripciones_v2.keys())

def build_classification_prompt(asunto_texto: str) -> str:
    instrucciones = """
Eres un sistema de clasificación de trámites internos de una oficina pública.
Tu tarea es leer el asunto de una nota y decidir a qué área debe ser derivada.

Estas son las áreas posibles y una breve descripción de sus funciones:
"""
    for area, desc in area_descripciones_v2.items():
        instrucciones += f"\n- {area}: {desc.strip()}\n"

    instrucciones += f"""
Ahora, dado el siguiente ASUNTO, debes responder SOLO con el nombre exacto de UNA de las áreas listadas arriba,
sin explicaciones adicionales ni texto extra.

ASUNTO:
\"\"\"{asunto_texto}\"\"\"

Respuesta (solo el nombre del área):
"""
    return instrucciones
