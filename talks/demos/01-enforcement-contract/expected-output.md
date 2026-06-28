# Erwartetes Ergebnis (zum Vorführen)

Diese Datei zeigt, **was die Auswertung des Vertrags ergibt** — ohne Code. So sieht der
Screencast / das Terminal in der Live-Demo aus. Die Auswertung kann jede Runtime
übernehmen (Hook, Proxy, CI-Step); das Ergebnis ist immer dasselbe, weil es allein aus
[`contract.yaml`](contract.yaml) + [`state.json`](state.json) folgt.

## Szenario A — Agent will schreiben, Plan ist NICHT freigegeben

```
state.json:   { "plan": { "approved": false } }
Aktion:       Write
Auslöser?     ja  (contract.on.tool == Write)
Bedingung?    erfüllt  (when.not.state: plan.approved == false)
─────────────────────────────────────────────────────────────
VERDICT:      BLOCK
MESSAGE:      Kein freigegebener Plan vorhanden. Schreibzugriff blockiert.
              Erst die Exploration abschliessen und Gate G2 freigeben.
```

## Szenario B — Plan freigegeben (Mensch hat G2 passiert)

```
state.json:   { "plan": { "approved": true } }
Aktion:       Write
Auslöser?     ja
Bedingung?    NICHT erfüllt  (plan.approved == true)
─────────────────────────────────────────────────────────────
VERDICT:      ALLOW
```

## Szenario C — Lesezugriff ist nie betroffen

```
Aktion:       Read
Auslöser?     nein  (contract.on.tool == Write, nicht Read)
─────────────────────────────────────────────────────────────
VERDICT:      ALLOW  (kein Auslöser im Vertrag)
```

> Kernaussage: Der **Auslöser**, die **Bedingung** und das **Verdict** stehen vollständig im
> Vertrag. Das Modell kann das Ergebnis nicht beeinflussen — die Regel greift außerhalb
> seiner Reichweite.
