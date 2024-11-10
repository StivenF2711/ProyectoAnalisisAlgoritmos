# ProyectoAnalisisAlgoritmos
 Universidad del Quindío

Programa de Ingeniería de Sistemas y Computación
Proyecto del curso: Algoritmia y bibliometría

Introducción: La bibliometría es una disciplina que permite explorar y analizar volúmenes de datos
derivados de la producción científica. Se fundamenta en las matemáticas y la estadística, para
establecer descripciones, relaciones, inferencias y presentaciones de la información suministrada
por las revistas, los artículos y en general las publicaciones.
Contexto: En el contexto de la bibliometría se pueden identificar diferentes indicadores. Algunos de
ellos se enfocan en la productividad de los autores, índices de impacto, tipologías de producción
académica, países, tópicos según el área de conocimiento, relación visual a partir de diferentes
variables bibliométricas. En el trabajo de (Donthu et al. 2021) se plantean las técnicas de análisis:
análisis de desempeño, mapeo científico y técnicas enriquecidas; cada una de las cuales está
soportada en métodos estadísticos, algoritmos y herramientas.
Dominio: Para el proyecto se plantea un dominio de conocimiento: “computational thinking”.
Fuentes de información: La universidad del Quindío cuenta actualmente con diversas bases de
datos científicas disponibles en: https://library.uniquindio.edu.co/databases, entre las cuales se
identifican: IEEE, SAGE, ScienceDirect, Scopus, Springer, Taylor & Francis. Cada una permite
métodos de consulta, acceso y exportación de información. En este último aspecto, existen los
formatos RIS, BibTex, CSV, texto plano entre otros. Las bases de datos disponibles presentan
diversas tipologías de productividad científica - productos (artículos, conferencias, capítulos de libro,
entre otros). Así mismo, cada base de datos presenta limitantes en cuanto al acceso a la información
y la calidad de los datos.
Propósito: Implementar algoritmos que permitan el análisis bibliométrico y computacional sobre un
dominio de conocimiento particular a partir de las bases de datos disponibles en la Universidad del
Quindío. El desarrollo del proyecto se fundamentará en una serie de requerimientos funcionales que
contemplan la implementación de diversas técnicas bibliométricas y la representación de información
derivada del análisis bibliométrico.
A continuación se hace una descripción de los requerimientos funcionales del proyecto:
Requerimiento 1. Unificar la estructura de la información en una sola fuente de datos, la cual debe
garantizar la completitud de los datos. En esta fuente de información se debe garantizar la existencia
de una sola instancia del producto, es decir, si en una o más bases de datos se identifica un producto
repetido, se debe garantizar un solo registro de este.

Requerimiento 2. Generar estadísticos descriptivos de acuerdo con las siguientes variables: primer
autor del producto (15 autores más citados), año de publicación, tipo de producto (artículos,
conferencias, capítulos de libro), afiliación del primer autor (institución), journal, publisher, base de
datos, cantidad de citaciones por artículo presentadas de manera ordenada (15 artículos más
citados). Todos los anteriores deben estar relacionados ya sea por la cantidad de productos o por el
año. Los descriptivos se podrán consultar desde dos variables: tipo de producto – año, base de datos
- autor, journal – articulo, autor – journals, autor – país.

Requerimiento 3. Dadas las siguientes categorías y sus variables, se debe presentar la frecuencia
de aparición teniendo como fuente el abstract de cada artículo. Es de tener en cuenta que para
algunos casos se tienen palabras que son sinónimos y los cuales deben ser unificados para el
análisis; estos sinónimos se presentarán mediante un guion (-) dentro de la columna denominada
variable.

Categoría Variable
Habilidades Abstraction
Algorithm
Algorithmic thinking
Coding
Collaboration
Cooperation
Creativity
Critical thinking
Debug
Decomposition
Evaluation
Generalization
Logic
Logical thinking
Modularity
Patterns recognition
Problem solving
Programming
Representation
Reuse
Simulation

Conceptos
Computationales

Conditionals
Control structures
Directions
Events
Funtions
Loops
Modular structure
Parallelism
Sequences
Software/hardware
Variables
Actitudes Emotional
Engagement
Motivation
Perceptions
Persistence
Self-efficacy
Self-perceived

Propiedades
psicométricas

