Big-Data-Technologien
Databricks

Prof. Dr. Suat Can | Sommersemester 2025

Databricks
Literatur

Die folgende Übung entstammt in Teilen dem Buch von :

§ Ilijason, Robert (2020): Beginning Apache Spark Using
Azure Databricks: Unleashing Large Cluster Analytics
in the Cloud. Apress.

Als eBook in der HsH Bibliothek erhältlich

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 634

Einführung in Databricks

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 635

Einführung in Databricks
Wo befinden wir uns?

https://towardsdatascience.com/scalable-efficient-big-data-analytics-machine-learning-pipeline-architecture-on-cloud-4d59efc092b5, aufgerufen am 16.05.2024

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 636

Einführung in Databricks
Azure IoT Hub vs. Event Hub

•

IoT Hub ist speziell für IoT-Szenarien gebaut – mit Geräteverwaltung und Zwei-Wege-
Kommunikation.

• Event Hub ist eine generische Event-Streaming-Plattform, ähnlich wie Apache Kafka, aber nicht

für Geräte gedacht, sondern für den massiven Dateneingang.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 637

Einführung in Databricks
Data Science und ML-Plattform

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 638

Einführung in Databricks
Einführung

Databricks

- Sie hat seinen Ursprung im akademischen Umfeld und in der Open-Source-Community
und wurde 2013 von den Originalentwicklern von Apache Spark™, Delta Lake und
MLflow gegründet.

- Als weltweit erste und einzige Lakehouse-Plattform in der Cloud kombiniert Databricks
das Beste aus Data Warehouses und Data Lakes und stellt eine offene und einheitliche
Plattform für Daten und KI zur Verfügung.

§ Entstand aus dem Projekt AMPLab der University of California, Berkeley.

§ Matei Zaharia war 2013 Mitgründer von Databricks (Apache Spark)

§ Ist bekannt für seine Lakehouse-Plattform und den Open-Source Systemen Spark, Delta Lake und

MLflow

§ Bietet Plattformen in der Cloud an (als PaaS und SaaS)

§ Setzt auf die bekannten Hyperscaler auf (AWS, Azure, GCP)

https://www.databricks.com/de/company/about-us, aufgerufen am 22.05.2024

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 639

Einführung in Databricks
Apache Spark

Apache Spark ist ein einheitliches In-Memory Big-Data-System,
was für die Verarbeitung von enormen Datenmengen geeignet ist:

§ Durch die verteilte Architektur in einem Cluster kann Spark

extrem große Datenmengen performant und parallel verarbeiten.

§ Spark verarbeitet die Daten im Arbeitsspeicher und versucht das

Schreiben auf eine Festplatte zu vermeiden.

§ Die gute Integration von vielen Machine Learning Algorithmen,
ermöglicht analytische Modelle auf Big-Data mit Apache Spark
anzuwenden.

§ Spark oft als Schweizer Taschenmesser der Big Data

Datenverarbeitung bezeichnet.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 640

Anlehnung an Albrecht (2017), Zaharia et al. (2010) sowie Freiknecht und Papp (2018)

/

h
t
t
p
s
:
/
/
d
1
.
a
w
s
s
t
a
t
i
c
.
c
o
m
D
a
t
a
%
2
0
L
a
k
e
/
w
h
a
t
-
i
s
-
a
p
a
c
h
e
-
s
p
a
r
k
.
b
3
a
3
0
9
9
2
9
6
9
3
6
d
f
5
9
5
d
9
a
7
d
3
6
1
0
f
1
a
7
7
f
f
0
7
4
9
d

f
.

P
N
G

,

a
u
f
g
e
r
u
f
e
n

a
m
0
1

.

0
4

.

2
0
2
4

Einführung in Databricks
Video: What is Apache Spark?

https://www.youtube.com/watch?v=p8FGC49N-zM

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 641

Einführung in Databricks
Delta Lake

§ Eine Speicherschicht, die auf einen Data Lake aufsetzt und die Grundlage für

jedes Lakehouse bildet.

§ Sie unterstützt sowohl die Batch-Datenverarbeitung als auch ACID-
Transaktionen, skalierbare Metadaten und Unified Streaming.

§ So lässt sich ein Data Lake einerseits mit den Vorteilen eines Data Warehouse

ausstatten.

