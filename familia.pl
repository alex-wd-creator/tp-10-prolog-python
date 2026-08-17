es_padre(cronos,zeus).
es_padre(cronos,poseidon).
es_padre(zeus,kratos).
es_padre(kratos,calliope).
es_padre(kratos,atreus).

es_madre(rhea,zeus).
es_madre(callisto,kratos).
es_madre(freyja,baldur).
es_madre(lysandra,calliope).
es_madre(laufey,atreus).

es_tio(poseidon,kratos) :- es_padre(zeus,kratos),es_hermano(poseidon,zeus).

es_hermano(calliope,atreus) :- es_padre(kratos,calliope),es_padre(kratos,atreus).
es_hermano(poseidon,zeus) :- es_padre(cronos,zeus),es_padre(cronos,poseidon).


es_abuelo(cronos,kratos) :- es_padre(cronos,zeus),es_padre(zeus,kratos).
es_abuelo(zeus,calliope) :- es_padre(kratos,calliope),es_padre(zeus,kratos).
es_abuelo(zeus,atreus) :- es_padre(kratos,atreus),es_padre(zeus,kratos).


es_abuela(rhea,kratos) :- es_madre(rhea,zeus),es_padre(zeus,kratos).
es_abuela(callisto,calliope) :- es_padre(kratos,calliope),es_madre(callisto,kratos).
es_abuela(callisto,atreus) :- es_padre(kratos,atreus),es_madre(callisto,kratos).

% CONSULTAS

% es_padre(cronos,zeus). true
% es_madre(laufey,atreus). true
% es_tio(poseidon,kratos). true
% es_hermano(poseidon,zeus). true
% es_abuelo(zeus,calliope). true
% es_abuela(rhea,kratos). true