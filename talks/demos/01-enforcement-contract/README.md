# Demo 1 — Enforcement-Contract

## Architekturfrage
> **Wie erzwingt man Regeln außerhalb des Modells?**

## Worum es geht
Ein Agent *will* schreiben — darf aber nicht, solange kein freigegebener Plan existiert.
Die Regel steckt **nicht** im Prompt (das wäre eine Bitte), sondern in einem
**deklarativen Vertrag**, der *außerhalb der Prompt-Schicht* ausgewertet wird.

Die zentrale Aussage der Demo:
> Erzwingbarkeit ist eine **Architektur-Eigenschaft**, kein Implementierungs-Detail.
> Die Datei [`contract.yaml`](contract.yaml) **ist** der Vertrag — wer ihn auswertet (Hook,
> Proxy, CI-Step), ist austauschbar und bewusst nebensächlich.

## Dateien (alle deklarativ — kein Code)
| Datei | Rolle |
|-------|-------|
| [`contract.yaml`](contract.yaml) | Der Vertrag: Auslöser → Bedingung → Verdict. Sprach-/runtime-agnostisch. |
| [`state.json`](state.json) | Der Zustand, gegen den geprüft wird (`plan.approved`). |
| [`expected-output.md`](expected-output.md) | Das vorbereitete Ergebnis der Auswertung — zum Zeigen / als Screencast-Vorlage. |

## Live-Ablauf (3 Min) — ohne Code
1. [`contract.yaml`](contract.yaml) zeigen — **Auslöser** (`on.tool: Write`), **Bedingung**
   (`when.not.state: plan.approved`), **Verdict** (`block`). Das ist die ganze Architektur.
2. [`state.json`](state.json) zeigen — der Plan ist **nicht** freigegeben.
3. [`expected-output.md`](expected-output.md) zeigen — Szenario A: **BLOCK**. Dann
   `plan.approved` auf `true` gedacht → Szenario B: **ALLOW**. `Read` → nie betroffen.

> Statt eines Skripts zeigt die Demo das **Artefakt + das vorbereitete Verdict**. Wer es live
> ausführen will, lässt eine beliebige Runtime den Vertrag auswerten — das Ergebnis ist
> dasselbe, weil es allein aus Vertrag + Zustand folgt.

## Was die Zuhörer mitnehmen
- Der **Auslöser** (`on.tool`), die **Bedingung** (`when`) und das **Verdict** sind explizit
  und versionierbar — kein verstecktes Verhalten im Prompt.
- Das Modell kann den Vertrag **nicht umgehen**, weil er außerhalb seiner Reichweite greift.
- Tauscht man die auswertende Runtime (Hook, Proxy, CI-Step), bleibt der Vertrag identisch.
  *Die Architektur liegt im Vertrag, nicht im Code.*