§ Andererseits können Daten in Echtzeit verarbeitet und analysiert werden.

§ Dabei ist Delta Lake zu hundert Prozent mit Spark kompatibel.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 642

https://www.oraylis.de/wiki/azure-databricks, aufgerufen am 23.05.2024

Einführung in Databricks
MLflow

§ Eine Plattform zur Verwaltung von Workflows für maschinelles Lernen.

§ Dabei deckt MLflow den gesamten Machine-Learning-Lebenszyklus ab.

- Modelle können während des Trainings und der Ausführung überwacht

werden.

- Die lassen sich speichern, in den Produktionscode laden und schließlich in

eine Pipeline überführen.

§ Entsprechend wird MLflow vor allem von MLOps-Teams und für Data Science

verwendet.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 643

https://www.oraylis.de/wiki/azure-databricks, aufgerufen am 23.05.2024

Einführung in Databricks
Versprechen und Herausforderung

Databricks

§ Databricks bietet Ihnen die enorme Analyseleistung von Apache Spark in einer sehr

benutzerfreundlichen Weise. Benutzerfreundlichkeit ist wichtig.

§ So sollen die Nutzer Zeit damit damit verbringen, Daten zu betrachten, und sich nicht

mit den Feinheiten von Konfigurationsdateien, virtuellen Maschinen und
Netzwerkkonfigurationen auseinandersetzen.

- Es ist viel zu einfach, sich in der Technik zu verzetteln.

Ø Versprechen: Mit Databricks werden Sie das nicht.

- Trotzdem ist es eine Herausforderung, Programme so zu schreiben, dass sie die

Vorteile der Architektur ausnutzen.

- Darum soll es in den nachfolgenden Übungen insbesondere gehen.

Ilijason (2020)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 644

Einführung in Databricks
Als Analyseplattform

§ Auch wenn die Dinge über die Zeit einfacher geworden sind, ist es für viele immer noch zu

kompliziert (hohe Einstiegshürde), alles von Grund auf neu einzurichten.

- Damit ist u.a. das Einrichten von Apache Spark gemeint!

§ Cloud Computing und verteiltes Computing haben für analytisch denkende Menschen eine

erstaunliche Chance eröffnet.

§ Anstatt über die Infrastruktur nachzudenken, können Sie sich auf Geschäftsprobleme und

deren Lösung konzentrieren.

§ Und was noch besser ist: Sie erhalten auch Hilfe bei der Ausführung der Software. Cluster

werden automatisch skaliert und heruntergefahren, wenn Sie sie nicht nutzen.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 645

Ilijason (2020)

Einführung in Databricks
Managed Spark

§ Databricks ist Apache Spark, verpackt in einen Cloud-Service - vollständig verwaltet und mit

einer Reihe von Extras versehen.

§ Es wurde von Personen entwickelt, welche 2009 Spark erschaffen haben. So nutzt sie die Core-

Engine auf die beste Art und Weise.

§ Am wichtigsten ist jedoch, dass alle technischen Aspekte des Einstiegs wegfallen.

§ Bei Databricks sagen Sie dem System einfach, wie viele Worker Sie benötigen und wie

leistungsfähig diese sein sollen.

- Die Konfiguration und Bereitstellung wird vollautomatisiert für den Nutzer übernommen

- Virtuelle Maschinen werden gestartet, Linux-Images mit Spark angewendet, und in

wenigen Minuten sind Sie startklar.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 646

Ilijason (2020)

Einführung in Databricks
Kollaboratives Arbeiten

§ Dieses Pay-as-you-go-Modell ist für die meisten Unternehmen ein großer Vorteil von Databricks.

§ Databricks bietet zahlreiche Schnittstelle an, die wirklich gut ist.

- Sie sind minimalistisch, einfach zu bedienen und auf Zusammenarbeit ausgelegt.

- Mehrere Personen können z. B. zur gleichen Zeit am gleichen Notebook arbeiten.

- Das macht die gemeinsame Entwicklung auch über große Entfernungen hinweg möglich.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 647

Ilijason (2020)

Einführung in Databricks
Lakehouse Plattform

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 648

https://www.datanami.com/wp-content/uploads/2022/03/Databricks-Lakehouse-Platform-Chart.png, aufgerufen am 22.05.2024