Classical Test Theory - CTT
Confirmatory Factor Analysis - CFA
Exploratory Factor Analysis - EFA
Item Response Theory (IRT) - IRT
Reliability
Structural Equation Model - SEM
Validity

Herramienta de
evaluación

Beginners Computational Thinking test - BCTt
Coding Attitudes Survey - ESCAS
Collaborative Computing Observation Instrument
Competent Computational Thinking test - cCTt
Computational thinking skills test - CTST
Computational concepts
Computational Thinking Assessment for Chinese Elementary
Students - CTA-CES
Computational Thinking Challenge - CTC
Computational Thinking Levels Scale - CTLS
Computational Thinking Scale - CTS
Computational Thinking Skill Levels Scale - CTS
Computational Thinking Test - CTt
Computational Thinking Test
Computational Thinking Test for Elementary School Students -
CTT-ES
Computational Thinking Test for Lower Primary - CTtLP
Computational thinking-skill tasks on numbers and arithmetic
Computerized Adaptive Programming Concepts Test - CAPCT
CT Scale - CTS
Elementary Student Coding Attitudes Survey - ESCAS
General self-efficacy scale
ICT competency test
Instrument of computational identity
KBIT fluid intelligence subtest
Mastery of computational concepts Test and an Algorithmic Test
Multidimensional 21st Century Skills Scale
Self-efficacy scale
STEM learning attitude scale - STEM-LAS
The computational thinking scale

Diseño de
investigación

No experimental
Experimental
Longitudinal research
Mixed methods
Post-test
Pre-test
Quasi-experiments

Nivel de
escolaridad

Upper elementary education - Upper elementary school
Primary school - Primary education - Elementary school
Early childhood education – Kindergarten -Preschool
Secondary school - Secondary education
high school - higher education
University – College
Medio Block programming
Mobile application
Pair programming
Plugged activities
Programming

Robotics
Spreadsheet
STEM
Unplugged activities

Estrategia Construct-by-self mind mapping - CBS-MM
Construct-on-scaffold mind mapping - COS-MM
Design-based learning - CTDBL
Design-based learning - DBL
Evidence-centred design approach
Gamification
Reverse engineering pedagogy - REP
Technology-enhanced learning
Collaborative learning
Cooperative learning
Flipped classroom
Game-based learning
Inquiry-based learning
Personalized learning
Problem-based learning
Project-based learning
Universal design for learning

Herramienta Alice
Arduino
Scratch
ScratchJr
Blockly Games
Code.org
Codecombat
CSUnplugged
Robot Turtles
Hello Ruby
Kodable
LightbotJr
KIBO robots
BEE BOT
CUBETTO
Minecraft
Agent Sheets
Mimo
Py– Learn
SpaceChem

Requerimiento 4. Con base en las variables de la anterior tabla, se debe construir una grafica de
palabras clave (algunos autores la denominan nube de palabras) considerando el contenido de los
abstract de todos los artículos almacenados en la base de datos. La nube de palabras se debe
generar dentro de la aplicación o herramienta que está desarrollada. No se permite hacer uso de
otras plataformas.

Requerimiento 5. Se deben identificar los 10 journal con mayor cantidad de artículos publicados y
posteriormente crear una representación gráfica (tipo grafo) que muestre su relación con los artículos
con mayor citación. Para ello, cada journal debe tener vinculado como máximo 15 artículos (los más
citados). Para cada artículo se debe vincular el país del primer autor del artículo. Existe la posibilidad
que no todas las bases de datos tengan el campo del nombre del journal para lo cual pueden usar
el issn. Así mismo, si no se proporciona en todos los casos la cantidad de citaciones del artículo, se
debe crear un valor aleatorio entre 0 y 250. Para el país puede ser que no todas las bases de datos
proporcionen el país de afiliación del primer autor, para lo cual se debe proporcionar una asignación
aleatoria. No se permite hacer uso de otras plataformas para generar la representación gráfica.
Requerimiento 6. El proyecto debe estar desplegado.

Documento final:
El proyecto debe estar soportado en un documento de diseño con la correspondiente arquitectura.
Se debe presentar para cada requerimiento una explicación técnica con detalles de implementación.
El uso de IA debe estar debidamente fundamentado.
Nota: En caso de ser necesario, la presente descripción del proyecto puede ser modificada para
efectos de dar mayor claridad en su especificación.
