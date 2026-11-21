# Come contribuire

Grazie dell'interesse. Questo file è la guida predefinita per i repository che
non ne hanno una propria: se il repository contiene un `CONTRIBUTING.md` suo,
vale quello.

## Prima di cominciare

- Per una modifica di grandi dimensioni apri prima una *issue* o una
  *discussione*: si evita lavoro buttato se la direzione non è condivisa.
- Cerca tra le issue aperte e chiuse: il problema potrebbe essere già noto.
- Le domande generiche vanno nelle **Discussioni** del repository, non nelle
  issue.

## Preparare e proporre una modifica

1. Fai un *fork* e crea un ramo dedicato a partire da `main` aggiornato.
2. Leggi il `README.md` del repository per i comandi di build e di test: le
   modifiche vanno provate con quelli.
3. Una modifica al comportamento si accompagna a un test; per una correzione,
   il test che riproduce il difetto.
4. Aggiorna la documentazione e il `CHANGELOG.md` se cambia qualcosa di
   visibile.
5. Apri una *pull request* compilando il modello: cosa cambia, perché, come
   l'hai provato.

## Commit e pull request atomiche

- Una sola modifica coerente per commit e per pull request: un fix, una
  funzione, una configurazione collegata. Non mescolare riscritture, fix CI,
  aggiornamenti di dipendenze e documentazione non correlata.
- Messaggio in italiano, prima riga breve e all'indicativo ("aggiunge il filtro
  per tipo"); il corpo spiega il *perché* quando serve e come è stata verificata
  la modifica.
- I controlli (test, lint, security scan) devono passare senza errori, warning o
  soppressioni generiche.
- Niente segreti, chiavi, dati personali, file generati o tracce di strumenti
  automatici nel diff.
- Mai riscrivere la storia di un ramo già pubblicato.

## Revisione

Una pull request viene unita quando i controlli automatici sono verdi e i
commenti di revisione sono risolti. Il progetto è mantenuto nel tempo libero:
le risposte possono non essere immediate.

## Licenza dei contributi

Contribuendo accetti che il tuo lavoro sia distribuito con la licenza del
repository a cui contribuisci. Non serve firmare nulla.

## Sicurezza

Per le vulnerabilità non aprire una issue pubblica: segui
[SECURITY.md](SECURITY.md).