Einführung in Databricks
Leader im Bereich Data Science und ML-Plattformen

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 649

https://databricks.com/de/blog/2021/03/04/databricks-named-a-leader-in-2021-gartner-magic-quadrant-for-data-science-and-
machine-learning-platforms.html, aufgerufen am 16.05.2024

Einführung in Databricks
Leader im Bereich Data Science und ML-Plattformen

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 650

https://databricks.com/de/blog/2021/03/04/databricks-named-a-leader-in-2021-gartner-magic-quadrant-for-data-science-and-
machine-learning-platforms.html

Einführung in Databricks
Die andere Seite des Databricks-Mondes

§ Databricks ist derzeit in folgenden Cloud-Anbietern (Hyperscaler) verfügbar:

1. Databricks on Google Cloud

2. Azure Databricks

3. Databricks on AWS

§ Andere möchten vielleicht andere Cloud-Anbieter als Amazon und Microsoft nutzen.

§ Derzeit ist Databricks weder auf IBM oder Oracle noch bei den kleineren Anbietern erhältlich.

§ Schließlich müssen Sie auch die Preise berücksichtigen: Apache Spark ist kostenlos.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 651

Ilijason (2020)

Einführung in Databricks
Storing Data

§ Es gibt auch eine Speicherebene zu berücksichtigen.

§ Ein Cluster benötigt Daten, die auf einem gemeinsamen Dateisystem verfügbar sind.

§ In  der  Welt  von  Apache  Spark  wird  häufig  das  Hadoop  Distributed  File  System  (HDFS)

verwendet. Dies ist jedoch keine Voraussetzung.

§ Wenn  Daten  in  Databricks  speichert  werden  sollen,  so  wird  das  Databricks  File  System

(DBFS) verwendet.

- Es ist ein verteiltes Dateisystem, auf das Sie über die Notebooks, den Code und die

Befehlszeilenschnittstelle (CLI) zugreifen können.

§ Es ist jedoch nicht zwingend ausschließlich Daten auf Databricks zu speichern.

- Sie können etwas wie Azure Blob Storage verwenden, um Ihre Daten zu speichern,
und sich einfach mit diesem verbinden. Dies ist sinnvoll, wenn Sie mehrere Tools oder
Arbeitsbereiche verwenden möchten.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 652

Ilijason (2020)

Einführung in Databricks
Cool components on top of Core

Die vier Komponenten sind

1. Spark Streaming,

2. Spark Machine Learning library (MLlib),

3. Spark GraphX und

4. Spark SQL.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 653

Ilijason (2020)

Einführung in Databricks
Community Edition

Community edition: No money? No problem!

§ Das Unternehmen war so freundlich, eine kostenlose Version anzubieten, mit der Sie die Software
ausprobieren können. Sowohl die Software als auch die Hardware sind kostenlos - es sind keine
Kreditkarteninformationen erforderlich.

§ Diese Version ist natürlich etwas eingeschränkt und hauptsächlich dazu gedacht das System

kennenzulernen

§ Mit der Community-Edition werden Sie keine Terabytes an Daten verarbeiten können. Was Sie

bekommen, ist ein Gefühl für die Benutzeroberfläche und die Notebooks.

§ Mit der kostenlosen Version erhalten Sie ein funktionierendes System mit nur einem 6-Gigabyte-

Driver-Node.

§ Es gibt keine Worker, so dass hier keine wirkliche Arbeitsverteilung stattfindet.

§ Auf den Notebooks ist keine Zusammenarbeit möglich, und nur drei Benutzer können eine Verbindung

zu verbinden.

§ Außerdem handelt es sich um eine öffentliche Umgebung.

Ilijason (2020)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 654

Einführung in Databricks
Community Edition

Wenn Sie das echte Databricks wollen, müssen Sie dafür bezahlen!

§ Die Community-Edition ist zwar gut, aber sie hilft Ihnen nicht bei der Lösung von Problemen, die

Sie vorher auf einem einzelnen Rechner nicht lösen konnten.

§ Um die volle Leistung zu erhalten, müssen Sie sich für eine der kommerziellen Editionen

entscheiden.

§ Data Engineering Light bietet Ihnen die Kernfunktionen mit Clustern und Notebooks fester

Größe.

§ Außerdem haben Sie die Möglichkeit, Aufträge mit Überwachung auszuführen. Das war's

auch schon.

§ Dies ist im Grunde eine abgespeckte Version für die Ausführung bekannter Aufgaben in der

Produktion.

§ Die höchste Stufe heißt Data Analytics und bietet hauptsächlich Funktionen für die

Zusammenarbeit.

Ilijason (2020)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 655

Einführung in Databricks
Workflow

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 656

Einführung in Databricks
Preise

§ Die Preisinformationen finden Sie unter
https://databricks.com/product/pricing

- Hier können Sie sich auch die Zahlen für den

Cloud-Anbieter Ihrer Wahl ansehen.

§ Zum Zeitpunkt der Erstellung dieser Folie (2024)

betrug der Preis für

- Data Engineer Light 0,07 $ pro Databricks Unit

(kurz DBU),

- Data Engineer 0,15 $ pro DBU und

- Data Analytics 0,40 $ pro DBU.

§ Diese Preise sind für beide Plattformen gleich,

decken aber nur den Databricks-Teil ab.

§ Die Cloud-Ressourcen sind extra, und hier kommt die

Variabilität ins Spiel!

Databricks Unit

- Eine Databricks Unit (DBU) ist eine

normalisierte Verarbeitungseinheit auf der
Databricks Lakehouse-Plattform und dient zu
Mess- und Abrechnungszwecken.

- Wie viele DBUs von einer Workload verbraucht

werden, hängt von den Verarbeitungsmetriken ab,
zu denen die benötigten Serverressourcen und
das verarbeitete Datenvolumen gehören.

https://databricks.com/product/pricing, aufgerufen am 23.05.2024

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 657

Einführung in Databricks
Azure Databricks

• Es sollte erwähnt werden, dass Microsoft in einer Investitionsrunden Beteiligung an Databricks

erworben hat.

• Dies könnte ein Grund für die offensichtliche Konzentration auf dieses spezielle Produkt sein, obwohl

das Unternehmen noch andere ähnliche Tools im Portfolio hat.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 658

Einführung in Databricks
Azure Preismodell

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 659

https://databricks.com/product/azure-pricing

Einführung in Databricks
Workload types

https://docs.databricks.com/administration-guide/account-settings/workload-types.html?_ga=2.249051271.181612431.1647866542- 1319855549.1647773636

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 660

Einführung in Databricks
Video: Was ist Databricks

https://www.oraylis.de/wiki/azure-databricks

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 661

Einführung in Databricks
Google Colab

Eine weitere Möglichkeit: Google Colab (Hosted Python)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 662

Databricks
Übung

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 663

Databricks Übung
Erstellen einer Databricks Community Edition Accounts

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 664

https://databricks.com/de/product/faq/community-edition

Databricks Übung
Erstellen einer Databricks Community Edition Accounts

Jetzt kostenlos einsteigen

1

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 665

https://databricks.com/de/

Databricks Übung
Erstellen einer Databricks Community Edition Accounts

https://databricks.com/de/try-databricks

2

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 666

Databricks Übung
Erstellen einer Databricks Community Edition Accounts

3

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 667

Databricks Übung
Databricks Community Edition - Übersicht

https://community.cloud.databricks.com

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 668

Databricks Übung
Databricks Community Edition - Übung

Nach dem Sie sich eingeloggt haben,
gehen Sie auf Compute

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 669

Databricks Übung
Databricks Community Edition - Übung

Erzeugen Sie ein neues
Cluster mit dem Namen
BDT-351-GX (dies kann
einige Minuten dauern):

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 670

Databricks Übung
Databricks Community Edition - Übung

Erzeugen Sie ein neues
Cluster mit dem Namen
BDT-351-GX (dies kann
einige Minuten dauern):

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 671

Databricks Übung
Databricks Community Edition - Übung

Prüfen Sie, ob der Cluster
angelegt wurde und
ordnungsgemäß läuft

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 672

Databricks Übung
Databricks Community Edition - Übung

Importieren Sie die Jupyter Notebook Datei  „BDT_Python_Basics.ipynb“ in Databricks
hoch (im Moodle hochgeladen)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 673

Databricks Übung
Databricks Community Edition - Übung

Laden Sie die Jupyter Notebook Datei „BDT_Python_Basics.ipynb“

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 674

Databricks Übung
Databricks Community Edition - Übung

Benennen Sie die Jupyter-Notebook Datei in „BDT-351-GX_Python_Basics.ipynb“ um (X
durch Ihre Gruppennummer ersetzen)

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 675

Databricks Übung
Databricks Community Edition - Übung

Verbinden Sie den Jupyter Notebook Datei mit dem Cluster

Ergebnis sollte wie folgt aussehen:

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 676

Databricks Übung
Databricks Community Edition - Übung

Führen Sie jede einzelne Zelle durch das drücken der Tastenkombination SHIFT + ENTER aus:

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 677

Databricks Übung
Databricks Community Edition - Übung

Alternativ gehen Sie auf den Reiter RUN und
wählen RUN CELL aus.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 678

Databricks Übung
Video - Python Einführung

Schauen Sie sich das folgende Video an
https://www.youtube.com/watch?v=xv5iIFTM4Uw

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 679

Databricks Übung
Databricks Community Edition - Übung

Für eine vollständige Beschreibung von Jupyter-Notebooks in Databricks siehe:

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 680

https://docs.databricks.com/notebooks/notebooks-code.html

Databricks Übung
Video: Pandas DataFrame

Schauen Sie sich das folgende Video über Pandas DataFrame unter
https://www.youtube.com/watch?v=e60ItwlZTKM an

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 681

Databricks Übung
Databricks Community Edition - Übung

§ Laden Sie sich die Jupyter-Notebook Datei „BDT_Übung_Jupyter_Notebook_Tutorial.ipynb“

herunter (Sie finden es in Moodle)

§ Das Notebook ist Ihnen vielleicht schon aus der KI-Vorlesung bekannt.

§ Gehen Sie alle Zellen durch und frischen Sie Ihr Grundverständnis der Python-Befehle und -

Konzepte im Notebook auf.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 682

Databricks Übung
Databricks Community Edition - Übung

§ Bislang haben wir einige Python-Grundlagen gelernt.

§ Sie können Python auf Ihrem Laptop  oder in einer gehosteten Python-Umgebung (z.B. Colab) laufen

lassen.

§ Oder in Databricks.

- Databricks bietet aber noch viel mehr. Insbesondere können Sie Programme auf Apache

Spark ausgeführt werden.

- Eine Schnittstelle ist PySpark oder Scala und SparkSQL.

- Mit PySpark kann man Python-Code schreiben, der Apache Spark-Funktionen nutzt. Z.B.

Spark Dataframes.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 683

Databricks Übung
Databricks Community Edition - Übung

Erkunden Sie jetzt das Quickstart-Tutorial: https://www.databricks.com/notebooks/gcp-qs-notebook.html

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 684

Databricks Übung
Databricks Community Edition - Übung

Erkunden Sie jetzt das Quickstart-Tutorial (ignorieren Sie die Zellen 7-9: /delta/diamonds)

This example
uses SparkSQL.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 685

Databricks Übung
Databricks Community Edition - Übung

Erkunden Sie jetzt das Quickstart-Tutorial (ignorieren Sie die Zellen 7-9: /delta/diamonds)

This example
uses PySpark.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 686

Databricks Übung
Databricks Community Edition - Übung

Erkunden Sie jetzt das Quickstart-Tutorial (ignorieren Sie die Zellen 7-9: /delta/diamonds)

§ Dies ist ein Spark-DatenFrame (und KEIN Pandas-Datenframe).

§ Zwischen Spark und Pandas DataFrame gibt es ein RIESIGER Unterschied (vom
Standpunkt der Architektur aus gesehen). In der Vorlesung und den folgenden
Übungen finden Sie weitere Einzelheiten.

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 687

Databricks Übung
Databricks Community Edition - Übung

Finden Sie die richtigen Python-Befehle, um die folgenden Ausgaben aus dem Datensatz
diamonds :

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 688

Databricks Übung
Databricks Community Edition - Übung

Finden Sie die richtigen Python-Befehle, um die folgenden Ausgaben aus dem
Datensatz diamonds :

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 689

Databricks Übung
Python for Data Science Pyspark Cheat Sheet

Download und nutzen:

Hochschule Hannover

Prof. Dr. Suat Can | Big-Data-Technologien | Sommersemester 2025

Seite 690

https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_SQL_Cheat_Sheet_Python.pdf

